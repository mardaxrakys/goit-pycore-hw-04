
import sys
from pathlib import Path
from colorama import Fore, Style, init

# функція для виведення вмісту директорії
def print_directory_contents(path, indent_level=0):
    #------------------------------------------------------------------------------
    # перевірка існування директорії
    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях {path} не існує.{Style.RESET_ALL}")
        return
    if not path.is_dir():
        print(f"{Fore.RED}Помилка: шлях {path} не є директорією.{Style.RESET_ALL}")
        return

    # виведення назви директорії
    print(f"{' ' * 2 * indent_level}{Fore.BLUE}{path.name}/{Style.RESET_ALL}")

    for item in sorted(path.iterdir()):
        if item.is_dir():
            # рекурсивний виклик для директорій
            print_directory_contents(item, indent_level + 1)
        else:
            # виведення назви файлу
            print(f"{' ' * 2 * (indent_level + 1)}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    #----------------------------------------------------------------------------------

# виклик функції для виведення вмісту директорії 
if __name__ == "__main__":

    init() # ініціалізація colorama

    # перевірка кількості аргументів командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python {sys.argv[0]} <шлях до директорії>{Style.RESET_ALL}")
    else:
        directory_path = Path(sys.argv[1])
        print_directory_contents(directory_path)

# приклад виклику з командного рядка: python "[absolute path]\homework-03.py" "[directory to process path]"
