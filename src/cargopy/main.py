#!/usr/bin/env python

from paintmystring.paint import paint
from help_panel import help_panel
import sys
import structure
import utils

def main():
    args = sys.argv[1:]

    new = False
    dir_name = None

    cd = False

    venv = False

    run = False
    file_name = None
    file_args = None

    pip = None
    package = None
    install = False
    upgrade = False
    uninstall = False
    listed = False


    while args:
        arg = args.pop(0)

        match arg:
            case "help" | "--help":
                help_panel()

            case "new":
                new = True
                try:
                    dir_name = args.pop(0)
                except IndexError:
                    paint(
                        paint("New").bright_red().bold(),
                        paint("action requires an argument...").bold(),
                    ).show()

            case "cd":
                cd = True

            case "venv":
                venv = True

            case "run":
                run = True
                try:
                    file_name = args.pop(0)
                except IndexError:
                    paint(
                        paint("Run").bright_red().bold(),
                        paint("action requires an argument...").bold(),
                    ).show()

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

            case "install":
                pip = True
                install = True
                try:
                    package = args.pop(0)
                except IndexError:
                    paint(
                        paint("Install").bright_red().bold(),
                        paint("action requires an argument...").bold(),
                    ).show()

            case "upgrade":
                pip = True
                upgrade = True
                try:
                    package = args.pop(0)
                except IndexError:
                    paint(
                        paint("Upgrade").bright_red().bold(),
                        paint("action requires an argument...").bold(),
                    ).show()

            case "uninstall":
                pip = True
                uninstall = True
                try:
                    package = args.pop(0)
                except IndexError:
                    paint(
                        paint("Uninstall").bright_red().bold(),
                        paint("action requires an argument...").bold(),
                    ).show()

            case "list":
                pip = True
                listed = True

            case _:
                paint("Unknown option...").bold().red().show()
                paint(
                    paint("Try:").bright_cyan().bold(),
                    paint("help").bright_yellow(),
                ).show()

    if new or cd:
        struct = structure.Structure()

        if new:
            if dir_name is None:
                sys.exit(1)

            struct.new(dir_name)

        elif cd:
            print(struct.cd())

    if venv or run or pip:
        project_utils = utils.Utils()

        if venv:
            project_utils.venv()

        elif run:
            if file_name is None:
                sys.exit(1)

            project_utils.run(file_name, file_args)

        elif pip:
            if package is None:
                sys.exit(1)

            if install:
                project_utils.pip(package, "install")

            elif upgrade:
                project_utils.pip(package, "upgrade")

            elif uninstall:
                project_utils.pip(package, "uninstall")

            elif listed:
                project_utils.pip("", "list")

if __name__ == "__main__":
    main()
