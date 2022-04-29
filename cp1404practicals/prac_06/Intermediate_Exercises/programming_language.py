from enum import Enum
from dataclasses import dataclass


class Typing(Enum):
    STATIC = "Static"
    DYNAMIC = "Dynamic"


@dataclass
class ProgrammingLanguage:
    name: str
    reflection: bool
    year: int
    typing: Typing

    @property
    def typing(self):
        return self._typing

    @typing.setter
    def typing(self, typing: Typing):
        if typing not in Typing:
            raise Exception
        self._typing = typing

    def __str__(self):
        return f"{self.name}, {self.typing.value} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """returns True/False if the programming language is dynamically typed or not"""
        return self.typing == Typing.DYNAMIC
