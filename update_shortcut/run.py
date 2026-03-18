#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests"]
# ///

import json
import sys
from pathlib import Path

import requests


def main() -> None:
    """Update an existing shortcut on the HAVPE server by its 0-based index."""
    config = json.loads(Path("../config.json").read_text())
    params = json.load(sys.stdin)

    response = requests.put(
        f"{config['havpe_url']}/shortcuts/{params['index']}",
        auth=("plugin", config["api_password"]),
        json=[params["regex"], params["url"]],
    )
    response.raise_for_status()

    json.dump({"result": response.text}, sys.stdout)


main()
