import re
import os


def check_filenames_in_directory(directory_path, name_pattern=r'^\d{9}$', valid_extension='py'):
    incorrect_files = []
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            name, extension = filename.rsplit('.', 1)
            if re.match(name_pattern, name) and extension == valid_extension:
                continue
            else:
                incorrect_files.append(filename)
    return incorrect_files


def check_string_format(string, pattern=r'^\d{9,10}_\w+(?:\s\w+)*$'):
    if re.match(pattern, string):
        return True
    else:
        return False


def check_file_extension(filename, expected_format='zip'):
    file_extension = os.path.splitext(filename)[1]
    return file_extension.lower() == expected_format.lower()


text='011202295_Rakibul Islam'
print(check_string_format(text))
