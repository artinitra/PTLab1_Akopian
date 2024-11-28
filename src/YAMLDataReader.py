import yaml
from src.Types import DataType
from src.DataReader import DataReader

class YAMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
        
        for student_entry in data:
            for student, subjects in student_entry.items():
                if not isinstance(subjects, dict):
                    print(f"Ошибка: данные о предметах у студента '{student}' должны быть словарем.")
                    continue
                self.students[student] = [(subject, int(score)) for subject, score in subjects.items()]
        
        return self.students
