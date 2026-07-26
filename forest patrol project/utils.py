# utils.py
import os
import sys
import tty
import termios

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def getch():
    """Считывает один символ с клавиатуры без нажатия Enter (кросс-платформенно)"""
    if os.name == 'nt':
        import msvcrt
        return msvcrt.getch().decode('utf-8', errors='ignore')
    else:
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch