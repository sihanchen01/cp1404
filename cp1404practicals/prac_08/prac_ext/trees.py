"""
CP1404/CP5632 Practical
Tree class with inherited (specialised tree) classes
by Trevor Andersen
"""
import random
import math

TREE_LEAVES_PER_ROW = 3


class Tree:
    """Represent a tree, with trunk height and a number of leaves."""

    def __init__(self):
        """Initialise a Tree with trunk_height of 1 and full row of leaves."""
        self._trunk_height = 1
        self._leaves = TREE_LEAVES_PER_ROW

    def __str__(self):
        """Return a string representation of the full Tree, e.g.
         ###
         ###
          |
          |    """
        return self.get_ascii_leaves() + self.get_ascii_trunk()

    def get_ascii_leaves(self) -> str:
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % TREE_LEAVES_PER_ROW > 0:
            result += "#" * (self._leaves % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._leaves // TREE_LEAVES_PER_ROW):
            result += "#" * TREE_LEAVES_PER_ROW
            result += "\n"
        return result

    def get_ascii_trunk(self) -> str:
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " | \n"
        return result

    def grow(self, sunlight, water) -> None:
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        self._leaves += random.randint(0, sunlight)


class EvenTree(Tree):
    """ represent an even tree, one that only grows leaves in full rows """

    def grow(self, sunlight, water):
        """Grow like a normal tree, but fill out each row of leaves."""
        Tree.grow(self, sunlight, water)
        while self._leaves % 3 != 0:
            self._leaves += 1


class UpsideDownTree(Tree):
    """Represent an upside-down tree; like a normal tree, but upside-down."""

    def __str__(self):
        """Return a string representation of the full tree,
        upside-down compared to a normal tree."""
        return self.get_ascii_trunk() + self.get_ascii_leaves()


class WideTree(Tree):
    """Represent a wide tree: grows twice as wide as a normal tree, e.g.
 #####
 ######
 ######
   ||
   ||  """

    def __init__(self):
        self._trunk_height = 1
        self._leaves = TREE_LEAVES_PER_ROW * 2

    def get_ascii_leaves(self) -> str:
        """Return a string representation of the tree's leaves."""
        result = ""
        if self._leaves % (TREE_LEAVES_PER_ROW * 2) > 0:
            result += "#" * (self._leaves % (TREE_LEAVES_PER_ROW * 2))
            result += "\n"
        for i in range(self._leaves // (TREE_LEAVES_PER_ROW * 2)):
            result += "#" * (TREE_LEAVES_PER_ROW * 2)
            result += "\n"
        return result

    def get_ascii_trunk(self):
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += "  ||  \n"
        return result


class QuickTree(Tree):
    """Represent a tree that grows more quickly."""
    faster_coefficient = 1.5

    def grow(self, sunlight, water):
        self._trunk_height += math.floor(max(random.randint(0, water)
                                         * self.faster_coefficient, 1))
        self._leaves += math.floor(max(random.randint(0, sunlight)
                                       * self.faster_coefficient, 1))


class FruitTree(Tree):
    """Represent a tree that has fruit as well as leaves, e.g.
.
...
##
###
###
 |
 |  """
    _fruits = 1

    def __str__(self):
        return self.get_ascii_fruits() + self.get_ascii_leaves() + self.get_ascii_trunk()

    def grow(self, sunlight, water):
        #  Fruit trees sometimes gain fruit when the grow method is called, the chance is 1 in 2
        self._fruits += 1 if random.randint(0, 1) == 0 else None
        #  Fruit trees sometimes lose fruit when the grow method is called, the chance is 1 in 5
        self._fruits -= 1 if random.randint(0, 4) == 0 else None
        return super().grow(sunlight, water)

    def get_ascii_fruits(self) -> str:
        result = ""
        if self._fruits % TREE_LEAVES_PER_ROW > 0:
            result += "." * (self._fruits % TREE_LEAVES_PER_ROW)
            result += "\n"
        for i in range(self._fruits // TREE_LEAVES_PER_ROW):
            result += "." * TREE_LEAVES_PER_ROW
            result += "\n"
        return result


class PineTree(Tree):
    """Represent a pine tree, e.g.
   *
  ***
 *****
*******
   |
   |    """

    def __init__(self):
        self._trunk_height = 1
        self._leave_rows = 2

    def get_ascii_leaves(self) -> str:
        """Return a string representation of the tree's leaves."""
        result = ""
        for i in range(self._leave_rows):
            result += " " * (self._leave_rows - i - 1) + \
                "*" * (2*i + 1) + " " * (self._leave_rows - i - 1)
            result += "\n"
        return result

    def get_ascii_trunk(self) -> str:
        """Return a string representation of the tree's trunk."""
        result = ""
        # the _ (underscore) variable is a convention for an unused variable
        for _ in range(self._trunk_height):
            result += " " * (self._leave_rows - 1) + "|" + \
                " " * (self._leave_rows - 1) + "\n"
        return result

    def grow(self, sunlight, water) -> None:
        """Grow a tree based on the sunlight and water parameters.
        Randomly grow the trunk height by a number between 0 and water.
        Randomly increase the leaves by a number between 0 and sunlight."""
        self._trunk_height += random.randint(0, water)
        self._leave_rows += 1 if random.randint(0, sunlight) > 2 else None
