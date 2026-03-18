#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests"]
# ///

import json
import sys
from pathlib import Path

import requests


def main() -> None:
    """List all shortcuts from the HAVPE server, including their 0-based index."""
    config = json.loads(Path("../config.json").read_text())
    json.load(sys.stdin)  # consume stdin even though no parameters are expected

    response = requests.get(
        f"{config['havpe_url']}/shortcuts",
        auth=("plugin", config["api_password"]),
    )
    response.raise_for_status()

    shortcuts = response.json()
    result = [[index, regex, url] for index, (regex, url) in enumerate(shortcuts)]
    json.dump({"shortcuts": result}, sys.stdout)


main()
