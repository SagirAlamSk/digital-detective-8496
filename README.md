# The Digital Detective

### Diwali Independent Learning Assignment

Computers are part of almost everything we do, but most of the processes happening behind the screen usually go unnoticed.

This project explores those processes through a series of practical missions. It covers computer fundamentals, operating systems, command-line tools, programming, number systems, version control and networking.

This repository contains my work, observations and learning notes from the Digital Detective assignment.

## Mission Roadmap

The assignment is divided into nine missions, with each mission documented separately.

| Mission | Topic | Documentation |
|---|---|---|
| 00 | GitHub Repository Setup | [Mission 0](mission-00-setup/README.md) |
| 01 | Know Your Computer | [Mission 1](mission-01-computer-basics/README.md) |
| 02 | Become Comfortable with the Terminal | [Mission 2](mission-02-terminal/README.md) |
| 03 | Understand the Operating System | [Mission 3](mission-03-operating-system/README.md) |
| 04 | How Programs Run | [Mission 4](mission-04-programs/README.md) |
| 05 | Numbers and Data | [Mission 5](mission-05-numbers-data/README.md) |
| 06 | Git and GitHub | [Mission 6](mission-06-git-github/README.md) |
| 07 | How Computers Communicate | [Mission 7](mission-07-networking/README.md) |
| 08 | Final Report and Submission | [Mission 8](mission-08-final-report/README.md) |

## What I Explored

### Computer Fundamentals
I studied the relationship between hardware and software and explored how information moves through the Input, Processing, Output and Storage (IPOS) cycle.

### Terminal and Operating Systems
I practised navigating directories, creating and modifying files, using command options and pipes, and managing files through the command line. I also explored processes, storage, file permissions and other operating-system responsibilities.

### Programming and Data Representation
I compared compilers and interpreters, executed a simple Python program and explored decimal, binary and hexadecimal number systems. I also learned how character-encoding standards represent text.

### Git and GitHub
I practised staging and committing changes, maintaining branches, publishing remote changes and using Pull Requests to review and integrate updates.

### Computer Networking
I explored LAN, MAN, WAN, DNS, routers, communication protocols, packet switching and the client-server model. I also used Terminal commands to test connectivity and inspect DNS records.

## Python Number Converter

Mission 5 contains a small Python program that accepts a decimal number and displays its binary and hexadecimal representations.

To run it from the repository root:

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

The program uses Python's built-in `input()`, `int()`, `bin()` and `hex()` functions. It also checks for invalid input and negative numbers.

Some of the tested values include:

| Decimal | Binary | Hexadecimal |
|---:|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 42 | `0b101010` | `0x2a` |

## How the Repository Is Organised

Each mission has its own directory and README so that the activities and explanations remain easy to find.

The repository also contains:

- `mission-04-programs/hello.py` — A basic Python execution exercise.
- `mission-05-numbers-data/number_converter.py` — The number conversion program.
- `mission-02-terminal/terminal-practice/` — Files created during command-line practice.
- `evidence/` — A reserved directory for privacy-safe screenshots or selected outputs. It contains a `.gitkeep` placeholder.

## My Learning

Working through these missions helped me connect several computing concepts with things I use on my own computer.

I became more comfortable using Terminal instead of relying entirely on graphical interfaces. I also gained a better understanding of how operating systems manage resources and how programs are executed.

Building the number converter was particularly useful because it connected the mathematics of number systems with actual Python code.

The Git and GitHub mission helped me understand why developers use branches and Pull Requests instead of making every change directly on the main branch.

Finally, the networking exercises showed me that something as simple as opening a website involves several systems communicating with one another.

## Version Control and Progress

Git is used throughout this project to maintain a history of the work.

Each mission has its own dedicated commit, and its completed files are pushed to the public GitHub repository before proceeding to the next mission.

The project also includes a separate `update-about` branch and a Pull Request that was successfully merged into `main`.

## Repository Information

- **Repository:** `digital-detective-8496`
- **GitHub owner:** `SagirAlamSk`
- **Primary branch:** `main`
- **Visibility:** Public

This repository contains the documented work for the Digital Detective assignment, including practical exercises, explanations, supporting files and the final report.
