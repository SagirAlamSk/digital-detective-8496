# Mission 4 — How Programs Run

## 1. Task / objective

The objective of this mission was to understand how programs execute on a computer. I had to create and run a basic Python program and learn the difference between a compiler and an interpreter.

## 2. Work completed

I created a Python file named `hello.py` containing a simple print statement.

I ran the program using Python 3 from the Terminal and verified that it displayed the expected message.

I also compared compilers and interpreters based on their execution process, output, examples and advantages.

### Task 4.1 — Program execution result

I executed the program using:

`python3 hello.py`

The Terminal displayed:

```text
Hello from Python
```

This confirmed that the Python file was saved and executed successfully.

### Task 4.2 — Compiler and Interpreter Comparison

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates source code before program execution. | Executes instructions during runtime. |
| Typical output | Often produces object code or an executable program. | Generally executes through the interpreter without producing a standalone native executable. |
| One example | GCC compiler used for C programs. | Python interpreter. |
| One advantage | Compiled output can execute efficiently without translating the entire source program each time. | Makes testing and running code convenient because instructions are handled during execution. |

### Explanation

A compiler translates source code into another form before the program runs, often producing machine code or an executable. An interpreter executes program instructions during runtime. Compiled programs can execute efficiently, while interpreters provide a convenient way to run and test code. Python uses an interpreter-based execution model, although its implementation also involves compiling source code into bytecode.

## 3. Commands / tools used

| Command / tool | Purpose |
|---|---|
| `python3 --version` | Checks the installed Python 3 version. |
| `cat` | Displays the contents of a file and was used to create the Python file. |
| `python3 hello.py` | Executes the Python program. |
| Terminal | Used to navigate the project and run the program. |
| Text editor | Used to work with the mission files. |

## 4. My understanding

I learned that a program is a set of instructions written to perform a particular task.

A compiler translates source code into another form before execution, often producing machine code or an executable. An interpreter executes instructions during runtime.

The main difference is when and how the translation and execution take place.

I also understood that Python uses an interpreter-based execution model. Running `python3 hello.py` tells the Python interpreter to execute the instructions written in the file.

This mission helped me understand how the code I write eventually becomes something the computer can execute.

## 5. Difficulties faced

No major difficulties. Creating the Python file and executing it through Terminal was straightforward.

## 6. How I resolved them

I checked the installed Python version before running the program. I then executed the file using the `python3` command and checked whether the expected output appeared.

## 7. Evidence / files

- `hello.py` — Contains the basic Python program that prints a message.
- This README — Contains the mission explanation and compiler/interpreter comparison.

## 8. Commit details

**Commit message:** `Compare compilers and interpreters`

The completed mission files were committed and pushed to the GitHub repository.
