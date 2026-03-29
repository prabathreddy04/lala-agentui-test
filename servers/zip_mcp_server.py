from fastmcp import FastMCP
import subprocess
import sys
from pathlib import Path

mcp = FastMCP(name="zip-tool")

SCRIPT_PATH = Path(__file__).parent.parent / "tools" / "zip_directory.py"

@mcp.tool
def zip_directory(source: str, output: str = "", exclude: str = "") -> str:
    """Zip a directory into a .zip archive.

    Args:
        source: Path to the folder you want to zip
        output: (Optional) Output .zip file path
        exclude: (Optional) Space-separated glob patterns to exclude e.g. '.git __pycache__'
    """
    cmd = [sys.executable, str(SCRIPT_PATH), source]
    if output:
        cmd += ["--output", output]
    if exclude:
        cmd += ["--exclude"] + exclude.split()

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or result.stderr

if __name__ == "__main__":
    mcp.run(transport="stdio")