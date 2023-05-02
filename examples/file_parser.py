import glob


def get_list_of_text_files(dir_path, extension):
    return glob.glob(dir_path + "*." + extension)

