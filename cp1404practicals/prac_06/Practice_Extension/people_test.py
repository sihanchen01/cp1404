from people import People
import csv

FILENAME = "name_to_age.csv"


def get_list_of_people() -> list[People]:
    list_of_people = []
    first_name = input("First name: ").strip()
    while first_name != "":
        last_name = input("Last name: ").strip()
        age = int(input("Age: "))
        list_of_people.append(People(first_name, last_name, age))
        print()
        first_name = input("First name: ").strip()
    return list_of_people


def write_csv(filename, list_of_people: list[People]) -> None:
    list_of_people.sort(reverse=True)

    header = ["First Name", "Last Name", "Age"]
    with open(filename, "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)

        data = []
        for people in list_of_people:
            data.append([people.first_name, people.last_name, people.age])

        writer.writerows(data)


def main():
    list_of_people = get_list_of_people()
    write_csv(FILENAME, list_of_people)


if __name__ == "__main__":
    main()
