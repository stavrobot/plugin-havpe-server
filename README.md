# havpe-server plugin

A [Stavrobot](https://github.com/skorokithakis/stavrobot) plugin for managing voice command shortcuts and runtime settings on a [HAVPE server](https://github.com/skorokithakis/havpe-server). HAVPE server is a standalone voice pipeline backend for the Home Assistant Voice Preview Edition (HAVPE) device.

Shortcuts let you short-circuit the normal voice pipeline so that specific spoken phrases trigger a URL directly (e.g. a Home Assistant webhook) without going through the LLM. Settings let you control runtime behaviour such as STT language and TTS playback speed. This plugin lets you list, add, update, and remove shortcuts, and read or update those settings.

## Installation

Tell Stavrobot to install `https://github.com/stavrobot/plugin-havpe-server`

After installation, configure the plugin with your server details:

- `havpe_url`: Base URL of the HAVPE server (e.g. `http://192.168.1.50:8085`)
- `api_password`: API password for Basic Auth

## Tools

### Shortcuts

- **`list_shortcuts`** — List all voice command shortcuts. Returns each shortcut's index, regex pattern, and URL. No parameters.

- **`add_shortcut`** — Add a new shortcut. The regex is matched case-insensitively and should tolerate spurious punctuation that speech-to-text may insert.
  - `regex`: Pattern to match spoken phrases.
  - `url`: URL to call when the pattern matches.

- **`update_shortcut`** — Update an existing shortcut by its 0-based index. Use `list_shortcuts` to find the index.
  - `index`: 0-based index of the shortcut to update.
  - `regex`: New regex pattern.
  - `url`: New URL.

- **`remove_shortcut`** — Remove a shortcut by its 0-based index. Use `list_shortcuts` to find the index.
  - `index`: 0-based index of the shortcut to remove.

### Settings

These tools manage runtime settings on the HAVPE server.

- **`get_settings`** — Return the current STT language and TTS playback speed configured on the device. No parameters.

- **`set_speed`** — Set the TTS playback speed (how fast the assistant speaks).
  - `speed`: Playback speed in the range 0.7 (slower) to 1.2 (faster). Default is 1.0.

- **`set_language`** — Set the STT language used to transcribe spoken audio.
  - `language`: ElevenLabs STT language code (e.g. `en`, `es`, `fr`). Default is `en`.
