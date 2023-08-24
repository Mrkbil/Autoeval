import os
def get_filenames_in_directory(directory_path):
    try:
        items = os.listdir(directory_path)
        filenames = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
        return filenames
    except OSError as e:
        print(f"Error: {e}")
        return []

