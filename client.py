#!/usr/bin/env python3

from rich.console import Console
import subprocess
import textwrap
import json
import sys

PROGRAM = "AetherTopia"
DESCRIPTION = "A text-based multiplayer game"
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

      help              Show commands list
      exit              Exit game
      update            Update game
      play offline      Singleplayer
    """)
    )


def get_data(category, key=None, subkey=None):
    with open("data.json", "r") as f:
        data = json.load(f)
    
    if key:
        if subkey:
            return data[category][key][subkey]
        return data[category][key]
    return data[category]


def edit_data(action, category, key=None, subkey=None, value=None):
    with open("data.json", "r") as f:
        data = json.load(f)
    
    if action == "add":
        if subkey:
            data[category][key][subkey] = value
        elif key:
            data[category][key] = value
        else:
            data[category] = value

    elif action == "update":
        if subkey:
            data[category][key][subkey] = value
        elif key:
            data[category][key] = value
        else:
            data[category] = value

    elif action == "remove":
        if subkey:
            del data[category][key][subkey]
        elif key:
            del data[category][key]
        else:
            del data[category]

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)


def main():
    while True:
        cmd = input("> ").strip().lower()

        if cmd == "exit":
            raise KeyboardInterrupt

        elif cmd == "help":
            print_help()

        elif cmd == "play offline":
            username = input("Username: ")
            print(f"Logging on {username}...")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        error_console.log(f"Error: {e}")
        sys.exit(1)
        
