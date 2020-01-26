from typing import List, Union
import math

from data import Mushroom
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


def e_S(T: TreeNode, S: MushroomCollection) -> float:
    error_count = 0
    for i in range(0, S.getCount()):
        mushroom = S.get(i)
        # print(mushroom.getAttrValue(0), makeDecision(T, mushroom))
        if mushroom.getAttrValue(0) != makeDecision(T, mushroom):
            error_count = error_count + 1

    return error_count / S.getCount()


def e_T(T: TreeNode, S: MushroomCollection) -> float:
    err = e_S(T, S)
    return err + (math.sqrt(err * (1 - err)) / S.getCount())


def ID3(C: List[Attribute], R: List[Attribute], S: MushroomCollection) -> TreePart:
    R = R.copy() # python i jego referencje

    print(len(R))
    if S.isEmpty():
        if not S.hasPrevious():
            raise Exception("ID3(): S is empty")

        S = S.getPrevious()
        C = MyAttributes[0]
        values_count = list(map(lambda v: S.getCountOf(C.getIndex(), v), C.getValues()))
        i = values_count.index(max(values_count))
        return TreeLeaf(C.getValueName(i), C.getValue(i))

    if not R:
        C = MyAttributes[0]
        values_count = list(map(lambda v: S.getCountOf(C.getIndex(), v), C.getValues()))
        i = values_count.index(max(values_count))
        return TreeLeaf(C.getValueName(i), C.getValue(i))

    gains = list(map(lambda a: Gain(a, S), R))
    D = R.pop(gains.index(max(gains)))

    branches = list(map(lambda v: ID3(C, R, S.filterByAttrValue(D.getIndex(), v)), D.getValues()))

    return TreeNode(D, branches)


# def C45(C, R, S):
#     pass
def C45(C, R, S):
    T = ID3(C, R, S)

    if isinstance(T, TreeNode):

        def getLeaf(index: int, tree_node: TreeNode = T) -> Union[TreeLeaf, int]:
            leaf_found = 0

            for tree_part in tree_node.getChildren():
                if isinstance(tree_part, TreeLeaf):
                    leaf_found = leaf_found + 1
                    if leaf_found == index + 1:
                        return tree_part

                if isinstance(tree_part, TreeNode):
                    out = getLeaf(index - leaf_found, tree_part)
                    if isinstance(out, int):
                        leaf_found = leaf_found + out
                    if isinstance(out, TreeLeaf):
                        return out

            return leaf_found

        leaf_index = 0
        leaf = getLeaf(leaf_index, T)

        # Dla każdego liścia T :
        while isinstance(leaf, TreeLeaf):
            # Dla każdego węzła w na drodze liść-korzeń :
            node = leaf.getParent()
            while node != T:
                # wyciągamy przypadki tyczące się wtylko naszego drzewa
                S_node = filterCollectionToTreeNode(T, node, S)
                # e0
                e_0 = e_T(node, S_node)
                # e1
                histogram = [0] * (MyAttributes[0].getValuesCount() + 1)
                for i in range(0, S_node.getCount()):
                    mushroom = S_node.get(i)
                    value_index = MyAttributes[0].getValueIndex(mushroom.getAttrValue(0))
                    histogram[value_index] = histogram[value_index] + 1
                most_value_index = histogram.index(max(histogram))
                e_1 = max(histogram) / S_node.getCount()
                #
                node = node.getParent()
                if e_0 >= e_1:
                    node.setChild(most_value_index, TreeLeaf(MyAttributes[0].getValueName(most_value_index),
                                                             MyAttributes[0].getValue(most_value_index)))
            #
            leaf_index = leaf_index + 1
            leaf = getLeaf(leaf_index, T)

    else:
        raise Exception("C45: fatal error")

    return T


def makeDecision(T: TreeNode, mushroom: Mushroom) -> str:
    while True:
        attr_index = T.getAttribute().getIndex()
        value = mushroom.getAttrValue(attr_index)
        value_index = MyAttributes[attr_index].getValueIndex(value)
        T = T.getChild(value_index)

        if isinstance(T, TreeLeaf):
            return T.getValue()


def filterCollectionToTreeNode(T_top: TreeNode, T_me: TreeNode, S: MushroomCollection) -> MushroomCollection:
    T_current = T_me
    while True:
        T_parent = T_current.getParent()  # bierzemy rodzina
        value_index = T_parent.getChildren().index(T_current)  # bierzemy index w rodzicu
        attribute = T_parent.getAttribute()  # i na jego podstawie bierzemy atrubut jakim są połączeni

        S = S.filterByAttrValue(attribute.getIndex(), attribute.getValue(value_index))

        T_current = T_parent
        if T_parent == T_top:
            break

    return S
