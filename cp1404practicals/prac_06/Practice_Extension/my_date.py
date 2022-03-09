from dataclasses import dataclass

DAYS_OF_EACH_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


@dataclass
class Date:
    day: int
    month: int
    year: int

    def __str__(self):
        return f"It is {self.month}/{self.day}/{self.year}."

    def add_days(self, n: int) -> None:
        while n + self.day > self.get_days_of_current_month():
            n = n + self.day - self.get_days_of_current_month()
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
            self.day = 0
        else:
            self.day += n

    def get_days_of_current_month(self) -> int:
        """return number of days in current month"""
        number_of_days = DAYS_OF_EACH_MONTH[self.month - 1]
        if self.month == 2 and self.year % 4 == 0:
            number_of_days += 1
        return number_of_days
