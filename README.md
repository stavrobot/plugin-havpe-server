# havpe-server plugin

A [Stavrobot](https://github.com/skorokithakis/stavrobot) plugin for managing voice command shortcuts on a [HAVPE server](https://github.com/skorokithakis/havpe-server). HAVPE server is a standalone voice pipeline backend for the Home Assistant Voice Preview Edition (HAVPE) device.

Shortcuts let you short-circuit the normal voice pipeline so that specific spoken phrases trigger a URL directly (e.g. a Home Assistant webhook) without going through the LLM. This plugin lets you list, add, update, and remove those shortcuts.

## Installation

Tell Stavrobot to install `https://github.com/stavrobot/plugin-havpe-server`

After installation, configure the plugin with your server details:

- `havpe_url`: Base URL of the HAVPE server (e.g. `http://192.168.1.50:8085`)
- `api_password`: API password for Basic Auth
