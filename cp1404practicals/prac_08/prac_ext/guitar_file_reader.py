import csv
from guitar import Guitar
from collections import namedtuple


def main():
    guitars = []
    with open("guitars.csv", "r") as f:
        # skip the first line, headings
        f.readline()
        for line in f:
            name, year, cost = line.strip().split(',')
            guitar = Guitar(name=name, year=int(year), cost=float(cost))
            guitars.append(guitar)

    for guitar in guitars:
        print(guitar)

    print("\nSorting by built year (oldest to newest): ")
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()


def using_csv_nametuple():
    Guitar = namedtuple("Guitar", "name, year, cost")
    with open("guitars.csv", "r") as f:
        f.readline()
        for guitar in map(Guitar._make, csv.reader(f)):
            print(guitar.name, "was build in ",
                  guitar.year, "cost", guitar.cost)
            print(repr(guitar))


# using_csv_nametuple()
