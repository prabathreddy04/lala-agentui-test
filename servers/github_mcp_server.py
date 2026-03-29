from fastmcp import FastMCP
import subprocess
import sys
from pathlib import Path

mcp = FastMCP(name="github-tool")

SCRIPT_PATH = Path(__file__).parent.parent / "tools" / "github_tool.py"

@mcp.tool
def push_to_github(
    folder: str,
    repo_name: str,
    commit_message: str = "Automated push via Claude Code",
    private: bool = False,
    description: str = ""
) -> str:
    """Push a local folder to GitHub. Creates the repo automatically if it doesn't exist.
    No git required — uploads files directly via GitHub API.

    Args:
        folder: Absolute path to the folder you want to push
        repo_name: Name of the GitHub repository (will be created if it doesn't exist)
        commit_message: Commit message for the upload (default: 'Automated push via Claude Code')
        private: Whether to make the repo private (default: False)
        description: Optional description for the GitHub repo
    """
    cmd = [
        sys.executable, str(SCRIPT_PATH),
        folder,
        repo_name,
        "--message", commit_message,
        "--description", description
    ]
    if private:
        cmd.append("--private")

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout or result.stderr

if __name__ == "__main__":
    mcp.run(transport="stdio")