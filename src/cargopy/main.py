#!/home/kopihue/Python/cargopy/.venv/bin/python

import sys
import structure
import utils

args = sys.argv[1:]

new = False
dir_name = None

cd = False

venv = False

run = False
file_name = None
file_args = None

add = None
package = None


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
                print("New action requires an argument!")

        case "cd":
            cd = True

        case "venv":
            venv = True

        case "run":
            run = True
            try:
                file_name = args.pop(0)
            except IndexError:
                print("Run action requires an argument!")

            try:
                are_there_arguments = args.pop(0)
                if are_there_arguments == "--":
                    pass

                else:
                    raise ValueError("Invalid action")
            except IndexError:
                file_args = []
            else:
                file_args = args

        case "add":
            add = True
            try:
                package = args.pop(0)
            except IndexError:
                print("Add action requires an argument!")
                sys.exit(1)

        case _:
            print("Unknown option")

if new or cd:
    struct = structure.Structure()

    if new:
        if dir_name is None:
            sys.exit(1)

        struct.new(dir_name)

    elif cd:
        print(struct.cd())

if venv or run or add:
    utils = utils.Utils()

    if venv:
        utils.venv()

    elif run:
        if file_name is None:
            sys.exit(1)

        utils.run(file_name, file_args)

    elif add:
        print("add", package)
