import math
from math import *

def toSqrt(result_a, resultat_b): #fonction calcule y=carré(a)*b = (?)
    int_result = int(result_a) #cast str -> int
    int_resultat = int(resultat_b)
    x = sqrt(int_result)*int_resultat
    x_convert = math.floor(x)
    y = str(x_convert) #cast int -> str
    return x_convert
