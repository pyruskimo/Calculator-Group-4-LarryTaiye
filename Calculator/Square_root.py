#def square_root(a):
#    a = float(a)
#    return round(a, 9)
from cmath import sqrt


def square_root(a):
    a = float(a)
    # a = sqrt(int(a))
    return round((a ** .5), 9)

