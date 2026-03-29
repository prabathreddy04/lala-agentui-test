#!/usr/bin/env python3
"""
zip_directory.py
Converts a folder (and all its contents) into a zip archive.

Usage:
    python zip_directory.py <source_directory> [options]

Examples:
    python zip_directory.py /path/to/folder
    python zip_directory.py /path/to/folder --output my_archive.zip
    python zip_directory.py /path/to/folder --output /tmp/backup.zip --exclude .git __pycache__ *.pyc
"""

import argparse
import fnmatch
import os
import sys
import zipfile
from datetime import datetime
from pathlib import Path


def should_exclude(path: str, exclude_patterns: list[str]) -> bool:
    """Return True if any part of the path matches an exclude pattern."""
    parts = Path(path).parts
    for pattern in exclude_patterns:
        # Match against each path component and the full relative path
        if any(fnmatch.fnmatch(part, pattern) for part in parts):
            return True
        if fnmatch.fnmatch(path, pattern):
            return True
    return False


def zip_directory(
    source_dir: str,
    output_zip: str,
    exclude_patterns: list[str],
    verbose: bool = True,
) -> tuple[int, int]:
    """
    Zip all files in source_dir into output_zip.

    Returns:
        (files_added, files_skipped) counts
    """
    source_path = Path(source_dir).resolve()

    if not source_path.exists():
        print(f"[ERROR] Source directory does not exist: {source_path}", file=sys.stderr)
        sys.exit(1)

    if not source_path.is_dir():
        print(f"[ERROR] Source path is not a directory: {source_path}", file=sys.stderr)
        sys.exit(1)

    files_added = 0
    files_skipped = 0

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source_path):
            # Compute the relative path from source for exclusion checks
            rel_root = os.path.relpath(root, source_path)

            # Prune excluded subdirectories in-place so os.walk skips them
            dirs[:] = [
                d for d in dirs
                if not should_exclude(
                    os.path.join(rel_root, d) if rel_root != "." else d,
                    exclude_patterns,
                )
            ]

            for filename in files:
                rel_file = (
                    os.path.join(rel_root, filename)
                    if rel_root != "."
                    else filename
                )

                if should_exclude(rel_file, exclude_patterns):
                    if verbose:
                        print(f"  [SKIP]  {rel_file}")
                    files_skipped += 1
                    continue

                abs_file = os.path.join(root, filename)
                arcname = os.path.join(source_path.name, rel_file)

                if verbose:
                    print(f"  [ADD]   {arcname}")

                zf.write(abs_file, arcname)
                files_added += 1

    return files_added, files_skipped


def human_readable_size(path: str) -> str:
    size = os.path.getsize(path)
    for unit in ("B", "KB", "MB", "GB"):
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} TB"


def main():
    parser = argparse.ArgumentParser(
        description="Zip a directory and all its contents into a single archive.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "source",
        help="Path to the root directory you want to zip.",
    )
    parser.add_argument(
        "--output", "-o",
        default=None,
        help=(
            "Path for the output .zip file. "
            "Defaults to <source_folder_name>_<timestamp>.zip in the current directory."
        ),
    )
    parser.add_argument(
        "--exclude", "-e",
        nargs="*",
        default=[],
        metavar="PATTERN",
        help=(
            "Glob patterns to exclude (e.g. .git __pycache__ *.log). "
            "Matched against file/folder names and relative paths."
        ),
    )
    parser.add_argument(
        "--quiet", "-q",
        action="store_true",
        help="Suppress per-file output; show only the summary.",
    )

    args = parser.parse_args()

    source_dir = args.source
    source_name = Path(source_dir).resolve().name

    if args.output:
        output_zip = args.output
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_zip = f"{source_name}_{timestamp}.zip"

    print(f"\n{'='*55}")
    print(f"  Source  : {Path(source_dir).resolve()}")
    print(f"  Output  : {Path(output_zip).resolve()}")
    if args.exclude:
        print(f"  Exclude : {', '.join(args.exclude)}")
    print(f"{'='*55}\n")

    added, skipped = zip_directory(
        source_dir=source_dir,
        output_zip=output_zip,
        exclude_patterns=args.exclude,
        verbose=not args.quiet,
    )

    zip_size = human_readable_size(output_zip)

    print(f"\n{'='*55}")
    print(f"  Done!")
    print(f"  Files added   : {added}")
    print(f"  Files skipped : {skipped}")
    print(f"  Archive size  : {zip_size}")
    print(f"  Saved to      : {Path(output_zip).resolve()}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()