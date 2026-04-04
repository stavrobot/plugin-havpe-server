#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests"]
# ///

import json
import sys
from pathlib import Path

import requests


def main() -> None:
    """Set the STT language on the HAVPE server."""
    config = json.loads(Path("../config.json").read_text())
    params = json.load(sys.stdin)

    response = requests.put(
        f"{config['havpe_url']}/settings",
        auth=("plugin", config["api_password"]),
        json={"stt_language": params["language"]},
    )
    response.raise_for_status()

    json.dump(response.json(), sys.stdout)


main()
