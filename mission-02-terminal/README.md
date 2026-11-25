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

| Command / Tool | Purpose |
|---|---|
| `pwd` | Displays the current working directory. |
| `ls` | Lists files and directories. |
| `ls -la` | Displays a detailed listing, including hidden files. |
| `cd` | Changes the current directory. |
| `mkdir` | Creates a new directory. |
| `touch` | Creates an empty file if it does not already exist. |
| `echo` | Displays text or sends it into a file. |
| `cp` | Creates a copy of a file. |
| `mv` | Moves or renames a file. |
| `cat` | Displays the contents of a file. |
| `ls -lah` | Displays detailed information, hidden files and human-readable sizes. |
| `head` | Displays the first few lines of input. |
| `\|` | Sends the output of one command to another command. |
| `brew --version` | Checks the installed Homebrew version, if available. |
| `brew list` | Displays packages managed by Homebrew, if available. |

## 4. My Understanding

The Terminal provides another way to interact with a computer without depending entirely on its graphical interface. Instead of navigating through windows and menus, I can perform operations by entering commands.

I understood that `pwd` helps identify where I am currently working, while `ls` allows me to inspect the contents of that location. The `cd` command is useful for moving between directories.

I also learned that file operations have different purposes. Copying a file creates another version while keeping the original intact, whereas moving or renaming a file changes its location or name.

One interesting thing I explored was the difference between `>` and `>>`. The first replaces the existing file contents, while the second appends additional text without removing what was already there.

Flags provide additional options to commands. For example, `ls -lah` displays hidden files, detailed file information and sizes in a more readable format.

The pipe symbol (`|`) connects commands by passing the output of one command as the input of another. For example, `ls -lah | head` displays only the first few lines of a detailed directory listing.

Finally, I learned that package managers such as Homebrew make software management easier by providing a central way to install, update and manage packages.

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

**GitHub status:** To be committed and pushed to the remote repository after completing the mission.

## 9. Final Reflection

This mission helped me become more comfortable using the command line for everyday file and directory operations.

I also realised that Terminal commands can be combined to perform tasks more efficiently. Understanding these basics should make it easier to work with development tools and manage projects in the future.
