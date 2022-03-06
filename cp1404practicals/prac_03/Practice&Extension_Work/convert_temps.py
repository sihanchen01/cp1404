
def main():
    with open("temps_input.txt", "r") as rf:
        fahrenheit_temps = rf.readlines()

    with open("temps_output.txt", "w") as wf:
        for fahrenheit in fahrenheit_temps:
            celsius = fahrenheit_to_celsius(float(fahrenheit))
            wf.write(f"{fahrenheit[:-1]:<7} F -> {celsius:<7.2f} C\n")


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    main()
