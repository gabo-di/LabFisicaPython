from pathlib import Path
from typing import Tuple

from labfisica.CsvXYReader import read  

import matplotlib.pyplot as plt

def make_plot(data) -> Tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(8, 6))  
    ax.scatter(data.x, data.y, marker='o')  
    ax.set_title("Scatter Plot")
    ax.set_xlabel(data.xName)
    ax.set_ylabel(data.yName)
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
    fig.tight_layout()
    return fig, ax

def show_plot(fig: plt.Figure) -> None:
    plt.show() 

def save_plot(fig: plt.Figure, filename: str | Path) -> None:
    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(filename, format="png", dpi=150)

def main() -> None:
    import sys
    if len(sys.argv) < 2:
        print("Usage: poetry run python src/labfisica/CsvScatterPlot.py <file.csv>")
        sys.exit(2)

    csv_path = Path(sys.argv[1])
    data = read(csv_path)
    fig, _ = make_plot(data)
    show_plot(fig)

if __name__ == "__main__":
    main()
