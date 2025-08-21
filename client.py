#!/usr/bin/env python3

from rich.console import Console
from rich.panel import Panel
import subprocess
import textwrap
import sys

PROGRAM = "AetherTopia"
DESCRIPTION = "A text-based multiplayer"
AUTHOR = "batubyte"
VERSION = "0.1.0"

console = Console()
error_console = Console(stderr=True, style="bold red")


def update():
    subprocess.run(
        ["pipx", "install", "--force", "git+https://github.com/batubyte/AetherTopia"],
        check=True,
    )


def print_help():
    print(textwrap.dedent(f"""
    {PROGRAM} by {AUTHOR}, version-{VERSION}

      help      Show commands list
      exit      Exit app
    """)
    )


def main():
    while True:
        cmd = input("> ").strip().lower()

        if cmd == "exit":
            raise KeyboardInterrupt

        elif cmd == "help":
            print_help()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error_console.log(f"Error: {e}")
        sys.exit(1)
        
