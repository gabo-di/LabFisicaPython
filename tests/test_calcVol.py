from labfisica import CalcVol
import pytest

EPS = 1e-5
r = 1.2
h = 1.2
r_err = 0.01
h_err = 0.01

def test_sphereErr():
    err_vol_diff = CalcVol.sphere_err_diff(r, r_err)
    err_vol_deriv = CalcVol.sphere_err_deriv(r, r_err)

    assert err_vol_deriv == pytest.approx(err_vol_diff, abs=EPS)

def test_cilinderErr():
    err_vol_diff = CalcVol.cilinder_err_diff(r, h, r_err, h_err)
    err_vol_deriv = CalcVol.cilinder_err_deriv(r, h, r_err, h_err)

    assert err_vol_deriv == pytest.approx(err_vol_diff,  abs=EPS)
