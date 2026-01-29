# Git Setup and GitHub Upload Guide

This guide will help you set up a local Git repository on your desktop and push it to GitHub.

## Step 1: Install Git (if not already installed)

### Windows
Download and install from: https://git-scm.com/download/win

### macOS
```bash
brew install git
# or use Xcode Command Line Tools
xcode-select --install
```

### Linux
```bash
sudo apt-get install git  # Debian/Ubuntu
sudo yum install git      # RedHat/CentOS
```

## Step 2: Configure Git (First Time Setup)

Set your name and email (this will appear in your commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Create a GitHub Repository

1. Go to https://github.com and log in
2. Click the "+" icon in the top right, then "New repository"
3. Name your repository (e.g., `python-irc-client`)
4. Choose "Public" or "Private"
5. **DO NOT** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"
7. Keep this page open - you'll need the repository URL

## Step 4: Initialize Local Repository

Navigate to your project folder on your desktop:

```bash
# Example: if files are in C:\Users\Jason\Desktop\irc-client
cd /path/to/your/desktop/irc-client

# Initialize git repository
git init

# Add all files to staging
git add .

# Create first commit
git commit -m "Initial commit: Python IRC chat client"
```

## Step 5: Connect to GitHub and Push

Replace `YOUR_USERNAME` and `REPO_NAME` with your actual GitHub username and repository name:

```bash
# Add remote repository
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# Verify remote was added
git remote -v

# Push to GitHub (first time)
git push -u origin main
```

If you get an error about "master" vs "main" branch:
```bash
# Rename branch to main
git branch -M main
git push -u origin main
```

## Step 6: Verify Upload

1. Go to your GitHub repository page
2. Refresh the page
3. You should see all your files uploaded

## Future Updates

After making changes to your files:

```bash
# Check what changed
git status

# Add specific files
git add filename.py

# Or add all changed files
git add .

# Commit changes with a descriptive message
git commit -m "Add feature: description of what you changed"

# Push to GitHub
git push
```

## Common Git Commands

```bash
# View commit history
git log

# View current status
git status

# View differences
git diff

# Create a new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Pull latest changes from GitHub
git pull

# View all branches
git branch -a

# Delete a branch
git branch -d feature-name
```

## Authentication

GitHub may require authentication when pushing:

### Option 1: Personal Access Token (Recommended)
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select "repo" scope
4. Copy the token
5. Use it as your password when pushing

### Option 2: SSH Key
1. Generate SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your.email@example.com"
   ```
2. Add to SSH agent:
   ```bash
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```
3. Copy public key:
   ```bash
   cat ~/.ssh/id_ed25519.pub
   ```
4. Add to GitHub: Settings → SSH and GPG keys → New SSH key
5. Change remote URL to SSH:
   ```bash
   git remote set-url origin git@github.com:YOUR_USERNAME/REPO_NAME.git
   ```

## Troubleshooting

### "fatal: not a git repository"
Make sure you're in the correct directory and ran `git init`

### "Permission denied"
Check your authentication setup (token or SSH key)

### "rejected - non-fast-forward"
Someone else pushed changes. Pull first:
```bash
git pull --rebase origin main
git push
```

### "fatal: refusing to merge unrelated histories"
If you initialized the GitHub repo with files:
```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

## Best Practices

1. **Commit often**: Make small, focused commits
2. **Write clear messages**: Describe what and why, not how
3. **Pull before push**: Always pull latest changes before pushing
4. **Use branches**: Create feature branches for new work
5. **Test before commit**: Make sure code works before committing
6. **.gitignore**: Keep generated files out of version control

## Need Help?

- Git documentation: https://git-scm.com/doc
- GitHub guides: https://guides.github.com
- Git cheat sheet: https://education.github.com/git-cheat-sheet-education.pdf

---

Good luck with your project! 🚀
