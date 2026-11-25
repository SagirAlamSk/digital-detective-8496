# Mission 3 — Understand the Operating System

## 1. Task / objective

The objective of this mission was to explore the operating system and understand how it manages processes, storage, files, paths, permissions and other computer resources.

I used macOS Terminal to collect system information and observe how the operating system handles running applications and files.

## 2. Work completed

I completed the following activities:

- Checked the operating system version and build information.
- Checked the currently active account without including personal account details in this report.
- Examined available and used storage space.
- Viewed a snapshot of running system processes.
- Identified the PID (Process ID) column in the process list.
- Navigated between the project directory and its subdirectories.
- Inspected the permissions of a practice text file.
- Studied the main responsibilities of an operating system.

### System information

| Information | Observation |
|---|---|
| Operating system | macOS |
| Version | 27.2 |
| Build | 26B123 |
| Current account | Checked (details omitted for privacy) |
| Available storage on `/` | 317 GiB |
| Storage capacity | 460 GiB |
| Filesystem usage | Approximately 4% |

### Process observation

I used the process listing command to view a snapshot of running processes.

Some processes observed included:

- `launchd`
- `logd`
- `UserEventAgent`
- `fseventsd`
- `systemstats`

The process list also displayed a PID column, which identifies individual running processes.

### Path navigation

I navigated between the main assignment directory and the `mission-02-terminal` directory.

I observed that:

- An absolute path identifies a location starting from the filesystem root.
- A relative path identifies a location based on the current working directory.

### File permissions

I inspected the permissions of:

`mission-02-terminal/terminal-practice/notes.txt`

The permission string was:

`-rw-r--r--`

This indicates that the owner has read and write permissions, while the group and other users have read-only permissions.

## 3. Commands / tools used

| Command | Purpose |
|---|---|
| `sw_vers` | Displays macOS version and build information. |
| `whoami` | Displays the currently active account name. |
| `df -h /` | Shows filesystem capacity and available storage in readable units. |
| `ps -axo pid,comm` | Displays running processes with their process IDs and command names. |
| `head -n 15` | Displays the first 15 lines of command output. |
| `pwd` | Displays the current working directory. |
| `cd` | Changes the current working directory. |
| `ls -l` | Displays files with detailed information, including permissions. |

## 4. My understanding

An operating system acts as the manager between computer hardware, software and the user.

I learned that processes are programs currently running on a computer. Each process has a Process ID (PID), which helps the operating system distinguish and manage individual processes.

Storage information helps us understand how much disk space is being used and how much remains available.

I also understood the difference between absolute and relative paths. Absolute paths describe a location from the filesystem root, whereas relative paths depend on the current directory.

File permissions control who can read, modify or execute files. The three basic permission types are read (r), write (w) and execute (x).

### Main responsibilities of an operating system

| Responsibility | My explanation | Example |
|---|---|---|
| Process management | Manages running programs and allocates CPU time to them. | Running a browser and a text editor simultaneously. |
| Memory management | Allocates and manages RAM for different applications. | Giving a browser memory while it is running. |
| Device management | Coordinates communication between hardware devices and software. | Managing a connected keyboard or printer. |
| File management | Organises files and directories and controls access to them. | Creating, saving and deleting documents. |
| User interface / shell | Provides a way for users to interact with the computer. | Using macOS desktop or Terminal. |
| Security and permissions | Controls access to files, accounts and system resources. | Restricting who can modify a particular file. |

## 5. Difficulties faced

No major difficulties were faced during the practical activities.

The main thing I needed to understand was how process information, filesystem paths and permission characters relate to the operating system.

## 6. How I resolved them

I used Terminal commands to inspect actual system information and compared the results with the concepts covered in the assignment.

This made it easier to understand how the operating system manages processes, storage and file access.

## 7. Evidence / files

- System information collected using `sw_vers`.
- Storage information collected using `df -h /`.
- Running process snapshot collected using `ps`.
- Directory navigation observations using `pwd` and `cd`.
- File permission information collected using `ls -l`.
- This README containing the observations and explanations.

Personal account information and identifying filesystem paths have intentionally been excluded.

## 8. Commit details

**Commit message:** `Document operating system and file management`

**GitHub status:** To be committed and pushed after completing this mission documentation.
