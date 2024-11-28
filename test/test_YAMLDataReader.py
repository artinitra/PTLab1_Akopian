import pytest
from src.YAMLDataReader import YAMLDataReader
from src.Types import DataType

class TestYAMLDataReader:
    @pytest.fixture
    def yaml_content(self) -> tuple[str, DataType]:
        content = """
        Иванов Иван Иванович:
          математика: 90
          литература: 95
        Петров Петр Петрович:
          химия: 85
          физика: 100
        """
        data = {
            "Иванов Иван Иванович": [("математика", 90), ("литература", 95)],
            "Петров Петр Петрович": [("химия", 85), ("физика", 100)],
        }
        return content, data

    def test_read(self, yaml_content, tmpdir):
        path = tmpdir.join("test.yaml")
        path.write(yaml_content[0])
        reader = YAMLDataReader()
        assert reader.read(str(path)) == yaml_content[1]
