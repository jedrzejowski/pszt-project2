class Attribute:
    _name = None
    _values = []
    _names = []

    def __init__(self, name, values):
        self._name = name

        for v in values:
            [value, name] = v.split('=')
            self._values.append(value)
            self._names.append(name)

    def getValue(self, index):
        return self._values[index]

    def isValueValid(self, value):
        return value in self._values

    def getValueCount(self):
        return len(self._values)

    def getName(self):
        return self._name

    def getValueName(self, index):
        return self._name[index]
