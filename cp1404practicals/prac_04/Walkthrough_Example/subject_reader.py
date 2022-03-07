"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    class_infos = get_data()
    for class_info in class_infos:
        print(
            f"{class_info[0]} is taught by {class_info[1]:12} and has {class_info[2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    class_infos = []
    for line in input_file:
        line.strip()
        line_list = line.split(",")
        line_list[2] = int(line_list[2])
        class_infos.append(line_list)
    input_file.close()
    return class_infos


main()
