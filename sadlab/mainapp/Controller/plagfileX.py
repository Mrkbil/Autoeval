import os
import zipfile
import shutil


def unzip_uploaded_zip(zip_file, target_directory='C:\Autoeval\sadlab\mainapp\Storage\Editor\CheckPlag'):
    os.makedirs(target_directory, exist_ok=True)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_directory)


def delete_directory(directory_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\CheckPlag'):
    try:
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting directory '{directory_path}': {e}")

delete_directory()