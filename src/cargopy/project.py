from pathlib import Path

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
