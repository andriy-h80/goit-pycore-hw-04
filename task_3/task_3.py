
'''
Розробіть скрипт, який приймає шлях до директорії
в якості аргументу командного рядка і візуалізує структуру цієї директорії,
виводячи імена всіх піддиректорій та файлів.
Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
'''

import sys
from pathlib import Path
from colorama import Fore, Style

def print_tree(path: Path, line_prefix: str = ""):
    if not path.exists():
        print(Fore.RED + f"Помилка: шлях '{path}' не існує." + Style.RESET_ALL)
        return

    print(f"{line_prefix}{Fore.BLUE} \U0001F4C2 {path.name}{Style.RESET_ALL}")

    folders = []
    files = []

    for item in path.iterdir():
        if item.is_dir():
            folders.append(item)
        else:
            files.append(item)

    for folder in folders:
        print_tree(folder, line_prefix + " ┃ ")

    for file in files:
        print(f"{line_prefix} ┃ {Fore.YELLOW} \U0001F4DC {file.name}{Style.RESET_ALL}")


if len(sys.argv) > 1:
     path_arg = sys.argv[1]
else:
    path_arg = "."

path = Path(path_arg)
print_tree(path)
