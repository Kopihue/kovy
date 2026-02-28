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
        if self.root_project is None:
            print("Didn't find the project to create a venv")
            sys.exit(1)

        if (self.root_project / ".venv").exists():
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
