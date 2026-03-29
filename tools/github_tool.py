#!/usr/bin/env python3
"""
github_tool.py
Pushes a local folder to GitHub using the GitHub Contents API.
- No git required
- Creates the repo automatically if it doesn't exist
- Uploads every file in the folder directly via API
"""

import os
import base64
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load PAT from .env file
load_dotenv(Path(__file__).parent.parent / ".env")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_API = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}


def validate_env() -> str | None:
    """Check that required env vars are set."""
    if not GITHUB_TOKEN:
        return "GITHUB_TOKEN is not set in your .env file."
    if not GITHUB_USERNAME:
        return "GITHUB_USERNAME is not set in your .env file."
    return None


def create_repo_if_not_exists(repo_name: str, private: bool = False, description: str = "") -> tuple[bool, str]:
    """Create a GitHub repo if it doesn't already exist. Returns (success, repo_url)."""

    # Check if repo already exists
    check = requests.get(f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{repo_name}", headers=HEADERS)
    if check.status_code == 200:
        repo_url = check.json().get("html_url", "")
        print(f"[INFO] Repo already exists: {repo_url}")
        return True, repo_url

    # Create the repo
    print(f"[INFO] Creating new repo: {repo_name} ...")
    payload = {
        "name": repo_name,
        "description": description,
        "private": private,
        "auto_init": False
    }
    response = requests.post(f"{GITHUB_API}/user/repos", json=payload, headers=HEADERS)
    if response.status_code == 201:
        repo_url = response.json().get("html_url", "")
        print(f"[INFO] Repo created: {repo_url}")
        return True, repo_url

    return False, response.json().get("message", "Unknown error creating repo")


def upload_file(repo_name: str, file_path: Path, relative_path: str, commit_message: str) -> tuple[bool, str]:
    """Upload a single file to GitHub via the Contents API."""

    # Read and encode file content as base64
    try:
        content = file_path.read_bytes()
        encoded = base64.b64encode(content).decode("utf-8")
    except Exception as e:
        return False, f"Could not read file {relative_path}: {e}"

    url = f"{GITHUB_API}/repos/{GITHUB_USERNAME}/{repo_name}/contents/{relative_path}"

    # Check if file already exists (needed to get its SHA for updates)
    sha = None
    existing = requests.get(url, headers=HEADERS)
    if existing.status_code == 200:
        sha = existing.json().get("sha")

    # Build the payload
    payload = {
        "message": commit_message,
        "content": encoded,
    }
    if sha:
        payload["sha"] = sha  # Required by GitHub API to update an existing file

    response = requests.put(url, json=payload, headers=HEADERS)
    if response.status_code in (200, 201):
        return True, relative_path
    return False, f"{relative_path}: {response.json().get('message', 'Unknown error')}"


def push_folder_to_github(
    folder_path: str,
    repo_name: str,
    commit_message: str = "Automated push via Claude Code",
    private: bool = False,
    description: str = "",
    exclude: list[str] = None
) -> str:
    """
    Main function: push a local folder to GitHub without using git.
    Creates the repo if it doesn't exist, uploads all files via API.
    """

    # Validate credentials
    error = validate_env()
    if error:
        return f"[ERROR] {error}"

    # Validate folder
    folder = Path(folder_path).resolve()
    if not folder.exists():
        return f"[ERROR] Folder does not exist: {folder}"
    if not folder.is_dir():
        return f"[ERROR] Path is not a directory: {folder}"

    # Default exclusions
    if exclude is None:
        exclude = [".git", "__pycache__", ".env", "*.pyc", "node_modules", ".DS_Store"]

    # Create repo if needed
    success, result = create_repo_if_not_exists(repo_name, private=private, description=description)
    if not success:
        return f"[ERROR] Failed to create repo: {result}"

    repo_url = result

    # Walk through all files and upload them
    files_uploaded = 0
    files_failed = []

    print(f"[INFO] Uploading files from: {folder}")

    for file_path in sorted(folder.rglob("*")):
        if not file_path.is_file():
            continue

        # Check exclusions
        relative_path = file_path.relative_to(folder)
        parts = relative_path.parts
        skip = False
        for pattern in exclude:
            if any(part == pattern or part.endswith(pattern.lstrip("*")) for part in parts):
                skip = True
                break
        if skip:
            print(f"  [SKIP] {relative_path}")
            continue

        # Upload file
        print(f"  [UPLOAD] {relative_path}")
        ok, msg = upload_file(
            repo_name=repo_name,
            file_path=file_path,
            relative_path=str(relative_path),
            commit_message=commit_message
        )
        if ok:
            files_uploaded += 1
        else:
            files_failed.append(msg)

    # Summary
    print(f"\n[INFO] Upload complete.")
    print(f"  Files uploaded : {files_uploaded}")
    print(f"  Files failed   : {len(files_failed)}")

    if files_failed:
        failed_list = "\n  ".join(files_failed)
        return (
            f"[PARTIAL SUCCESS] {files_uploaded} files pushed to {repo_url}\n"
            f"  Failed files:\n  {failed_list}"
        )

    return f"[SUCCESS] {files_uploaded} files pushed to {repo_url}"


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Push a folder to GitHub using the Contents API.")
    parser.add_argument("folder", help="Path to the folder to push")
    parser.add_argument("repo_name", help="GitHub repository name")
    parser.add_argument("--message", "-m", default="Automated push via Claude Code", help="Commit message")
    parser.add_argument("--private", action="store_true", help="Make the repo private")
    parser.add_argument("--description", "-d", default="", help="Repo description")
    args = parser.parse_args()

    result = push_folder_to_github(
        folder_path=args.folder,
        repo_name=args.repo_name,
        commit_message=args.message,
        private=args.private,
        description=args.description
    )
    print(result)