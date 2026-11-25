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
| Current account | Checked; account name omitted for privacy. |
| Total filesystem capacity | 460 GiB |
| Used storage | 13 GiB |
| Available storage | 317 GiB |
| Filesystem usage | 4% |

The storage information was collected using `df -h /`. It showed that approximately 317 GiB was available on the root filesystem at the time of inspection.

### Process observation

I used `ps -axo pid,comm | head -n 15` to inspect a snapshot of running processes.

Some of the processes displayed were:

| PID | Process | Role |
|---:|---|---|
| 1 | `launchd` | System process responsible for starting and managing services. |
| 100 | `logd` | Background service responsible for system logging. |
| 103 | `UserEventAgent` | Background system process handling user-related events. |
| 105 | `fseventsd` | Monitors filesystem events. |
| 110 | `systemstats` | Collects system activity statistics. |

A process is an instance of a program currently running on the computer. The PID (Process ID) is the numeric identifier assigned to each process, helping the operating system distinguish between them.

The command displayed the PID column alongside the process names, allowing me to identify individual background processes.

### Path navigation

I navigated between the project directory and its Mission 2 subdirectory using `pwd` and `cd`.

**Absolute path example:**

`/Users/[redacted]/Coding/Projects/digital-detective-8496`

An absolute path starts from the filesystem root and identifies a location independently of the current working directory.

**Relative path example:**

`mission-02-terminal`

From the root of my assignment repository, this relative path refers to the Mission 2 directory.

I also used `cd ..` to return to the parent directory. This demonstrated how relative navigation depends on the current location.

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

**GitHub status:** Successfully committed and pushed to GitHub.
