from pathlib import Path
from structure import Structure
from project import Project
from paintmystring.paint import paint
import subprocess
import sys

class Utils(Project):
    def __init__(self):
        self.struct = Structure()

        self.pwd = Path.cwd()
        self.root_project = self.get_project_root()

    def venv(self):
        check_venv = self.check_venv_existence()
        if check_venv is None:
            paint("Not a Python project!").bright_magenta().bold().show()
            sys.exit(1)

        if check_venv:
            paint(
                paint(".venv").bright_cyan().bold(),
                paint("already exists!").bold(),
            ).show()
            sys.exit(1)

        else:
            command = ["python", "-m", "venv", ".venv"]
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                cwd=self.root_project
            )

            self.pip("pip", "upgrade")

            if result.returncode != 0:
                paint("The command has failed.").bold().show()
                print(result.stderr)

            else:
                paint(
                    paint("Succesfully created venv in ->").bold(),
                    paint(".venv").bright_cyan().bold(),
                ).show()

    def run(self, file_name: str, file_args: list[str] | None):
        check_venv = self.check_venv_existence()
        isolated_python = self.get_isolated_python()

        if file_args is None:
            sys.exit(1)

        if (
            check_venv is None 
            or self.root_project is None 
            or isolated_python is None
        ):
            paint("Not a Python project!").bright_magenta().bold().show()
            sys.exit(1)

        if not check_venv:
            self.venv()
            check_venv = True

        if check_venv:
            ignored_dirs = {".venv", "__pycache__"}
            found_scripts = []
            for path in self.root_project.rglob(file_name):
                if not any(
                    ignored in path.parts
                    for ignored in ignored_dirs
                ):
                    found_scripts.append(path.resolve())

            if not found_scripts:
                paint(
                    paint("Didn't find script in ->").bold(),
                    paint(file_name).blue(),
                ).show()
                sys.exit(1)

            command = [isolated_python, found_scripts[0], *file_args]
            subprocess.run(
                command,
            )

    def pip(self, package: str, action: str):
        check_venv = self.check_venv_existence()
        isolated_python = self.get_isolated_python()

        if check_venv is None or isolated_python is None:
            paint("Not a Python project!").bright_magenta().bold().show()
            sys.exit(1)

        if not check_venv:
            self.venv()
            check_venv = True

        if check_venv:
            if action == "upgrade":
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    package,
                ]

            elif action == "list":
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    action,
                ]

            elif action == "uninstall":
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    action,
                    "-y",
                    package
                ]

            else:
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    action,
                    package,
                ]

            subprocess.run(
                command,
            )
