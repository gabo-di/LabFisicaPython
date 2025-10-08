from pydantic import validate_call 

@validate_call(validate_return=True)
def calcMean(x: list[float])->float:
    n = 0
    aux = 0
    for xx in x:
        aux += xx
        n += 1
    return aux / n


@validate_call(validate_return=True)
def calcMeanVar(x: list[float])->tuple[float,float]:
    n = 0 
    aux1 = 0
    aux2 = 0
    for xx in x:
        aux1 += xx
        aux2 += xx**2
        n += 1
    return aux1/n, aux2/n - (aux1/n)**2
    
if __name__ == "__main__":
    x = [0.1, 0.2, 0.3]
    y = calcMeanVar(x)
    print("Mean value")
    print(y[0])
    print("Variance")
    print(y[1])
