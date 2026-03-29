#!/usr/bin/env python3
"""
check_env.py
Diagnostic script to verify .env file is being read correctly
before making any changes to the MCP tools.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# ── Paths to check ────────────────────────────────────────────
ENV_PATHS = [
    Path("/home/prabath-reddy/Hackathon/agentui/.env"),
    Path(__file__).parent / ".env",
    Path(__file__).parent.parent / ".env",
    Path.home() / ".env",
]

REQUIRED_KEYS = ["GITHUB_TOKEN", "GITHUB_USERNAME"]

# ── Helper ────────────────────────────────────────────────────
def mask(value: str) -> str:
    """Show only first 10 and last 4 chars of a secret."""
    if not value:
        return "None"
    if len(value) <= 14:
        return "***"
    return f"{value[:10]}...{value[-4:]}"

# ── Check each path ───────────────────────────────────────────
print("\n" + "="*55)
print("  ENV DIAGNOSTIC CHECK")
print("="*55)

found_env = None

for env_path in ENV_PATHS:
    exists = env_path.exists()
    print(f"\n  Path : {env_path}")
    print(f"  Found: {'✓ Yes' if exists else '✗ No'}")

    if exists:
        # Try loading it
        load_dotenv(env_path, override=True)
        token = os.getenv("GITHUB_TOKEN")
        username = os.getenv("GITHUB_USERNAME")

        print(f"  GITHUB_TOKEN    : {mask(token)}")
        print(f"  GITHUB_USERNAME : {username or 'None'}")

        if token and username:
            found_env = env_path
            print(f"  Status: ✓ All required keys found!")
        else:
            missing = [k for k in REQUIRED_KEYS if not os.getenv(k)]
            print(f"  Status: ✗ Missing keys: {', '.join(missing)}")

# ── Summary ───────────────────────────────────────────────────
print("\n" + "="*55)
if found_env:
    print(f"  ✓ Working .env found at:\n    {found_env}")
    print(f"\n  Use this in your tool:")
    print(f'    load_dotenv("{found_env}")')
else:
    print("  ✗ No working .env found in any of the checked paths!")
    print("\n  Fix: Make sure your .env file exists and contains:")
    print("    GITHUB_TOKEN=your_token_here")
    print("    GITHUB_USERNAME=your_username_here")
print("="*55 + "\n")