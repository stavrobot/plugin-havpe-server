#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests"]
# ///

import json
import sys
from pathlib import Path

import requests


def main() -> None:
    """Get the current settings from the HAVPE server."""
    config = json.loads(Path("../config.json").read_text())
    json.load(sys.stdin)  # consume stdin even though no parameters are expected

    response = requests.get(
        f"{config['havpe_url']}/settings",
        auth=("plugin", config["api_password"]),
    )
    response.raise_for_status()

    json.dump(response.json(), sys.stdout)


main()
