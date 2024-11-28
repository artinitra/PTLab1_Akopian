from src.CalcRating import CalcRating
from src.Types import DataType, RatingType
from src.RatingFilter import RatingFilter
import pytest


class TestRatingFilter:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingType]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("математика", 100),
                    ("русский язык", 100),
                    ("программирование", 100)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 75),
                    ("русский язык", 75),
                    ("программирование", 75),
                    ("литература", 75)
                ],
            "Тестовый Тест Тестович":
                [
                    ("математика", 50),
                    ("русский язык", 50),
                    ("ОБЖ", 50),
                    ("литература", 50)
                ],
            "Несуществующий студент эвм":
                [
                    ("NotFound", 0),
                    ("NotFound", 0),
                    ("NotFound", 0),
                    ("NotFound", 0)
                ],
            "Существующий студент ивт":
                [
                    ("МЗЯ", 25),
                    ("АрхЭВМ", 25),
                    ("ООП", 25),
                    ("Физика", 25)
                ],
        }

        filtered_rating = {
            "Несуществующий студент эвм": 0, 'Существующий студент ивт': 25.0
        }

        return data, filtered_rating

    def test_init_filter_rating(self, input_data: tuple[RatingType,
                                RatingType]) -> None:
        filter_rating = RatingFilter(input_data[0])
        assert input_data[0] == filter_rating.data

    def test_filter_second_quantile(self, input_data: tuple[DataType,
                                    RatingType]) -> None:
        calc_rating = CalcRating(input_data[0]).calc()
        filter_rating = RatingFilter(calc_rating).filter_get_second_quantile()

        assert pytest.approx(filter_rating) == input_data[1]
