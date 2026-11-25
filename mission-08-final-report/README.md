# Mission 8 — Final Report and Submission

## 1. Task / objective

The objective of this mission was to review the complete Digital Detective assignment, check that all mission folders and required files were present, improve the root README, and prepare the public GitHub repository for submission.

This final stage brings together the work completed throughout the eight previous missions and provides an overview of the concepts and practical activities covered.

## 2. Work completed

### Step 1 — Review the repository structure

Reviewed the repository and checked that all nine mission directories were present.

The repository contains the following structure:

| Folder / file | Contents |
|---|---|
| `README.md` | Main project introduction, mission roadmap and learning summary. |
| `evidence/` | Reserved for supporting screenshots and selected outputs; contains `.gitkeep`. |
| `mission-00-setup/` | Repository setup documentation. |
| `mission-01-computer-basics/` | IPOS, hardware, software and computer-based systems. |
| `mission-02-terminal/` | Terminal exercises and file-management practice. |
| `mission-03-operating-system/` | Operating-system information, processes, paths and permissions. |
| `mission-04-programs/` | Python execution exercise and compiler/interpreter comparison. |
| `mission-04-programs/hello.py` | Simple Python program. |
| `mission-05-numbers-data/` | Number conversions, Python verification and encoding notes. |
| `mission-05-numbers-data/number_converter.py` | Decimal-to-binary and hexadecimal converter. |
| `mission-06-git-github/` | Git workflow, branch and Pull Request documentation. |
| `mission-07-networking/` | Networking concepts and connectivity observations. |
| `mission-08-final-report/` | Final repository review and submission report. |

Each mission has a separate README containing its relevant documentation.

The additional `evidence/` directory is preserved using `.gitkeep`, which allows Git to track the directory even when it contains no other files.

### Step 2 — Review the completed missions

The following table records the progress of the assignment.

| Mission | Topic | Status |
|---|---|---|
| 0 | GitHub Repository Setup | Completed |
| 1 | Know Your Computer | Completed |
| 2 | Become Comfortable with the Terminal | Completed |
| 3 | Understand the Operating System | Completed |
| 4 | How Programs Run | Completed |
| 5 | Numbers and Data | Completed |
| 6 | Git and GitHub | Completed — Pull Request merged |
| 7 | How Computers Communicate | Completed |
| 8 | Final Report and Submission | Documentation prepared; final checks recorded |

### Step 3 — Review the practical files

The repository contains practical work from several missions.

**Mission 2 — Terminal practice**

The `terminal-practice/` directory contains:

- `notes.txt`
- `backup-notes.txt`

These files were used to practise writing, appending, copying and renaming text files.

**Mission 4 — Python execution**

The `hello.py` program contains a simple Python print statement and was used to practise executing a Python file from Terminal.

**Mission 5 — Number conversion**

The `number_converter.py` program accepts a decimal number and displays its binary and hexadecimal representations.

It was tested using the values 13, 25 and 42.

The recorded results were:

| Decimal | Binary | Hexadecimal |
|---:|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 42 | `0b101010` | `0x2a` |

The mission also contains separate files for manual calculations, Python verification, converter tests and text encoding.

**Mission 7 — Network observations**

Network connectivity and DNS resolution were tested using macOS Terminal.

The `ping -c 4 example.com` command returned four successful replies with 0% packet loss.

The observed average round-trip time was 17.595 milliseconds.

The `nslookup` and `dig` commands also returned DNS information for the example domain, with two IPv4 A records in the observed responses.

### Step 4 — Review Git and GitHub activity

Git was used throughout the assignment to maintain separate commits for completed missions.

A feature branch named `update-about` was created to modify the root README.

Pull Request #1 was opened from `update-about` into `main`, reviewed and successfully merged.

The resulting merge commit is visible in the repository history.

The repository also preserves a separate commit for the evidence directory.

### Step 5 — Update the root README

The root README was revised to provide a clearer introduction to the assignment.

It includes:

- A description of the project.
- Direct links to all nine mission READMEs.
- A summary of the topics explored.
- Instructions for executing the Python number converter.
- A summary of the learning gained throughout the missions.
- Information about the repository structure and Git workflow.

### Step 6 — Final repository review

During the final review, I identified and addressed some repository housekeeping items.

The generated Python `__pycache__` directory was removed from the tracked project files, and `.gitignore` was updated with rules to exclude generated Python bytecode and macOS metadata files.

The generated Python cache files were removed from Git tracking, and `.gitignore` was updated to exclude Python bytecode and macOS metadata files.

A few earlier README details also require a final consistency check, particularly the recorded Python and Git versions in Mission 0 and the completed push status in the earlier mission reports.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `git status` | Checks the state of the working directory and staging area. |
| `git log --oneline --decorate --all` | Reviews commits, branches and repository history. |
| `git branch -a` | Displays local and remote branches. |
| `git ls-files` | Lists files tracked by Git. |
| `git diff --check` | Checks changes for whitespace problems. |
| `git rm -r` | Removes generated files from Git tracking. |
| `cat` | Creates or displays text and Markdown files. |
| `python3` | Runs Python programs and conversion exercises. |
| `ping` | Tests network connectivity. |
| `nslookup` | Performs DNS lookups. |
| `dig` | Displays detailed DNS query information. |
| GitHub CLI (`gh`) | Used to manage and inspect the Pull Request. |
| GitHub | Hosts the public repository and its commit history. |

## 4. My understanding

Completing this assignment gave me a better understanding of how different areas of computing connect with one another.

I started with computer fundamentals and the IPOS model, which helped explain how a computer receives information, processes it, produces output and stores results.

The Terminal exercises showed me how files and directories can be managed using commands rather than graphical interfaces. I also learned that command flags and pipes can make command-line operations more flexible.

Exploring the operating system helped me understand how processes, memory, storage, devices and permissions are managed.

The Python exercises introduced me to program execution and number representation. Building the number converter was particularly useful because I could apply the conversion concepts directly in code and compare the results against manual calculations.

The Git and GitHub activities showed me how version control helps organise development. Branches and Pull Requests also provided a practical example of how changes can be reviewed before being integrated into a main project.

Finally, the networking mission helped explain how devices communicate through DNS, routers and protocols. The connectivity and DNS tests made these concepts easier to understand.

Overall, the assignment connected theoretical concepts with practical activities performed on my own computer.

## 5. Difficulties faced

Some parts of the assignment required additional attention:

- Understanding the difference between staging and committing changes.
- Managing local and remote branches during the Pull Request exercise.
- Learning the binary and hexadecimal conversion process.
- Understanding the information returned by DNS lookup tools.
- Keeping generated files and unnecessary information out of the public repository.

## 6. How I resolved them

I worked through the Git operations separately and checked repository status and commit history after important changes.

For number conversions, I compared manual calculations with Python's built-in functions.

For networking, I compared the results of `ping`, `nslookup` and `dig` to understand what each command revealed.

During the final repository review, I also removed generated Python cache files and added appropriate `.gitignore` rules.

## 7. Evidence / files

The repository contains the following supporting material:

- Root `README.md` — Project introduction, mission navigation and learning summary.
- `mission-00-setup/README.md` — Repository setup details.
- `mission-01-computer-basics/README.md` — IPOS and computer-system explanations.
- `mission-02-terminal/README.md` — Terminal command reference and observations.
- `mission-02-terminal/terminal-practice/` — Text files from file-management exercises.
- `mission-03-operating-system/README.md` — Operating-system observations.
- `mission-04-programs/hello.py` — Python execution exercise.
- `mission-05-numbers-data/number_converter.py` — Working number converter.
- `mission-05-numbers-data/calculations.md` — Manual number conversions.
- `mission-05-numbers-data/python-verification.md` — Python conversion results.
- `mission-05-numbers-data/converter-tests.md` — Converter test cases.
- `mission-05-numbers-data/text-encoding.md` — ASCII and UTF-8 notes.
- `mission-06-git-github/README.md` — Git and GitHub documentation.
- `mission-07-networking/README.md` — Networking explanations and observations.
- `evidence/.gitkeep` — Preserves the evidence directory in the repository.

**GitHub repository:** https://github.com/SagirAlamSk/digital-detective-8496

**Pull Request #1:** https://github.com/SagirAlamSk/digital-detective-8496/pull/1

## 8. Commit details

**Mission 8 commit message:** `Complete final report and verify assignment submission`

The final report and root README are prepared for the final commit.

The final push and repository verification are completed after committing these updates.
