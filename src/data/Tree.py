from typing import List

from data.Attribute import Attribute
from data.MushroomCollection import MushroomCollection


class TreePart:
    def __init__(self, name):
        self._parent = None
        self._name = name

    def getName(self):
        return self._name

    def getParent(self):
        return self._parent

    def hasParent(self) -> bool:
        return self._parent is None

    def setParent(self, new_parent):
        if not isinstance(new_parent, TreePart):
            raise Exception("TreePart.setParent(): new_parent is not TreePart")
        self._parent = new_parent

    def dump(self, prefix1: str = "", prefix2: str = "") -> str:
        pass


class TreeNode(TreePart):
    def __init__(self, attribute: Attribute, children: List[TreePart]):
        self._attribute = attribute
        self._children = children
        TreePart.__init__(self, attribute.getName())

    def getChild(self, i: int) -> TreePart:
        return self._children[i]

    def getChildCount(self):
        return len(self._children)

    def getChildren(self):
        return self._children

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

        for i in range(0, len(self._children)):
            name = self._attribute.getValueName(i)
            name = " " + name + " -> "
            branch = self._children[i]
            if i == len(self._children) - 1:
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
        return prefix1 + self.getName()
