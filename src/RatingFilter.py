import statistics
from src.Types import RatingType


class RatingFilter:

    def __init__(self, data: RatingType) -> None:
        self.data = data
        self.filtered_rating = {}

    def filter_get_second_quantile(self) -> RatingType:
        sorted_students = dict(sorted(self.data.items(), key=lambda item: item[1]))

        # Calculate the total number of students
        n = len(self.data)

        # Calculate the lower and upper bounds of the second quartile
        lower_bound = statistics.median(list(sorted_students.values())[:n // 4])
        upper_bound = statistics.median(list(sorted_students.values())[n // 4:n // 2])

        # Find all students whose scores fall within the range of the second quartile
        second_quartile_students = {name: score for name, score in sorted_students.items()
                                    if lower_bound <= score <= upper_bound}

        return second_quartile_students
