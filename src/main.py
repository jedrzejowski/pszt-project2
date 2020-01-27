#!/usr/bin/python3

import random

from Algorhythm import ID3, C45, makeDecision, testTree
from data.MushroomCollection import MushroomCollection
from data.MyAttributes import MyAttributes


def newCollection(start, end):
    collection = MushroomCollection("../assets/agaricus-lepiota.data")
    if end == -1:
        end = len(collection._mushrooms)
    random.shuffle(collection._mushrooms)
    collection._mushrooms = collection._mushrooms[start:end]
    return collection


max_data = 8124 - 1


def makeTest(spacer):
    # obcięcie na zbiór treningowy
    training = newCollection(0, spacer)
    # obcięcie na zbiór testujący
    testing = newCollection(spacer + 1, max_data)

    id3 = ID3(
        MyAttributes[0],
        MyAttributes[1:(len(MyAttributes) - 1)],
        training
    )

    c45 = C45(
        MyAttributes[0],
        MyAttributes[1:(len(MyAttributes) - 1)],
        training
    )

    e1 = testTree(id3, testing)
    e2 = testTree(c45, testing)

    # print(id3.dump())

    print("| [ " + str(0) + " : " + str(spacer) + " ] | " +
          "[ " + str(spacer + 1) + " : " + str(max_data) + " ] | `" +
          str(e1) + "` | `" + str(e2) + "` | ")


print("| Zbiór treningowy | Zbiór testujący | Wynik ID3 | Wynik C4.5 |")
print("| --- | --- | --- | --- |")
for i in range(100, 1000, 100):
    makeTest(i)
for i in range(1000, max_data, 1000):
    makeTest(i)

# print(ID3(
#     MyAttributes[0],
#     MyAttributes[1:(len(MyAttributes) - 1)],
#     myCollection
# ).dump())
