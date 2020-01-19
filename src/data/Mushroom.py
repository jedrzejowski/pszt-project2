from data.MyAttributes import MyAttributes


class Mushroom:

    def __init__(self, line: str):
        self._attrs = line.split()[0].split(',')
        self._assertAttrs()

    def isPositive(self) -> bool:
        return self._attrs[0] == 'e'

    def isNegative(self) -> bool:
        return self._attrs[0] == 'p'

    def getAttrValue(self, attr_index: int):
        return self._attrs[attr_index]

    def _assertAttrs(self):
        max_attr_length = 23
        length = len(self._attrs)

        if length != 23:
            raise Exception("Mushroom: attributes number missmatch")

        for i in range(1, 23):
            if not MyAttributes[i].isValueValid(self._attrs[i]):
                raise Exception("Mushroom: attribute has invalid value")
