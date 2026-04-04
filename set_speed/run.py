#!/usr/bin/env -S uv run
# /// script
# dependencies = ["requests"]
# ///

import json
import sys
from pathlib import Path

import requests


def main() -> None:
    """Set the TTS playback speed on the HAVPE server."""
    config = json.loads(Path("../config.json").read_text())
    params = json.load(sys.stdin)

    response = requests.put(
        f"{config['havpe_url']}/settings",
        auth=("plugin", config["api_password"]),
        json={"tts_speed": params["speed"]},
    )
    response.raise_for_status()

    json.dump(response.json(), sys.stdout)


main()
