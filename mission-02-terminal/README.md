# Mission 2 — Become Comfortable with the Terminal

## 1. Task / Objective

The objective of this mission was to become familiar with the Terminal and understand how command-line instructions can be used to navigate directories, create and manage files, and inspect information.

I also explored command options (flags), pipes and the purpose of package managers.

## 2. Work Completed

During this mission, I practised several basic Terminal operations within my assignment repository.

The activities included:

- Checking my current working directory and listing its contents.
- Navigating between directories using relative paths.
- Creating directories and empty files.
- Copying and renaming files.
- Displaying file contents directly through Terminal.
- Adding new text to an existing file without removing its previous contents.
- Comparing normal and detailed directory listings.
- Using flags to display hidden files and file sizes.
- Combining commands using pipes.
- Exploring the purpose of Homebrew as a package manager on macOS.

I also created a `terminal-practice` directory to keep the file-management exercises separate from the other assignment files.

## 3. Commands / Tools Used

| Operation / command name | What it does | What I observed |
|---|---|---|
| `pwd` | Displays the absolute path of the current directory. | Displayed the location of the assignment repository. |
| `ls` | Lists files and directories in the current location. | Displayed the README, evidence folder and mission directories. |
| `ls -la` | Displays detailed information, including hidden files. | Showed entries such as `.git` and `.gitignore` along with file permissions and sizes. |
| `cd ..` | Moves to the parent directory. | Moved from the project directory to its parent directory. |
| `cd -` | Returns to the previous working directory. | Brought me back to the project directory. |
| `mkdir -p` | Creates a directory and any missing parent directories. | Created `mission-02-terminal/terminal-practice`. |
| `touch` | Creates an empty file if it does not exist. | Created `notes.txt` inside the practice directory. |
| `echo` with `>` | Writes text into a file, replacing existing contents. | Created the first line in `notes.txt`. |
| `echo` with `>>` | Adds text to the end of an existing file. | Added a second line without removing the first. |
| `cp` | Creates a copy of a file. | Created `notes-backup.txt` from `notes.txt`. |
| `mv` | Moves or renames a file. | Renamed `notes-backup.txt` to `backup-notes.txt`. |
| `cat` | Displays file contents. | Displayed both lines stored in `notes.txt`. |
| `ls -l` | Displays detailed file information. | Showed permissions, file size and modification information. |
| `ls -lah` | Includes hidden entries and displays file sizes in human-readable form. | Displayed both practice files with sizes of 64B each. |
| `ls -lah \| head` | Passes the listing to `head`, which displays only its first few lines. | Displayed the beginning of the directory listing. |
| `brew --version` | Displays the installed Homebrew version. | Reported Homebrew 7.0.16. |
| `brew list` | Displays installed packages managed by Homebrew. | Displayed the installed Formulae on the computer. |

### Answers to Task 2.2

**1. What is the difference between replacing a file's contents and adding text to the end?**

The `>` operator replaces the existing contents of a file, whereas `>>` appends new text without removing what was already present. I used both operators while creating the two-line `notes.txt` file.

**2. What is the difference between copying a file and moving a file?**

Copying creates another version while leaving the original unchanged. Moving transfers the file to another location or renames it. I practised this using `cp` and `mv`.

**3. What information does the current-directory display provide?**

The `pwd` command tells me the exact directory in which Terminal is currently operating. This is useful for checking my location before executing file operations.

**4. Why is a directory-listing operation useful?**

A directory listing helps identify the files and folders available at a particular location. Detailed options also provide information such as permissions and file sizes.

## 4. My Understanding

The Terminal provides another way to interact with a computer without depending entirely on its graphical interface. Instead of navigating through windows and menus, I can perform operations by entering commands.

I understood that `pwd` helps identify where I am currently working, while `ls` allows me to inspect the contents of that location. The `cd` command is useful for moving between directories.

I also learned that file operations have different purposes. Copying a file creates another version while keeping the original intact, whereas moving or renaming a file changes its location or name.

One interesting thing I explored was the difference between `>` and `>>`. The first replaces the existing file contents, while the second appends additional text without removing what was already there.

Flags provide additional options to commands. For example, `ls -lah` displays hidden files, detailed file information and sizes in a more readable format.

The pipe symbol (`|`) connects commands by passing the output of one command as the input of another. For example, `ls -lah | head` displays only the first few lines of a detailed directory listing.

Finally, I learned that package managers such as Homebrew make software management easier by providing a central way to install, update and manage packages.

### Understanding Package Managers

Homebrew is a package manager for macOS. It provides a convenient way to install, update and manage software through Terminal instead of downloading and configuring every application manually.

The `brew list` command displays packages managed by Homebrew, making it easier to see which tools are already installed.

My installed Homebrew version was **7.0.16**.

## 5. Difficulties Faced

Initially, remembering the different Terminal commands and understanding how their options affect the output required some practice.

I also needed to understand the difference between appending text to a file and replacing its existing contents.

## 6. How I Resolved Them

I practised each operation separately and checked the results using commands such as `ls` and `cat`.

Comparing the output before and after using different flags helped me understand how command options work.

I also tested file-copying, renaming and text-appending operations inside the dedicated practice directory to avoid affecting other assignment files.

## 7. Evidence / Files

The following files and directories were created or updated during this mission:

- `README.md` — Mission documentation and learning summary.
- `terminal-practice/notes.txt` — Text file used to practise writing and appending content.
- `terminal-practice/backup-notes.txt` — Backup copy created and renamed during the exercise.

## 8. Commit Details

**Commit message:** `Complete Terminal and file management mission`

**GitHub status:** Successfully committed and pushed to GitHub.

## 9. Final Reflection

This mission helped me become more comfortable using the command line for everyday file and directory operations.

I also realised that Terminal commands can be combined to perform tasks more efficiently. Understanding these basics should make it easier to work with development tools and manage projects in the future.
