import difflib
import os
import zipfile


def save_uploaded_file(file,upload_path='C:\Autoeval\sadlab\mainapp\Storage\Plagiarism'):
    file_path = os.path.join(upload_path, 'code.py')
    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def unzip_uploaded_zip(zip_file, target_directory='C:\Autoeval\sadlab\mainapp\Storage\Plagiarism\CheckCodes'):
    os.makedirs(target_directory, exist_ok=True)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(target_directory)
def save_string_as_py_file(code_string, file_name='code', save_path='C:\Autoeval\sadlab\mainapp\Storage\Plagiarism'):
    if not file_name.endswith('.py'):
        file_name += '.py'
    file_path = os.path.join(save_path, file_name)
    with open(file_path, 'w',newline='') as file:
        file.write(code_string)

def read_file(file_path='C:\Autoeval\sadlab\mainapp\Storage\Plagiarism\code.py'):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None

def check_plagiarism(code_string, directory_path='C:\Autoeval\sadlab\mainapp\Storage\Plagiarism\CheckCodes'):
    results = []
    if not os.path.exists(directory_path):
        return results
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                file_content = file.read()
                similarity_ratio = difflib.SequenceMatcher(None, code_string, file_content).ratio()
                result = {
                    'filename': filename,
                    'similarity': similarity_ratio
                }
                results.append(result)
                sorted_results = sorted(results, key=lambda x: x['similarity'], reverse=True)

    return sorted_results

def format_results(sorted_results):
    formatted_results = []
    for result in sorted_results:
        filename = result['filename']
        similarity = result['similarity']
        formatted_result = f"{filename} similarity found: {similarity:.2f}"
        formatted_results.append(formatted_result)
    return formatted_results


