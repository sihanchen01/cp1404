import random


def main():
    number_of_scores = int(
        input("Enter the number of scores you want to generate: "))
    with open("results.txt", "a") as f:
        for _ in range(number_of_scores):
            random_score = random.randint(0, 100)
            f.writelines(f"{random_score:<3} is {get_comment(random_score)}\n")


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
