# Python IRC Chat Client

A simple, graphical IRC (Internet Relay Chat) client built with Python and Tkinter. Connect to IRC servers, join channels, and chat with others in a user-friendly interface.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- 🌐 Connect to any IRC server
- 💬 Join and leave channels
- 📝 Send messages and view chat history
- 🎨 Color-coded message types (server messages, errors, user messages)
- ⚡ Real-time message receiving with threading
- 🔧 Support for IRC commands
- 🖥️ Clean, intuitive GUI interface

## Screenshots

The client features a simple interface with connection controls, channel management, and a scrollable chat window.

## Requirements

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/python-irc-client.git
cd python-irc-client
```

2. No additional dependencies needed! The client uses only Python standard library modules.

## Usage

Run the client:
```bash
python3 irc_client.py
```

### Connecting to a Server

1. Enter the IRC server address (e.g., `irc.libera.chat`)
2. Enter the port (usually `6667` for non-SSL, `6697` for SSL)
3. Choose a nickname
4. Click "Connect"

### Joining a Channel

1. Enter the channel name (with or without `#` prefix)
2. Click "Join"
3. Start chatting!

### Available Commands

The client supports standard IRC commands prefixed with `/`:

- `/join #channel` - Join a channel
- `/part` or `/leave` - Leave the current channel
- `/msg nickname message` - Send a private message
- `/nick newnick` - Change your nickname
- `/quit` - Disconnect from the server

You can also send raw IRC commands by typing them with a `/` prefix.

## Popular IRC Servers

Here are some popular public IRC servers to try:

- **Libera.Chat**: `irc.libera.chat:6667` - Popular for open source projects
- **OFTC**: `irc.oftc.net:6667` - Open and Free Technology Community
- **Rizon**: `irc.rizon.net:6667` - General chat and anime community

## How It Works

The client uses Python's built-in `socket` library to establish a TCP connection to IRC servers and communicate using the IRC protocol (RFC 1459). A separate thread handles incoming messages to keep the GUI responsive.

### Message Flow

1. **Connection**: Sends `NICK` and `USER` commands during handshake
2. **Keep-alive**: Automatically responds to server `PING` requests with `PONG`
3. **Channels**: Uses `JOIN` and `PART` commands for channel management
4. **Messaging**: Sends `PRIVMSG` commands to post messages

## Project Structure
```
python-irc-client/
├── irc_client.py       # Main application file
├── README.md           # This file
├── LICENSE             # MIT License
├── .gitignore          # Git ignore rules
└── requirements.txt    # Python dependencies (none required)
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- Add SSL/TLS support for secure connections
- Implement multi-channel tabs
- Add user list display for channels
- Support for IRC color codes
- Message logging to files
- Custom themes/color schemes
- Auto-reconnect functionality

## Known Limitations

- No SSL/TLS support (only unencrypted connections)
- Single channel view at a time
- No persistent configuration
- Basic error handling

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python's standard library
- IRC protocol specification: [RFC 1459](https://tools.ietf.org/html/rfc1459)
- Inspired by the classic IRC chat experience

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/python-irc-client/issues) page
2. Create a new issue if your problem isn't already listed
3. Provide details about your Python version, OS, and the error message

## Author

Your Name - [your-email@example.com](mailto:your-email@example.com)

Project Link: [https://github.com/yourusername/python-irc-client](https://github.com/yourusername/python-irc-client)

---

**Note**: IRC is a real-time chat protocol that has been around since 1988. While Discord and Slack have become more popular, IRC is still widely used in the open source community and offers a lightweight, decentralized alternative to modern chat platforms.
```

## .gitignore
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
*.log
chat_logs/
```

## LICENSE
```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## requirements.txt
```
# No external dependencies required
# This project uses only Python standard library modules:
# - tkinter (GUI)
# - socket (IRC connection)
# - threading (async message handling)

# Python 3.6+ required
