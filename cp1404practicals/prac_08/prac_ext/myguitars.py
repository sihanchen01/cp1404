import csv
from guitar import Guitar


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

    # sorting guitars by year
    print("\nSorting by built year (oldest to newest): ")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    # create new guitars
    print("\nLet's make new guitars!")
    new_guitars = get_new_guitars()
    write_to_csv(new_guitars)


def get_new_guitars() -> list[Guitar]:
    """let user create new guitars, return the list of new guitars"""
    new_guitars = []
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        new_guitars.append(guitar)
        print(str(guitar) + " added.\n")
        name = input("Name: ").strip()
    return new_guitars


def write_to_csv(new_guitars: list[Guitar], filename: str = "myguitars.csv"):
    """write guitars to csv file"""
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        data = []
        for guitar in new_guitars:
            data.append([guitar.name, guitar.year, guitar.cost])
        writer.writerows(data)


main()
