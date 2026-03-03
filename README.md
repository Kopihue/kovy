# Kovy 🚀

**Kovy** is a lightweight tool inspired by **Rust's cargo** to manage Python projects quickly and efficiently, from project creation to script execution and package management.

---

## 🛠️ Usage

### Available Options

| Option | Description |
|--------|-------------|
| `new <name>` | Creates a new project with the given name. |
| `cd` | Shows the root path of your project. |
| `venv --complete` | Initializes a virtual environment in your project. Use `--complete` to also automatically install twine and build. |
| `run -- parameters` | Runs the main script with optional parameters. |
| `install <package>` | Installs the specified Python package. |
| `upgrade <package>` | Updates the specified package. |
| `uninstall <package>` | Uninstalls the specified package. |
| `build` | Builds the distribution. |
| `upload` | Uploads your project to PyPi! |

---

## ⚡ Examples

```bash
# Create a project called "my_project"
kovy new my_project

# Initialize virtual environment
kovy venv

# Install requests
kovy install requests
```

# Enjoy using kovy!
