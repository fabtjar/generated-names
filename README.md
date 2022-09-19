# Generated Names

An exercise from the book [The Pragmatic Programmer](https://www.amazon.co.uk/The-Pragmatic-Programmer-Andrew-Hunt/dp/020161622X). Write a script that generates a `names.h` and `names.c` with enums supplied from a file.

## Usage

```sh
python3 generate_names.py
clang main.c --include name.c -o generated_names
./generated_names
```