# Mission 6 — Git and GitHub

## 1. Task / objective

The objective of this mission was to understand version control and practise using Git and GitHub. I explored the basic Git workflow, created a separate branch, updated the project README and opened a Pull Request.

## 2. Work completed

I practised checking repository status, staging files, creating commits and viewing commit history.

I created a branch named `update-about` and added a section called "My Learning" to the main project README. The update describes some of the concepts and skills I gained while completing the previous missions.

After committing and pushing the branch, I opened a Pull Request on GitHub to propose merging the changes into `main`.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `git status` | Checks the current state of the repository. |
| `git add` | Stages selected file changes. |
| `git commit` | Records staged changes in Git history. |
| `git log --oneline` | Displays a compact commit history. |
| `git diff` | Shows changes made to files. |
| `git diff --cached --check` | Checks staged changes for whitespace problems. |
| `git switch -c` | Creates a new branch and switches to it. |
| `git branch` | Lists available local branches. |
| `git push -u origin` | Publishes a branch to GitHub and sets its upstream. |
| `git pull --ff-only origin main` | Retrieves remote changes without creating a merge commit. |
| GitHub | Used to create and review a Pull Request. |

## 4. My understanding

Git is a version control system that helps track changes made to files over time. It allows developers to maintain a history of their work and return to earlier versions when necessary.

Staging and committing are two different steps. Staging selects the changes that should be included in the next commit, while committing permanently records those selected changes in the local Git history.

A branch is an independent line of development. It allows changes to be made without directly modifying the main branch.

A Pull Request is a way to propose changes from one branch to another on GitHub. It allows the changes to be reviewed before they become part of the main project.

I understood that branches and Pull Requests make collaboration safer because changes can be checked before being included in the main project.

## 5. Difficulties faced

The main thing that required attention was understanding how local branches and remote branches are connected. It was also important to select the correct source and destination branches while creating the Pull Request.

## 6. How I resolved them

I checked the active branch using `git branch` and verified the repository status before committing. I used the GitHub Pull Request interface to compare `update-about` with `main`.

## 7. Evidence / files

- Updated root `README.md`.
- Git command practice and commit history.
- `update-about` branch.
- GitHub Pull Request.
- This Mission 6 README.

## 8. Commit details

**Commit message:** Complete Git and GitHub collaboration mission

**Branch:** main

**Push status:** Complete

**Pull Request status:** Merged
