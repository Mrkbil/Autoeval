import os
import zipfile


def unzip_uploaded_zip(zip_file, target_directory='C:\Autoeval\sadlab\mainapp\Storage\Editor\CheckCodes'):
    os.makedirs(target_directory, exist_ok=True)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_directory)