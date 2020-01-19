from typing import List

from data.Attribute import Attribute
from data.MushroomCollection import MushroomCollection


class TreePart:
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def dump(self, prefix1: str = "", prefix2: str = "") -> str:
        pass


class TreeNode(TreePart):
    def __init__(self, attribute: Attribute, branches: List[TreePart]):
        self._attribute = attribute
        self._branches = branches
        TreePart.__init__(self, attribute.getName())

    def dump(self, prefix1: str = "", prefix2: str = "") -> str:
        # https://www.utf8-chartable.de/unicode-utf8-table.pl?start=9472&unicodeinhtml=dec
        line = ' ┃ '
        middle = ' ┣━'
        end = ' ┗━'
        EOF = '\n'

        lines = list()

        def addLines(line):
            prefix = prefix1 if len(lines) == 0 else prefix2
            for l in line.split(EOF):
                lines.append(prefix + l)

        addLines(self.getName())

        for i in range(0, len(self._branches)):
            name = self._attribute.getValueName(i)
            name = " " + name + " -> "
            branch = self._branches[i]
            if i == len(self._branches) - 1:
                # element ostatni
                addLines(branch.dump(end + name, '   '))
            else:
                addLines(branch.dump(middle + name, line))

        return EOF.join(lines)


class TreeLeaf(TreePart):
    def __init__(self, value):
        self._value = value
        TreePart.__init__(self, value)

    def dump(self, prefix1: str = "", prefix2: str = "") -> str:
        return prefix1 +  self.getName()
