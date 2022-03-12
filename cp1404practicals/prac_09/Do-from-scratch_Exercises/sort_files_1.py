import os
import shutil


def categorize():
    os.chdir('FilesToSort')
    already_created = []
    for filename in os.listdir("."):
        ext = filename[filename.rfind('.') + 1:]
        if ext not in already_created:
            try:
                os.mkdir(ext)
            except FileExistsError:
                pass
            already_created.append(ext)
        shutil.move(filename, f'{ext}/' + filename)


categorize()
