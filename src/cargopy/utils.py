from pathlib import Path
from structure import Structure
from project import Project
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
            print("Not a Python project")
            sys.exit(1)

        if check_venv:
            print(".venv already exists!")
            sys.exit(1)

        else:
            command = ["python", "-m", "venv", ".venv"]
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                cwd=self.root_project
            )

            if result.returncode != 0:
                print("The command has failed.")
                print(result.stderr)

            else:
                print("Succesfully created .venv!")

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
            print("Not a Python project")
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
                print(f"Didn't found script in {self.root_project}")
                sys.exit(1)

            command = [isolated_python, found_scripts[0], *file_args]
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
            )

            if result.returncode != 0:
                print(f"Exception running {file_name}")
                print(result.stderr)

    def pip(self, package: str, action: str):
        check_venv = self.check_venv_existence()
        isolated_python = self.get_isolated_python()

        if check_venv is None or isolated_python is None:
            print("Not a Python project")
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
