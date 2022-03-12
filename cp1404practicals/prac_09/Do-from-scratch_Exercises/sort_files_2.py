import os
import shutil


def categorize():
    os.chdir('FilesToSort2')
    file_to_folder = {}
    for filename in os.listdir("."):
        ext = filename[filename.rfind('.') + 1:]
        if ext not in file_to_folder.keys():
            user_input = input(
                f"What category would you like to sort {ext} files into? ")
            try:
                os.mkdir(user_input)
            except FileExistsError:
                pass
            file_to_folder[ext] = user_input
        shutil.move(filename, file_to_folder[ext] + '/' + filename)


categorize()
