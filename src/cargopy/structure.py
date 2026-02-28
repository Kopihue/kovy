from pathlib import Path
from project import Project
import sys
import shutil
import subprocess

class Structure(Project):
    def __init__(self):
        self.pwd = Path.cwd()
        self.root_project = self.get_project_root()

    def new(self, dir_name: str):
        dir_path = self.pwd / dir_name

        if dir_path.exists():
            print("Project already exists")
            sys.exit(1)

        try:
            dir_path.mkdir(exist_ok=True)
        except Exception as e:
            print("Exception", e)

        (dir_path / "README.md").touch()
        (dir_path / "pyproject.toml").touch()

        src_dir = dir_path / "src"
        tests_dir = dir_path / "tests"
        src_dir.mkdir()
        tests_dir.mkdir()

        package_dir = src_dir / dir_name
        package_dir.mkdir()
        (package_dir / "__init__.py").touch()

        print(f"Created project in {dir_name}")
        if shutil.which("git") is not None:
            subprocess.run(
                ["git", "init"],
                cwd=dir_path,
            )

        else:
            print("Couldn't create git repository, git doesn't exists")

    def cd(self) -> Path:
        if self.root_project is None:
            print("You haven't initialized a Python project!")
            sys.exit(1)

        else:
            return self.root_project
