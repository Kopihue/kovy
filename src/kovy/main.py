from paintmystring.paint import paint
from .help_panel import help_panel
from .structure import Structure
from .utils import Utils
import sys

def main():
    args = sys.argv[1:]

    new = False
    dir_name = None

    cd = False

    venv = False
    complete = False

    run = False
    file_args = None

    pip = None
    package = None
    install = False
    upgrade = False
    uninstall = False
    listed = False

    build = False
    upload = False

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
                try:
                    complete_flag = args.pop(0)
                except IndexError:
                    pass
                else:
                    if complete_flag == "--complete":
                        complete = True

                    else:
                        paint("Invalid flag").bright_red().bold().show()
                        paint(
                            paint("The only flag avaivable is ->").magenta().bold(),
                            paint("--complete").bold(),
                        ).show()
                        sys.exit(1)

            case "run":
                run = True
                try:
                    are_there_arguments = args.pop(0)
                    if are_there_arguments == "--":
                        pass

                    else:
                        paint(
                            paint("To pass arguments: ").bold(),
                            paint("Use -> --").magenta().bold(),
                            sep="\n",
                        ).show()
                        sys.exit(1)
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
                package = "list"

            case "build":
                pip = True
                build = True
                package = "build"

            case "upload":
                pip = True
                upload = True
                package = "upload"

            case _:
                paint("Unknown option...").bold().red().show()
                paint(
                    paint("Try:").bright_cyan().bold(),
                    paint("help").bright_yellow(),
                ).show()
                sys.exit(1)

    if new or cd:
        struct = Structure()

        if new:
            if dir_name is None:
                sys.exit(1)

            struct.new(dir_name)

        elif cd:
            print(struct.cd())

    elif venv or run or pip:
        project_utils = Utils()

        if venv:
            project_utils.venv(complete)

        elif run:
            project_utils.run(file_args)

        elif pip:
            if package is None:
                sys.exit(1)

            if install:
                project_utils.pip("install", package)

            elif upgrade:
                project_utils.pip("upgrade", package)

            elif uninstall:
                project_utils.pip("uninstall", package)

            elif listed:
                project_utils.pip("list")

            elif build:
                project_utils.pip("build")

            elif upload:
                project_utils.pip("upload")

    else:
        help_panel()

if __name__ == "__main__":
    main()
