from pathlib import Path
import csv
from typing import List
from .XYData import XYData

def read(csv_path: Path) -> XYData:
    xs: List[float] = []
    ys: List[float] = []
    xName = "X"
    yName = "Y"

    with csv_path.open(newline="", encoding="utf-8") as f:
        r = csv.reader(f)  # default delimiter=','
        # header 
        header = next(r, None)
        if header and len(header) >= 2:
            xName = (header[0] or "X").strip() or "X"
            yName = (header[1] or "Y").strip() or "Y"

        # data rows
        for row in r:
            if len(row) < 2:
                continue
            sx = (row[0] or "").strip()
            sy = (row[1] or "").strip()
            if not sx or not sy:
                continue
            try:
                xs.append(float(sx))
                ys.append(float(sy))
            except ValueError:
                # skip malformed line
                continue

    return XYData(x=xs, y=ys, xName=xName, yName=yName)
