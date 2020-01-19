from typing import List
import math

from data.Attribute import Attribute
from data.Collection import Collection
from data.MyAttributes import MyAttributes

Vector = List[float]


def I(P: Vector) -> float:
    def myLog(p):
        if p == 0:
            return 0
        return p * math.log(p)

    if sum(P) != 1.0:
        print("[Warn] I(P): sum of P is not equal 1.0")

    out = -sum(list(map(myLog, P)))

    if out > 1 or 0 > out:
        raise Exception("I(): out is out of [1..0] range")

    return out


def Info1(T: Collection):
    P = list()

    C = MyAttributes[0]

    if T.getCount() == 0:
        return 0

    for i in C.getValues():
        P.append(T.getCountOf(0, i) / T.getCount())

    return I(P)


def Info2(X: Attribute, T: Collection):
    sigma = list()

    for value in X.getValues():
        Ti = T.filterByAttrValue(X.getIndex(), value)
        sigma.append(Ti.getCount() / T.getCount() * Info1(Ti))

    out = sum(sigma)

    if out > 1 or 0 > out:
        raise Exception("Info2(): out is out of [1..0] range")

    return out


def Gain(X: Attribute, T: Collection):
    return Info1(T) - Info2(X, T)


def ID3(C: List[Attribute], R: List[Attribute], S: Collection):
    if S.isEmpty():
        raise Exception("S=∅ error")

    if not R:
        raise Exception("R=∅ error")

    gains = list(map(lambda a: Gain(a, S), R))

    pass


def C45(C, R, S):
    pass
