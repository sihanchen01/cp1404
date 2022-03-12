import os


def find_missing_copyright():
    os.chdir("Lyrics")
    no_copyright_files = []
    for directory_name, _, filenames in os.walk("."):
        for filename in filenames:
            with open(os.path.join(directory_name, filename), 'r') as rf:
                has_copyright = False
                for line in rf.readlines():
                    if line.startswith(".i"):
                        has_copyright = True
                        break
                if not has_copyright:
                    no_copyright_files.append([filename, directory_name])

    print("The following files are missing copyright information:")
    fname_max_width = max(len(f[0]) for f in no_copyright_files)
    for no_copyright_file in no_copyright_files:
        name, directory = no_copyright_file
        print(
            f"Name: {name:{fname_max_width}}\t-\tDirectory: {directory}")


find_missing_copyright()
