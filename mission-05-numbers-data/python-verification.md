# Task 5.2 — Python Verification

I used Python's built-in conversion functions to check my manual calculations.

| Expression | Result | Manual calculation |
|---|---|---|
| bin(13) | 0b1101 | 1101 |
| bin(25) | 0b11001 | 11001 |
| int("1010", 2) | 10 | 10 |
| int("1101", 2) | 13 | 13 |
| hex(13) | 0xd | 13 in decimal |
| hex(31) | 0x1f | 1F |
| int("A", 16) | 10 | 10 |
| int("1F", 16) | 31 | 31 |
| hex(int("1111", 2)) | 0xf | F |

The Python results matched the manual calculations. Python adds prefixes to indicate the number system being displayed.
