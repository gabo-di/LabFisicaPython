from labfisica import CalcStats
import pytest

EPS = 1e-10
x = [0.1, 0.2, 0.3]

def test_mean():
    x_mean = 0.2

    assert x_mean == pytest.approx(CalcStats.calcMean(x), EPS)

def test_meanvar():
    x_mean = 0.2
    x_var = 2*0.01/3
    y = CalcStats.calcMeanVar(x)

    assert x_mean == pytest.approx(y[0], EPS)
    assert x_var == pytest.approx(y[1], EPS)
