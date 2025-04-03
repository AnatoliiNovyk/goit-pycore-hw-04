import os

def total_salary(path):
    """
    Аналізує файл із заробітними платами розробників та повертає загальну та середню суму.

    Args:
        path (str): Шлях до текстового файлу.

    Returns:
        tuple: Кортеж із загальної суми зарплат та середньої заробітної плати,
               або None, якщо файл не знайдено або дані некоректні.
    """
    total_salary = 0
    employee_count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 2:
                    try:
                        salary = int(data[1])
                        total_salary += salary
                        employee_count += 1
                    except ValueError:
                        print(f"Увага: Некоректний формат зарплати в рядку: {line.strip()}")
                elif line.strip():
                    print(f"Увага: Некоректний формат рядка: {line.strip()}")

        if employee_count > 0:
            average_salary = total_salary / employee_count
            return total_salary, average_salary
        else:
            return 0, 0

    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return None

if __name__ == '__main__':
    # Створимо тестовий файл
    test_data = "Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000"
    with open("salary_file.txt", "w", encoding="utf-8") as f:
        f.write(test_data)

    result = total_salary("salary_file.txt")
    if result:
        total, average = result
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    # Перевірка випадку відсутності файлу
    total_salary("non_existent_file.txt")
