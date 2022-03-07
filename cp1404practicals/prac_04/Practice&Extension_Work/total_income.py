"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    month_counts = int(input("How many months? "))

    for month in range(1, month_counts + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    print("\nIncome Report\n-------------")
    # total = 0
    # for month in range(1, month_counts + 1):
    #     income = incomes[month - 1]
    #     total += income
    #     print(
    #         "Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

    total = 0
    for month, income in enumerate(incomes):
        total += income
        print(
            f"Month {month+1:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()
