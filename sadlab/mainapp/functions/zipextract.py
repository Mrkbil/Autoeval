import os
import zipfile
import rarfile

def extract_archive_file(archive_file):
    base_dir = os.path.dirname(archive_file)
    base_name = os.path.splitext(os.path.basename(archive_file))[0]
    extraction_location = os.path.join(base_dir, base_name)
    if archive_file.endswith('.zip'):
        with zipfile.ZipFile(archive_file, 'r') as zip_ref:
            zip_ref.extractall(extraction_location)
        print(f"Extracted {archive_file} successfully.")
    elif archive_file.endswith('.rar'):
        with rarfile.RarFile(archive_file, 'r') as rar_ref:
            rar_ref.extractall(extraction_location)
        print(f"Extracted {archive_file} successfully.")
    return extraction_location

