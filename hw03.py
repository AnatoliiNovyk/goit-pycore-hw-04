import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def visualize_directory(path, indent=0):
    """Візуалізує структуру директорії."""
    try:
        items = sorted(path.iterdir())
        for item in items:
            if item.is_dir():
                print(f"{'  ' * indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                visualize_directory(item, indent + 1)
            else:
                print(f"{'  ' * indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{Fore.RED}Помилка доступу до директорії: {path}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Використання: python hw03.py <шлях_до_директорії>")
        return

    target_path_str = sys.argv[1]
    target_path = Path(target_path_str)

    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{target_path_str}' не існує.{Style.RESET_ALL}")
        return

    if not target_path.is_dir():
        print(f"{Fore.RED}Помилка: '{target_path_str}' не є директорією.{Style.RESET_ALL}")
        return

    print(f"Структура директорії: {target_path_str}")
    visualize_directory(target_path)

if __name__ == "__main__":
    main()
