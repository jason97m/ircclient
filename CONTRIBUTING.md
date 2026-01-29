# Contributing to Python IRC Client

First off, thank you for considering contributing to Python IRC Client! It's people like you that make this project better.

## Code of Conduct

This project adheres to a simple principle: be respectful and considerate to others.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed and what you expected**
- **Include your Python version and operating system**
- **Include any error messages or stack traces**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Explain why this enhancement would be useful**
- **List any examples of where this enhancement exists in other tools**

### Pull Requests

1. Fork the repository
2. Create a new branch from `main`:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
6. Push to your fork:
   ```bash
   git push origin feature/my-new-feature
   ```
7. Submit a pull request

#### Pull Request Guidelines

- Keep pull requests focused on a single feature or bug fix
- Write clear, descriptive commit messages
- Update the README.md if you're adding new features
- Ensure the code follows the existing style
- Test your changes on multiple platforms if possible
- Add comments for complex code sections

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/python-irc-client.git
   cd python-irc-client
   ```

2. No dependencies to install! Just run:
   ```bash
   python3 irc_client.py
   ```

## Style Guidelines

### Python Style Guide

This project follows PEP 8 style guidelines:

- Use 4 spaces for indentation (no tabs)
- Limit lines to 100 characters
- Use descriptive variable names
- Add docstrings to functions and classes
- Keep functions focused and single-purpose

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters
- Reference issues and pull requests when relevant

Example:
```
Add SSL/TLS connection support

- Implement SSL socket wrapper
- Add SSL port option (6697)
- Update README with SSL instructions

Fixes #123
```

## Feature Ideas

Here are some areas where contributions would be especially valuable:

- **SSL/TLS Support**: Add encrypted connections
- **Multi-channel Tabs**: View multiple channels simultaneously
- **User List**: Display channel user lists
- **Logging**: Save chat history to files
- **Color Codes**: Parse and display IRC color codes
- **Notifications**: Desktop notifications for mentions
- **Configuration**: Save/load connection settings
- **Auto-reconnect**: Automatically reconnect on disconnect
- **DCC**: Direct Client-to-Client file transfers
- **SASL Authentication**: Add SASL auth support

## Testing

Before submitting a pull request, please test:

1. Connection to multiple IRC servers
2. Joining and leaving channels
3. Sending and receiving messages
4. All IRC commands you've modified
5. Error handling for edge cases
6. UI responsiveness

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
