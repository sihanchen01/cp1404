from guitar import Guitar


def main():
    print("My guitars!")
    guitars = []
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        print(str(guitar) + " added.")
        guitars.append(guitar)
        print()
        name = input("Name: ").strip()

    print()
    print("These are my guitars:")
    guitars.sort(key=lambda guitar: guitar.cost, reverse=True)
    max_name_len = max([len(g.name) for g in guitars])
    max_cost_len = max([len(f"{g.cost:,.2f}") for g in guitars])
    for i in range(len(guitars)):
        name_ = guitars[i].name
        year_ = guitars[i].year
        cost_ = guitars[i].cost
        is_vintage = guitars[i].is_vintage()
        output = f"Guitar {i + 1}:  {name_:>{max_name_len}} ({year_}), worth $ {cost_:>{max_cost_len},.2f}"
        suffix = " (vintage)" if is_vintage else ""
        print(output + suffix)


if __name__ == "__main__":
    main()
