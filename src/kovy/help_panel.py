import os
import time
from paintmystring.paint import paint

def clear(lazy: float):
    time.sleep(lazy)
    os.system("clear")

def help_panel():
    clear(0)

    paint(
        paint("*"),
        paint("Help panel deployed").bright_yellow().bold(),
        paint("*"),
    ).show()

    paint("*" * 23).show()
    print()
    
    paint(
        paint("Usage:"),
        paint("kovy").bright_red().bold(),
        paint("<option>").bright_green().bold(),
        paint("<parameter>").bright_blue().bold(),
    ).show()
    print()

    paint("Options: ").bright_green().bold().show()
    paint(
        paint("\tnew <parameter> ->").bright_magenta(),
        paint("Creates a new project named as <parameter>").bold()
    ).show()

    paint(
        paint("\tcd ->").bright_magenta(),
        paint("Prints the path of the root of your project").bold()
    ).show()

    paint(
        paint("\tvenv ->").bright_magenta(),
        paint("Initializes a virtual env in your project").bold()
    ).show()

    paint(
        paint("\trun <parameter> ->").bright_magenta(),
        paint("Runs the script named <parameter> just if it exists").bold()
    ).show()

    paint(
        paint("\tinstall <parameter> ->").bright_magenta(),
        paint("Installs the package named <parameter>").bold()
    ).show()

    paint(
        paint("\tupgrade <parameter> ->").bright_magenta(),
        paint("Upgrades the package named <parameter>").bold()
    ).show()

    paint(
        paint("\tuninstall <parameter> ->").bright_magenta(),
        paint("Uninstalls the package named <parameter>").bold()
    ).show()

    print()
