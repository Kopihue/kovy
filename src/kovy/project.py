from pathlib import Path
from paintmystring.paint import paint
import sys

class Project:
    @staticmethod
    def get_project_root() -> Path | None:
        pwd = Path.cwd()

        while True:
            if pwd == pwd.parent:
                return None

            if (pwd / "pyproject.toml").exists():
                return pwd

            else:
                pwd = pwd.parent

    @staticmethod
    def check_venv_existence() -> bool | None:
        pwd = Project.get_project_root()
        if pwd is None:
            return None
        
        if (pwd / ".venv").exists():
            return True

        else:
            return False

    @staticmethod
    def get_isolated_python() -> Path | None:
        root_project = Project.get_project_root()

        if root_project is None:
            return None

        isolated_python = (
            root_project
            / ".venv" 
            / "bin" 
            / "python"
        )

        if not isolated_python.exists():
            paint("Virtual Python doesn't exists").bold().show()
            paint("Try running again \"kovy venv\"").bold().bright_yellow().show()
            sys.exit(1)

        return isolated_python
