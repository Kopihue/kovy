#!/usr/bin/env python

import sys
import structure

args = sys.argv[1:]
new = False
dir_name = None
cd = False
venv = False

while args:
    arg = args.pop(0)

    match arg:
        case "help" | "--help":
            print("Help panel deployed")

        case "new":
            new = True
            try:
                dir_name = args.pop(0)
            except IndexError:
                print("New requires a directory name")

        case "cd":
            cd = True

        case "venv":
            venv = True

        case _:
            print("Unknown option")

if new or cd:
    struct = structure.Structure()

    if new:
        if dir_name is None:
            sys.exit(1)

        struct.new(dir_name)

    if cd:
        struct.cd()

if venv:
    print("venv")
