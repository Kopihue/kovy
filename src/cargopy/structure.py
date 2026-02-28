from pathlib import Path
import sys

class Structure:
    def __init__(self):
        self.pwd = Path.cwd()

    def new(self, dir_name: str):
        dir_path = self.pwd / dir_name

        dir_path.mkdir(exist_ok=True)
        (dir_path / "README.md").touch()
        (dir_path / "pyproject.toml").touch()

        src_dir = dir_path / "src"
        tests_dir = dir_path / "tests"
        src_dir.mkdir(exist_ok=True)
        tests_dir.mkdir(exist_ok=True)

        package_dir = src_dir / dir_name
        package_dir.mkdir(exist_ok=True)
        (package_dir / "__init__.py").touch()

    def cd(self):
        while True:
            if (self.pwd / "pyproject.toml").exists():
                print(self.pwd)
                break;

            elif self.pwd.parent == self.pwd:
                print("You haven't initialized a Python project")
                sys.exit(1)

            self.pwd = self.pwd.parent
