from getpass import getpass
import os
import time
import msvcrt
import ctypes
import curses
import datetime
from enum import Enum

# Constants
COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "pink": "\x1b[38;5;201m",
    "cyan": "\033[36m",
    "white": "\033[37m"
}

STYLES = {
    "dim": "\033[2m",
    "normal": "\033[0m",
    "bright": "\033[1m"
}

BACKGROUNDS = {
    "black": "\033[40m",
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "pink": "\x1b[38;5;201m",
    "cyan": "\033[46m",
    "white": "\033[47m"
}

class LogLevel(Enum):
    SUCCESS = "success"
    ERROR = "error"
    DEBUG = "debug"
    INFO = "info"

class ConsoleX:
    def __init__(self):
        self.reset = "\033[0m"

    def clear(self):
        """Clears the console."""
        os.system("cls" if os.name == "nt" else "clear")

    def title(self, title):
        """Sets the console title."""
        os.system(f"title {title}")

    def size(self, width, height):
        """Sets the console size."""
        os.system(f"mode con: cols={width} lines={height}")

    def move(self, x, y):
        """Moves the console window."""
        os.system(f"mode con: cols={x} lines={y}")

    def hide(self):
        """Hides the console."""
        os.system("cls" if os.name == "nt" else "clear")

    def show(self):
        """Shows the console."""
        os.system("cls" if os.name == "nt" else "clear")

    def print(self, text, end="\n", fg=None, bg=None, style=None):
        """Prints text to the console with optional color, background, and style."""
        if fg and fg in COLORS:
            text = f"{COLORS[fg]}{text}"
        if bg and bg in BACKGROUNDS:
            text = f"{BACKGROUNDS[bg]}{text}"
        if style and style in STYLES:
            text = f"{STYLES[style]}{text}"
        print(f"{text}{self.reset}", end=end)

    def input(self, text, fg=None, bg=None, style=None):
        """Gets user input."""
        if fg and fg in COLORS:
            text = f"{COLORS[fg]}{text}"
        if bg and bg in BACKGROUNDS:
            text = f"{BACKGROUNDS[bg]}{text}"
        if style and style in STYLES:
            text = f"{STYLES[style]}{text}"
        return input(f"{text}{self.reset}")

    def pause(self, text="Press any key to continue..."):
        """Pauses the console."""
        self.print(text, end="")
        getpass("")
        print()
        
    def confirm(self, text): # work in progress
        """Confirms an action with the user."""
        self.print(text, end="")
        return msvcrt.getch() in [b"y", b"Y"]

    def progress(self, text, length, delay=0.1, percent=True):
        """Displays a progress bar."""
        for i in range(length+1):
            progress_bar = "#" * i + " " * (length - i)
            if percent:
                percent_complete = (i / length) * 100
                progress_text = f"\r{text} [\033[32m{progress_bar}\033[0m] {percent_complete:.2f}%\r"
            else:
                progress_text = f"\r{text} [\033[32m{progress_bar}\033[0m]\r"
            self.print(progress_text, end="")
            time.sleep(delay)
        print()
        
    def alert(self, title, message, style="ok"):
        """Displays an alert."""
        if style == "ok":
            style = 0x0
        elif style == "error":
            style = 0x10
        elif style == "warning":
            style = 0x30
        elif style == "info":
            style = 0x40
        elif style == "question":
            style = 0x20
        else:
            style = 0x0
        return ctypes.windll.user32.MessageBoxW(0, message, title, style)

    def log(self, message, level):
        """Logs a message with a given log level."""
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if level == LogLevel.SUCCESS:
            symbol = "INF ✅ "
            color = "pink"
        elif level == LogLevel.ERROR:
            symbol = "❌ "
            color = "red"
        elif level == LogLevel.DEBUG:
            symbol = "DBG 🐛 "
            color = "magenta"
        elif level == LogLevel.INFO:
            symbol = "INFO ❓ "
            color = "cyan"
        else:
            symbol = "❓ "
            color = "magenta"
        self.print(f"[{current_time}] {symbol} {message}", fg=color)