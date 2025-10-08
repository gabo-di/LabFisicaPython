import math
from pydantic import validate_call 

@validate_call(validate_return=True)
def sphere(r: float)->float:
    return 4 * math.pi * r**3 / 3

@validate_call(validate_return=True)
def sphere_err_deriv(r: float, r_err: float)->float:
    return 4 * math.pi * r**2 * r_err     

@validate_call(validate_return=True)
def sphere_err_diff(r: float, r_err: float)->float:
    return abs(sphere(r+r_err) - sphere(r-r_err))/2

@validate_call(validate_return=True)
def cilinder(r: float, h: float)->float:
    return math.pi * r**2 * h

@validate_call(validate_return=True)
def cilinder_err_deriv(r: float, h:float, r_err:float, h_err:float)->float:
    r_err_contribution = 2 * math.pi * r * h * r_err
    h_err_contribution = math.pi * r**2 * h_err
    return math.sqrt((r_err_contribution)**2 + (h_err_contribution)**2)

@validate_call(validate_return=True)
def cilinder_err_diff(r:float, h:float, r_err:float, h_err:float)->float:
    r_err_contribution = abs( cilinder(r+r_err,h) - cilinder(r-r_err,h) )/2
    h_err_contribution = abs( cilinder(r,h+h_err) - cilinder(r,h-h_err) )/2
    return math.sqrt((r_err_contribution)**2 + (h_err_contribution)**2)

def main_sphere():
    r = 1.2
    r_err = 0.01

    vol_s = sphere(r)
    err_vol_diff = sphere_err_deriv(r, r_err)
    err_vol_deriv = sphere_err_diff(r, r_err)

    print("")
    print("Volumne esfera")
    print(vol_s)
    print("Error volumen diferencias finitas");
    print(err_vol_diff)
    print("Error volumen derivada");
    print(err_vol_deriv)

def main_cilinder():
    r = 1.2
    h = 1.2
    r_err = 0.01
    h_err = 0.01

    vol_c = cilinder(r,h)
    err_vol_diff = cilinder_err_deriv(r, h, r_err, h_err)
    err_vol_deriv = cilinder_err_diff(r, h, r_err, h_err)

    print("")
    print("Volumne cilindro")
    print(vol_c)
    print("Error volumen diferencias finitas");
    print(err_vol_diff)
    print("Error volumen derivada");
    print(err_vol_deriv)

if __name__ == "__main__":
    main_sphere()
    main_cilinder()
