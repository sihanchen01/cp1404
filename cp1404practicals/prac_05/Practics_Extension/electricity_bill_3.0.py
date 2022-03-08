import random

tariffs = {"TARIFF_11": 0.244618, "TARIFF_31": 0.136928}


def add_random_tariff(tariffs: dict):
    tariff = "TARIFF_" + str(random.randint(1, 50))
    while tariff in tariffs:
        tariff = "TARIFF_" + str(random.randint(1, 50))
    value = round(random.uniform(0.1, 0.5), 6)
    tariffs[tariff] = value


# use random to add 3 more tariffs to the test
for _ in range(3):
    add_random_tariff(tariffs)

print("Electricity bill estimator 3.0")
tariff_options = [k.split("_")[1] for k in tariffs.keys()]
tariff = "TARIFF_" + input(f"Which tariff? {' or '.join(tariff_options)}: ")
while tariff not in tariffs:
    print("Invalid input, try again!")
    tariff = "TARIFF_" + \
        input(f"Which tariff? {' or '.join(tariff_options)}: ")

daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

price = tariffs[tariff]
bill = price * daily_use * billing_days

print(f"Estimated bill: {bill:.2f}")
