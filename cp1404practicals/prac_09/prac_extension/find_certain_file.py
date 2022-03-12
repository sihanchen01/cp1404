import os


def find_with_size(target_size: int, over: bool = True) -> list[list[str, str]]:
    """find file over or within a certain size, return list of list of filename and directories"""
    target_files = []
    for directory_name, _, filenames in os.walk("."):
        for filename in filenames:
            file_size = os.stat(os.join(directory_name, filename)).st_size
            if over:
                target_files.append(
                    [filename, directory_name]) if file_size > target_size else None
            else:
                target_files.append(
                    [filename, directory_name]) if file_size <= target_size else None
    return target_files


def find_with_ext(target_ext: str) -> list[list[str, str]]:
    """find file with a certain extension, return list of list of filename and directories"""
    target_files = []
    for directory_name, _, filenames in os.walk("."):
        for filename in filenames:
            file_ext = filename[filename.rfind('.') + 1:]
            target_files.append(
                [filename, directory_name]) if file_ext == target_ext else None
    return target_files


def find_with_text(target_text: str) -> list[list[str, str]]:
    """find file containing certain text, return list of list of filename and directories"""
    target_files = []
    for directory_name, _, filenames in os.walk("."):
        for filename in filenames:
            has_target_text = False
            with open(os.path.join(directory_name, filename), 'r') as rf:
                for line in rf.readlines():
                    if line.find(target_text) != -1:
                        has_target_text = True
                        break
            target_files.append(
                [filename, directory_name]) if has_target_text else None
    return target_files
