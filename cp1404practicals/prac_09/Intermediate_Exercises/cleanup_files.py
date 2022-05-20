import shutil
import os

from matplotlib.cbook import index_of


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    os.chdir('Lyrics/Christmas')

    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        shutil.move(filename, 'temp/' + new_name)


def convert_camelcase(words: str) -> str:
    """convert camelcase word with space."""
    new_word_list = []
    for word in words.split():
        if sum(1 for c in word[1:] if c.isupper()) > 0:
            new_word = word[0]
            for c in word[1:]:
                if c.isupper():
                    new_word += " "
                new_word += c
            new_word_list.append(new_word)
        else:
            new_word_list.append(word)
    return " ".join(new_word_list)


def get_fixed_filename(filename: str) -> str:
    """Return a 'fixed' version of filename."""
    name = filename[:filename.rfind('.')]
    # check if parenthese exist
    index_of_parenthese = name.find("(")
    if index_of_parenthese != -1:
        name_first_part = name[:index_of_parenthese]
        name_second_part = name[index_of_parenthese:]
        # if word is a single word and from the second character, if uppercase letter exist (camelword), reformat
        new_name = convert_camelcase(name_first_part) + " " + name_second_part
    else:
        new_name = convert_camelcase(name)
    new_name = new_name.title().replace(" ", "_")
    return new_name + '.txt'


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            old_path = os.path.join(directory_name, filename)
            new_path = os.path.join(directory_name, new_name)
            os.rename(old_path, new_path)


# main()
demo_walk()

# testlist = ['Away In A Manger.txt', 'SilentNight.txt',
#             'O little town of bethlehem.TXT', 'ItIsWell (oh my soul).txt', 'test.txt', 'test2Test.txt']

# for t in testlist:
#     print(get_fixed_filename(t))
