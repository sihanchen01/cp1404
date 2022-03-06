"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    print(get_comment(score))
    random_score = random.uniform(0, 100)
    print(
        f"The comment for random score {random_score:.2f} is '{get_comment(random_score)}'")


def get_comment(score: float) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


if __name__ == "__main__":
    main()
