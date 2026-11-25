# Mission 0 — GitHub Repository Setup

## 1. Task / objective

The purpose of this mission was to establish a workspace for the Digital Detective assignment and publish it as a public GitHub repository.

This involved preparing the required directory structure, checking the development tools, configuring Git and connecting the local project to GitHub.

**Repository name:** `digital-detective-8496`

## 2. Work completed

- Prepared a local project directory using the required repository naming convention.
- Created separate directories for Missions 0 through 8.
- Added an individual README file to each mission directory.
- Prepared the main README containing the project introduction and mission navigation.
- Created an `evidence/` directory for collecting relevant screenshots and outputs.
- Added the initial Python converter file to the appropriate mission directory.
- Checked the installed versions of Python and Git.
- Verified GitHub CLI authentication.
- Initialised the project as a Git repository and configured the default branch as `main`.
- Published the repository on GitHub using the command-line interface.

## 3. Commands / tools used

| Command / Tool | Purpose |
|---|---|
| `python3 --version` | Displays the installed Python 3 version. |
| `git --version` | Displays the installed Git version. |
| `gh auth status` | Checks the authenticated GitHub account and CLI login status. |
| `git init` | Converts the project directory into a local Git repository. |
| `git status` | Displays the current branch and the state of tracked and untracked files. |
| `gh repo create --public --source=. --remote=origin` | Creates a public GitHub repository from the current directory and adds its remote connection as `origin`. |

**Verified tool versions:** Python 3.14.7 and Git 2.55.0.

**How the repository was published:**

Rather than creating the repository manually through the GitHub website, GitHub CLI was used:

```bash
gh repo create --public --source=. --remote=origin
```

The command creates the online repository using the existing local project directory and establishes the remote connection.

## 4. My understanding

A repository is a location where project files and their version history are maintained. Git keeps track of changes, making it possible to inspect previous versions and manage project development.

GitHub hosts Git repositories online, making them accessible from different computers and allowing collaboration with other developers.

Keeping each mission in a separate directory helps organise the assignment. It also makes documentation easier because each folder contains information specific to its corresponding mission.

Using GitHub CLI also makes repository creation more convenient because it can be performed directly from the Terminal without manually navigating through the website.

## 5. Difficulties faced

- Git commands initially failed because the project directory had not yet been initialised as a repository.
- The Git author configuration function could not be used before repository initialisation.
- The default initial branch needed to be configured as `main`.

## 6. How I resolved them

- Initialised the project using `git init`.
- Configured the default branch name using `git config --global init.defaultBranch main`.
- Reinitialised the repository after applying the branch configuration.
- Configured the appropriate Git author profile after initialisation.
- Used GitHub CLI to create and connect the public repository.

## 7. Evidence / files

The following files and directories were prepared:

```text
digital-detective-8496/
├── evidence/
├── mission-00-setup/
│   └── README.md
├── mission-01-computer-basics/
│   └── README.md
├── mission-02-terminal/
│   └── README.md
├── mission-03-operating-system/
│   └── README.md
├── mission-04-programs/
│   └── README.md
├── mission-05-numbers-data/
│   ├── number_converter.py
│   └── README.md
├── mission-06-git-github/
│   └── README.md
├── mission-07-networking/
│   └── README.md
├── mission-08-final-report/
│   └── README.md
└── README.md
```

**Tools used:**
- Python 3
- Git
- GitHub CLI

## 8. Commit details

**Commit message:** `Set up Digital Detective mission structure`

**Push status:** Successfully committed and pushed to GitHub.
