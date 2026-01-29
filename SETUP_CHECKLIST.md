# GitHub Setup Checklist

Follow these steps to get your IRC client on GitHub from your desktop computer.

## ✅ Pre-requisites

- [ ] Git installed on your desktop computer
- [ ] GitHub account created
- [ ] All project files downloaded to your desktop

## 📋 Step-by-Step Process

### 1. Configure Git (First Time Only)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 2. Create GitHub Repository
- [ ] Go to https://github.com
- [ ] Click "+" → "New repository"
- [ ] Name: `python-irc-client` (or your choice)
- [ ] Visibility: Public or Private
- [ ] **DO NOT** check "Initialize with README"
- [ ] Click "Create repository"
- [ ] Copy the repository URL (e.g., `https://github.com/yourusername/python-irc-client.git`)

### 3. Initialize Local Repository
```bash
# Navigate to your project folder
cd /path/to/python-irc-client

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Python IRC chat client"
```

### 4. Push to GitHub
```bash
# Add GitHub as remote (replace with YOUR URL)
git remote add origin https://github.com/YOUR_USERNAME/python-irc-client.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

### 5. Verify
- [ ] Visit your GitHub repository URL
- [ ] Refresh the page
- [ ] Confirm all files are visible
- [ ] Check that README.md displays correctly

## 🔧 If You Need to Make Changes Later
```bash
# Make your changes to files
# Then:

git add .
git commit -m "Description of changes"
git push
```

## 📁 Project Files Included

- `irc_client.py` - Main application
- `README.md` - Project documentation
- `LICENSE` - MIT License
- `.gitignore` - Files to ignore
- `requirements.txt` - Dependencies (none needed)
- `CONTRIBUTING.md` - Contribution guidelines
- `GIT_SETUP_GUIDE.md` - Detailed Git setup instructions
- `QUICKSTART.md` - Quick start guide for users

## 🔑 Authentication Options

Choose one:

**Option A: Personal Access Token**
1. GitHub → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Select "repo" scope
4. Use token as password when pushing

**Option B: SSH Key**
1. Generate key: `ssh-keygen -t ed25519 -C "your.email@example.com"`
2. Add to GitHub: Settings → SSH and GPG keys
3. Change remote: `git remote set-url origin git@github.com:USERNAME/REPO.git`

## 🆘 Common Issues

**"Permission denied"**
→ Check authentication (token or SSH key)

**"Nickname already in use"**
→ This is IRC-related, not Git. Try a different IRC nickname.

**"fatal: not a git repository"**
→ Make sure you ran `git init` and you're in the right folder

**Files not showing on GitHub**
→ Make sure you ran `git add .` before committing

## 📚 Additional Resources

- Full setup guide: See `GIT_SETUP_GUIDE.md`
- Git documentation: https://git-scm.com/doc
- GitHub guides: https://guides.github.com

---

Good luck! If you get stuck, check the detailed guide in GIT_SETUP_GUIDE.md
