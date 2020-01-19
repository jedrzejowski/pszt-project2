from typing import List
import math

from data.Attribute import Attribute
from data.MushroomCollection import MushroomCollection
from data.MyAttributes import MyAttributes
from data.Tree import TreeNode, TreeLeaf, TreePart

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
        print("[Warn] I(P): out is out of [0.0, 1.0] range")

    return out


def Info1(T: MushroomCollection):
    P = list()

    C = MyAttributes[0]

    if T.getCount() == 0:
        return 0

    for i in C.getValues():
        P.append(T.getCountOf(0, i) / T.getCount())

    return I(P)


def Info2(X: Attribute, T: MushroomCollection):
    sigma = list()

    for value in X.getValues():
        Ti = T.filterByAttrValue(X.getIndex(), value)
        sigma.append(Ti.getCount() / T.getCount() * Info1(Ti))

    out = sum(sigma)

    if out > 1 or 0 > out:
        print("[Warn] Info2(X,T): out is out of [1..0] range")

    return out


def Gain(X: Attribute, T: MushroomCollection):
    return Info1(T) - Info2(X, T)


def ID3(C: List[Attribute], R: List[Attribute], S: MushroomCollection) -> TreePart:
    if S.isEmpty():
        return TreeLeaf("S=∅ error")

    if not R:
        C = MyAttributes[0]
        values_count = list(map(lambda v: S.getCountOf(C.getIndex(), v), C.getValues()))
        i = values_count.index(max(values_count))
        return TreeLeaf(C.getValueName(i))

    gains = list(map(lambda a: Gain(a, S), R))
    D = R.pop(gains.index(max(gains)))

    branches = list(map(lambda v: ID3(C, R, S.filterByAttrValue(D.getIndex(), v)), D.getValues()))

    return TreeNode(D, branches)


def C45(C, R, S):
    pass
