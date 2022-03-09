from dataclasses import dataclass, field


@dataclass(order=True)
class People:
    sort_index: int = field(init=False, repr=False)
    first_name: str
    last_name: str
    age: int

    def __post_init__(self):
        self.sort_index = self.age
