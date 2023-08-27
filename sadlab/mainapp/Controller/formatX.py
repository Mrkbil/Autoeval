import os

def save_string_to_txt_file(content,file_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\Regx.txt'):
    try:
        with open(file_path, 'w') as txt_file:
            txt_file.write(content)
        print(f"String saved as '{file_path}'")
    except Exception as e:
        print(f"Error saving string as '{file_path}': {e}")
