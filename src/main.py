from Algorhythm import ID3, C45
from data.MushroomCollection import MushroomCollection
from data.MyAttributes import MyAttributes
from data.Tree import TreeNode


def newCollection(start, end) -> MushroomCollection:
    collection = MushroomCollection("../assets/agaricus-lepiota.data")
    if end == -1:
        end = len(collection._mushrooms)
    collection._mushrooms = collection._mushrooms[start:end]
    return collection


max_data = 8124 - 1


def testTree(T: TreeNode, S: MushroomCollection):
    return 0


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

    print("[" + str(0) + " : " + str(spacer) + " ] | " +
          "[ " + str(spacer + 1) + " : " + str(max_data) + " ] | " +
          str(e1) + " | " +
          str(e2) + " | ")


for i in range(100, 1000, 100):
    makeTest(i)
for i in range(1000, max_data, 1000):
    makeTest(i)

# print(ID3(
#     MyAttributes[0],
#     MyAttributes[1:(len(MyAttributes) - 1)],
#     myCollection
# ).dump())
