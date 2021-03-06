from data.Mushroom import Mushroom
from data.MyAttributes import MyAttributes


class MushroomCollection:
    """
    Klasa reprezentuje listę grybów z dodatkami ułatwiającymi jej użytkowanie
    """

    def __init__(self, path_or_list, previous_collection=None):
        self._mushrooms = []
        self._previous_collection = previous_collection

        # z pliku
        if isinstance(path_or_list, str):
            shrooms = open(path_or_list, "r")

            if shrooms.mode != 'r':
                print("Nie można wczytać pliku")
                exit(1)

            line = shrooms.readline()
            while line:
                self._mushrooms.append(Mushroom(line))
                line = shrooms.readline()

        # z filtru
        if isinstance(path_or_list, list):
            self._mushrooms = path_or_list

    def getCount(self):
        return len(self._mushrooms)

    def isEmpty(self):
        return len(self._mushrooms) == 0

    def get(self, i):
        return self._mushrooms[i]

    def getCountOf(self, attr_index, value):
        s = 0

        for mushroom in self._mushrooms:
            if mushroom.getAttrValue(attr_index) == value:
                s = s + 1

        return s

    def hasPrevious(self):
        return self._previous_collection is not None

    def getPrevious(self):
        return self._previous_collection

    def filterByAttrValue(self, attr_index, value):
        """
        Filtrowanie grzybów po wartości atrybutu
        :param attr_index:
        :param value:
        :return:
        """
        if not MyAttributes[attr_index].isValueValid(value):
            raise Exception("wrong attribute valie")

        return MushroomCollection(
            list(filter(
                lambda obj: obj.getAttrValue(attr_index) == value,
                self._mushrooms
            )),
            self)
