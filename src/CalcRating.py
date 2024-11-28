# src/CalcRating.py
from src.Types import DataType

class CalcRating:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.rating: dict[str, float] = {}

    def calc(self) -> dict[str, float]:
        """Вычисляет средний рейтинг студентов"""
        for student, subjects in self.data.items():
            total_score = sum(score for _, score in subjects)
            self.rating[student] = total_score / len(subjects)
        return self.rating

    def count_excellent_students(self) -> int:
        """Считает количество студентов, у которых баллы ≥ 90 по всем предметам"""
        count = 0
        for subjects in self.data.values():
            if all(score >= 90 for _, score in subjects):
                count += 1
        return count
