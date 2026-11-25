# Mission 5 — Numbers and Data

## 1. Task / objective

The aim of this mission was to understand how computers represent numbers and text. I practised converting values between decimal, binary and hexadecimal, checked my calculations using Python, built a small number converter and explored basic character encoding.

## 2. Work completed

I completed all four activities in this mission.

- **Manual conversions:** Worked through seven decimal, binary and hexadecimal conversion problems, showing the calculation steps for each one.
- **Python verification:** Used Python's built-in conversion functions to check the manual answers and confirmed that the results matched.
- **Number converter:** Created `number_converter.py`, a program that accepts a decimal number and displays its binary and hexadecimal representations.
- **Program testing:** Tested the converter with 13, 25 and 42. I also included basic input validation for negative numbers and invalid input.
- **Text encoding:** Looked up the ASCII decimal values of uppercase A and lowercase a and learned why standards such as ASCII and UTF-8 are needed.

## 3. Commands / tools used

| Command / function | Purpose |
|---|---|
| `cd` | Navigate into the Mission 5 folder. |
| `mkdir -p` | Create the evidence directory if it does not already exist. |
| `cat` | Create and write the mission notes and Python program. |
| `python3` | Open the Python interactive environment and execute Python files. |
| `python3 -m py_compile` | Check the Python program for syntax errors. |
| `ls -la` | Inspect the files created in the mission folder. |
| `bin()` | Convert an integer into its binary representation. |
| `hex()` | Convert an integer into its hexadecimal representation. |
| `int()` | Convert a value into an integer, using a specified base when required. |
| `input()` | Accept a number entered by the user. |
| `print()` | Display the conversion results. |

## 4. My understanding

This mission helped me understand why computers use different number systems. Decimal is the system we normally use, but binary is especially important because computer data is represented using bits, which have values of 0 and 1. Hexadecimal provides a shorter way to write binary values.

I also understood that converting between number systems is not just about changing how a number looks. The value remains the same; only its representation changes.

Python made checking these conversions much easier. The `bin()` and `hex()` functions handle the conversion, while `int()` can interpret a number written in another base. I used these functions in my own converter so that the program could accept a decimal number and display both representations.

Another interesting part was text encoding. Characters need numerical representations before computers can store and process them. ASCII covers a basic set of characters, whereas UTF-8 supports a much wider range of writing systems and symbols.

## 5. Difficulties faced

Understanding the remainders in decimal-to-binary conversion took a little practice, particularly remembering to read them from bottom to top.

I also had to understand the prefixes in Python's output. For example, `0b` identifies a binary value and `0x` identifies a hexadecimal value. These prefixes initially looked like part of the number itself.

## 6. How I resolved them

I worked through the division steps individually and checked the final results using Python. Comparing the manual answers with the built-in conversion functions helped me understand where each result came from.

I also tested the converter with multiple values instead of relying on a single successful run. This helped confirm that the program was producing the expected output.

## 7. Evidence / files

The following files contain the work completed for this mission:

| File | Contents |
|---|---|
| `calculations.md` | Manual number conversions with working. |
| `python-verification.md` | Python expressions and verification results. |
| `number_converter.py` | Working decimal-to-binary and decimal-to-hexadecimal converter. |
| `converter-tests.md` | Three test values and their expected outputs. |
| `text-encoding.md` | ASCII values and text-encoding explanation. |

## 8. Commit details

**Commit message:** `Build number converter and practise data representation`

The completed Mission 5 files were staged, committed and pushed to the GitHub repository on the `main` branch.
