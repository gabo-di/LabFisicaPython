from labfisica import CsvXYReader
from pathlib import Path

def test_csvreader(data_dir):
    csv_path = data_dir / "data.csv"
    xy = CsvXYReader.read(csv_path)
    
    assert "X" == xy.xName
    assert "Y" == xy.yName
    assert 5 == len(xy.x)
    assert [1, 3, 5, 7 ,9] == xy.x
    assert [2, 4, 6, 8 ,10] == xy.y
