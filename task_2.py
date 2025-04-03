import os

def get_cats_info(path):
    """
    Зчитує інформацію про котів з файлу та повертає список словників.

    Args:
        path (str): Шлях до текстового файлу.

    Returns:
        list: Список словників з інформацією про кожного кота,
              або None, якщо файл не знайдено.
    """
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 3:
                    cat_id, name, age = data
                    cats_info.append({"id": cat_id, "name": name, "age": age})
                elif line.strip():
                    print(f"Увага: Некоректний формат рядка: {line.strip()}")
        return cats_info
    except FileNotFoundError:
        print(f"Помилка: Файл '{path}' не знайдено.")
        return None

if __name__ == '__main__':
    # Створимо тестовий файл
    test_data = "60b90c1c13067a15887e1ae1,Tayson,3\n60b90c2413067a15887e1ae2,Vika,1\n60b90c2e13067a15887e1ae3,Barsik,2\n60b90c3b13067a15887e1ae4,Simon,12\n60b90c4613067a15887e1ae5,Tessi,5"
    with open("cats_file.txt", "w", encoding="utf-8") as f:
        f.write(test_data)

    cats = get_cats_info("cats_file.txt")
    if cats:
        print(cats)

    # Перевірка випадку відсутності файлу
    get_cats_info("non_existent_cats_file.txt")
