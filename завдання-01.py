
from pathlib import Path

def total_salary(path):
    #------------------------------------------------------------------------------
    # перевірка існування файлу
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не знайдено")
    #----------------------------------------------------------------------------------
    total_salaries = 0
    developer_count = 0

    # використання менеджера контексту для автоматичного закриття файлу
    with path.open('r', encoding='utf-8') as salary_file:
        for line in salary_file:
            parts = line.strip().split(',')
            if len(parts) != 2:
                raise ValueError(f"Некоректний формат: '{line.strip()}'. Кожен рядок файлу має містити (ім'я,зарплата)")
            
            # перетворення зарплати в число
            try:
                salary = int(parts[1])
            except ValueError:
                raise ValueError(f"Недійсне значення зарплати: '{line.strip()}'. Зарплата повинна бути числом.")
            
            total_salaries += salary
            developer_count += 1

    if developer_count == 0:
        raise ValueError("Немає даних для обробки.")
    #----------------------------------------------------------------------------------
    # підрахунок середньої ЗП
    average_salary = total_salaries / developer_count if developer_count else 0
    return (total_salaries, average_salary)

#----------------------------------------------------------------------------------

if __name__ == "__main__":
    file_name = "zarplata.txt"
    try:
        total, average = total_salary(file_name)
        print(f"Загальна сума зарплат: {total}, Середня зарплата: {int(average)}")
    except Exception as e:
        print(f"Помилка: {e}")