from dataclasses import dataclass, field
from datetime import date


@dataclass(order=True)
class Guitar:
    sort_index: int = field(init=False)
    name: str = ""
    year: int = 0
    cost: float = 0.0

    def __str__(self) -> None:
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __post_init__(self):
        self.sort_index = self.year

    def get_age(self) -> int:
        """returns how old the guitar is in years"""
        return date.today().year - self.year

    def is_vintage(self) -> bool:
        """returns True if the guitar is 50 or more years old, False otherwise"""
        return self.get_age() >= 50
