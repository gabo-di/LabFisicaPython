from labfisica import CsvXYReader
from labfisica import MMC

def test_mmc(data_dir):
    csv_path = data_dir / "data.csv"
    xy = CsvXYReader.read(csv_path)

    mmc = MMC.MMC(x = xy.x, y = xy.y)
    assert mmc.A == 0
    assert mmc.B == 0
    assert mmc.A_err == 0
    assert mmc.B_err == 0
