from pathlib import Path
from .project import Project
from paintmystring.paint import paint
import sys
import shutil
import subprocess

class Structure(Project):
    def __init__(self):
        self.pwd = Path.cwd()
        self.root_project = self.get_project_root()

    def new(self, dir_name: str):
        py_project = f"""[project]
name = "{dir_name}"
version = "0.1.0"
description = ""
readme = "README.md"
requires-python = ""

[project.scripts]
{dir_name} = "{dir_name}.main:main"

[project.urls]
Homepage = ""

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
        """

        main_py = """def main():
    print("Hello, world!")

if __name__ == "__main__": 
    main()
    """

        dir_path = self.pwd / dir_name

        if dir_path.exists():
            paint("Project already exists...").bright_magenta().bold().show()
            sys.exit(1)

        try:
            dir_path.mkdir(exist_ok=True)
        except Exception as e:
            paint(
                paint("Exception").bright_red().bold(),
                paint(e).bold(),
            ).show()

        (dir_path / "README.md").touch()
        (dir_path / "pyproject.toml").touch()
        with open(dir_path / "pyproject.toml", "w") as f:
            f.write(py_project)

        src_dir = dir_path / "src"
        tests_dir = dir_path / "tests"
        src_dir.mkdir()
        tests_dir.mkdir()

        package_dir = src_dir / dir_name
        package_dir.mkdir()
        (package_dir / "__init__.py").touch()
        (package_dir / "main.py").touch()
        with open(package_dir / "main.py", "w") as f:
            f.write(main_py)

        paint(
            paint("Created project in ->").bold(),
            paint(dir_name).bold().bright_blue(),
        ).show()

        if shutil.which("git") is not None:
            subprocess.run(
                "git init &>/dev/null",
                cwd=dir_path,
                shell=True,
            )

        else:
            paint(
                paint("Couldn't start git repository ->").bold(),
                paint("git is not on your path").bright_magenta(),
            ).show()

    def cd(self) -> Path:
        if self.root_project is None:
            paint("Not a Python project!").bright_magenta().bold().show()
            sys.exit(1)

        else:
            return self.root_project
