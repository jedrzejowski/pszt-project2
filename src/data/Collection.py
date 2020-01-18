from data.Mushroom import Mushroom
from data.MyAttributes import MyAttributes


class Collection:
    _array = []

    def __init__(self, path):

        shrooms = open("../assets/agaricus-lepiota.data", "r")

        if shrooms.mode != 'r':
            print("Nie można wczytać pliku")
            exit(1)

        line = shrooms.readline()
        while line:
            self._array.append(Mushroom(line))
            line = shrooms.readline()

    def getCount(self):
        return len(self._array)

    def getAttrCounter(self):
        return self._array[0]