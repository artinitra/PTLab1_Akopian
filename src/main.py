# src/main.py
from src.YAMLDataReader import YAMLDataReader
from src.CalcRating import CalcRating
from pprint import pprint

def main():
    path = "data/data.yaml"  # Укажите путь к вашему YAML-файлу

    # Чтение данных
    reader = YAMLDataReader()
    students = reader.read(path)
    
    print("\n=== Данные о студентах ===")
    for student, subjects in students.items():
        print(f"- {student}:")
        for subject, score in subjects:
            print(f"  {subject}: {score}")
    
    # Расчет количества отличников
    calc = CalcRating(students)
    excellent_students = calc.count_excellent_students()
    
    print("\n=== Результаты ===")
    print(f"Количество студентов-отличников: {excellent_students}")

if __name__ == "__main__":
    main()
