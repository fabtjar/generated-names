import datetime
import sys

HEADER_FILE_TEMPLATE = """// Generated with {file} {date}.

#ifndef NAME_H
#define NAME_H

extern const char* NAME_names[];

typedef enum {{
{enums}}} NAME;

#endif  // NAME_H
"""

C_FILE_TEMPLATE = """// Generated with {file} {date}.

const char* NAME_names[] = {{
{enums}}};
"""


def get_enums():
    with open("names.txt", "r") as f:
        return [e.strip() for e in f.readlines()[1:]]


def create_header_file(enums):
    with open("name.h", "w+") as f:
        f.writelines(
            HEADER_FILE_TEMPLATE.format(
                file=sys.argv[0],
                date=datetime.datetime.now(),
                enums="".join([f"    {e},\n" for e in enums]),
            )
        )


def create_c_file(enums):
    with open("name.c", "w+") as f:
        f.writelines(
            C_FILE_TEMPLATE.format(
                file=sys.argv[0],
                date=datetime.datetime.now(),
                enums="".join([f'    "{e}",\n' for e in enums]),
            )
        )


if __name__ == "__main__":
    enums = get_enums()
    create_header_file(enums)
    create_c_file(enums)
