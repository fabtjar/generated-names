# Generated Names

An exercise from the book [The Pragmatic Programmer](https://www.amazon.co.uk/The-Pragmatic-Programmer-Andrew-Hunt/dp/020161622X).

Write a script that generates a `name.h` and `name.c` file with enums supplied from within the `names.txt` file.
This would be useful to be able to print out the state as a string (as opposed to a number) for debugging purposes.

## Usage

```sh
python3 generate_names.py
clang main.c --include name.c -o generated_names
./generated_names
```

## Files generates

```c
// name.h

#ifndef NAME_H
#define NAME_H

extern const char* NAME_names[];

typedef enum {
    state_ace,
    state_act,
    ...
    state_zap,
    state_zip,
} NAME;

#endif  // NAME_H
```

```c
// name.c

const char* NAME_names[] = {
    "state_ace",
    "state_act",
    ...
    "state_zap",
    "state_zip",
};
```