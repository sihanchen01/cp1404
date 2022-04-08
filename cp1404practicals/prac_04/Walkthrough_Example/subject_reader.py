"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_infos = get_data()
    print_subjects(subject_infos)


def print_subjects(subject_infos):
    for subject_info in subject_infos:
        print(
            f"{subject_info[0]} is taught by {subject_info[1]:12} and has {subject_info[2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subject_infos = []
    for line in input_file:
        line.strip()
        line_list = line.split(",")
        line_list[2] = int(line_list[2])
        subject_infos.append(line_list)
    input_file.close()
    return subject_infos


main()
