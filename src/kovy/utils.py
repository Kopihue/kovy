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

    def venv(self, complete: bool):
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

            if complete:
                self.pip("upgrade", "pip")
                self.pip("install", "build")
                self.pip("install", "twine")
                self.pip("editable")

            else:
                self.pip("upgrade", "pip")
                self.pip("editable")


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
            self.venv(False)
            check_venv = True

        if check_venv:
            py_project = self.root_project / "pyproject.toml"
            if not py_project.exists():
                paint("Your pyproject doesn't exist...").red().bold().show()
                sys.exit(1)

            with open(py_project, "rb") as f:
                data = tomllib.load(f)

            try:
                script: dict = data["project"]["scripts"]
            except KeyError:
                paint("No block \"scripts\" in your pyproject").bold().show()
                paint(
                    paint("[+]").bright_green(),
                    paint("Add [project.scripts] to your pyproject").blue().bold(),
                ).show()
                sys.exit(1)

            entry_point = script.items()
            _, entry_point = list(entry_point)[0]

            module, _ = entry_point.split(":")

            command = [
                isolated_python,
                "-m",
                module,
            ]

            for arg in file_args:
                command.append(arg)

            print("command to execute ->", command)

            subprocess.run(
                command,
            )

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
            self.venv(False)
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

            elif action == "editable":
                command = [
                    isolated_python,
                    "-m",
                    "pip",
                    "install",
                    "-e",
                    ".",
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
                dist_path = self.root_project / "dist"
                if not dist_path.exists():
                    paint(
                        paint("Dist doesn't exist...").bold(),
                    ).show()
                    self.pip("build")

                command = [
                    isolated_python,
                    "-m",
                    "twine",
                    "upload",
                    "dist/*",
                ]

                paint("Executing upload...").bright_magenta().bold().show()

                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                    cwd=self.root_project
                )

                if result.returncode != 0:
                    paint("Error:").bright_red().bold().show()
                    print(result.stdout)

                else:
                    paint("all good.").blue().bold().show()

                sys.exit(0)

            else:
                paint("Not a pip command!").bright_magenta().bold().show()
                sys.exit(1)


            subprocess.run(
                command,
            )
