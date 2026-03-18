#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests"]
# ///

import json
import sys
from pathlib import Path

import requests


def main() -> None:
    """Remove a shortcut from the HAVPE server by its 0-based index."""
    config = json.loads(Path("../config.json").read_text())
    params = json.load(sys.stdin)

    response = requests.delete(
        f"{config['havpe_url']}/shortcuts/{params['index']}",
        auth=("plugin", config["api_password"]),
    )
    response.raise_for_status()

    json.dump({"result": response.text}, sys.stdout)


main()
