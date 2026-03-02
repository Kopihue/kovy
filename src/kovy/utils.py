from .structure import Structure
from .project import Project
from paintmystring.paint import paint
from pathlib import Path
import subprocess
import sys
import shutil
import tomllib

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

    def run(self, file_args: list[str] | None):
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
            py_project = self.root_project / "pyproject.toml"
            if not py_project.exists():
                paint("Your pyproject doesn't exists...").red().bold().show()
                sys.exit(1)

            with open(py_project, "rb") as f:
                data = tomllib.load(f)

            print(data)

    def pip(self, action: str, package: str | None = None):
        check_venv = self.check_venv_existence()
        isolated_python = self.get_isolated_python()

        if (
            check_venv is None 
            or isolated_python is None 
            or self.root_project is None
        ):
            paint("Not a Python project!").bright_magenta().bold().show()
            sys.exit(1)

        if not check_venv:
            self.venv()
            check_venv = True

        if check_venv:
            if action == "install" and package is not None:
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    action,
                    package,
                ]

            elif action == "upgrade" and package is not None:
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    "install",
                    "--upgrade",
                    package,
                ]

            elif action == "uninstall" and package is not None:
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    action,
                    "-y",
                    package
                ]

            elif action == "list":
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    action,
                ]

            elif action == "build":
                dist_directory = self.root_project / "dist"
                if (dist_directory).exists():
                    paint(
                        paint("Directory \"dist\" detected.").yellow().bold(),
                        paint("Deleting it.").bright_red().bold()
                    ).show()

                    try:
                        shutil.rmtree(dist_directory)
                    except Exception as e:
                        paint(
                            paint("Error, ").bold().red(),
                            paint(e),
                        ).show()

                command = [
                    isolated_python,
                    "-m",
                    action,
                ]

                paint("Creating \"dist\" directory...").green().bold().show()

                result = subprocess.run(
                    command,
                    cwd=self.root_project,
                    capture_output=True,
                    text=True,
                )

                if result.returncode == 0:
                    paint("All good.").blue().bold().show()

                else:
                    paint("There was an exception...").red().bold().show()
                    print("\n", result.stderr)

                sys.exit(0)

            elif action == "upload":
                print("Upload")

                sys.exit(0)

            else:
                paint("Not a pip command!").bright_magenta().bold().show()
                sys.exit(1)


            subprocess.run(
                command,
            )
