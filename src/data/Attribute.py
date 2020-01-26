class Attribute:

    def __init__(self, name, values):
        self._name = name
        self._values = []
        self._names = []

        for v in values:
            [name, value] = v.split('=')
            self._values.append(value)
            self._names.append(name)

    def getValuesCount(self):
        return len(self._values)

    def getValues(self):
        return self._values

    def getValue(self, index):
        return self._values[index]

    def getValueIndex(self, value):
        return self._values.index(value)

    def isValueValid(self, value):
        return value in self._values

    def getValuesCount(self):
        return len(self._values)

    def getName(self):
        return self._name

    def getValueName(self, index):
        return self._names[index]

    def getIndex(self):
        from data.MyAttributes import MyAttributes
        return MyAttributes.index(self)
