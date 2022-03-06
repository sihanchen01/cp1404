# print("Electricity bill estimator")
# price = int(input("Enter cents per kWh: "))
# daily_use = float(input("Enter daily use in kWh: "))
# billing_days = int(input("Enter number of billing days: "))

# bill = price * daily_use * billing_days / 100

# print(f"Estimated bill: {bill:.2f}")

# =============================================================

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electricity bill estimator 2.0")
tariff = input("Which tariff? 11 or 31: ")
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

price = TARIFF_11 if tariff == "11" else TARIFF_31
bill = price * daily_use * billing_days

print(f"Estimated bill: {bill:.2f}")
