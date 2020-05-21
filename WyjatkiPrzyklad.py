
"""
def average(collection):
    S=sum(collection)
    L=len(collection)
    return S/L

try:
    print(average([1]))
    print(average([1,2]))
except ZeroDivisionError:
    print("Powstal blad dzielenie - nie dziel przez ZERO")

except (AttributeError, KeyError):
    print("Blad dostepu do parametru")
else:
    print("Kod w naszym try nie wywola bledu")
finally:
    print("Kod tutaj sie zawsze wykona")


def divide(x,y):
    try:
        result = x/y
        print("Super, may wynik!!!: ", result)
    except ZeroDivisionError:
        print("leee, dzielisz przez zero")

divide(3, 0)
"""
x=5
if x<10:
    raise ValueError('x pownien nie byc mniejszy od 10')