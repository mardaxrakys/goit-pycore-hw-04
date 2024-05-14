
from pathlib import Path

# функція для отримання інформації про котів з файлу
def get_cats_info(file_path: str) -> list:
    #------------------------------------------------------------------------------
    # перевірка існування файлу
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл за адресою {file_path} не знайдено.")
    #----------------------------------------------------------------------------------
    cats_info = []  # список для зберігання інформації про котів

    # використання менеджера контексту
    with path.open('r', encoding='utf-8') as db_file:
        for line in db_file:
            # розділення рядка на частини для аналізу даних про котів
            parts = line.strip().split(',')
            if len(parts) != 3:
                raise ValueError(f"Формат файлу некоректний у рядку {line.strip()}")

            # словник для інформації про кота
            cat_dict = {
                "id": parts[0], # ID кота
                "name": parts[1], # ім'я кота
                "age": parts[2] # вік кота
            }
            cats_info.append(cat_dict)
    #----------------------------------------------------------------------------------
    return cats_info
#----------------------------------------------------------------------------------


if __name__ == "__main__":
    file_path = "cats.txt"
    try:
        cats_info = get_cats_info(file_path)
        print(cats_info)
    except Exception as error_:
        print(f"Error: {error_}")
