import os


def get_file_name(file_dict):
    for key in file_dict.keys():
        return key

def file_exists(path):
    if os.isfile(path):
        return True
    return False

