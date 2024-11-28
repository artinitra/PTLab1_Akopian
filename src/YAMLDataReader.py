import yaml
from src.Types import DataType
from src.DataReader import DataReader

class YAMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        # Проверка структуры данных
        if isinstance(data, dict):
            # Если данные представлены словарем, преобразуем в список
            data = [data]
        elif not isinstance(data, list):
            # Если данные не являются списком или словарем, выбрасываем исключение
            raise ValueError("Файл YAML должен содержать список или словарь!")

        # Обработка списка данных
        for student_entry in data:
            if not isinstance(student_entry, dict):
                raise ValueError("Каждый элемент списка должен быть словарем!")
            for student, subjects in student_entry.items():
                if not isinstance(subjects, dict):
                    print(f"Ошибка: данные о предметах у студента '{student}' должны быть словарем. Пропуск...")
                    continue
                # Преобразуем данные в список пар (предмет, оценка)
                self.students[student] = [(subject, int(score)) for subject, score in subjects.items()]
        
        return self.students
