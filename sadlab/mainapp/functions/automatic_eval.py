import os
from .execute import *
#from execute import *


# returns all the files with a specific extension
def get_files_by_extension(directory, extension):
    file_list = []
    if not os.path.exists(directory):
        return file_list
    for filename in os.listdir(directory):
        if filename.endswith("." + extension):
            file_list.append(directory+'/'+filename)

    return file_list



def run_file_list(directory, extension, input='', output=''):
    filelist = get_files_by_extension(directory, extension)
    output_list = []
    if extension == 'py':
        for file in filelist:
            filename = os.path.basename(file)  # Get the filename without path
            res = run_python_code(file, input, output)
            output_list.append({'filename': filename, 'result': res})
    elif extension == 'java':
        for file in filelist:
            filename = os.path.basename(file)  # Get the filename without path
            res = run_java_code(file, input, output)
            output_list.append({'filename': filename, 'result': res})
    elif extension == 'cpp':
        for file in filelist:
            filename = os.path.basename(file)  # Get the filename without path
            res = run_cpp_code(file, input, output)
            output_list.append({'filename': filename, 'result': res})
    elif extension == 'c':
        for file in filelist:
            filename = os.path.basename(file)  # Get the filename without path
            res = run_c_code(file, input, output)
            output_list.append({'filename': filename, 'result': res})
    return output_list


def format_output_to_string(result_list):
    output_lines = []
    for entry in result_list:
        output_lines.append(f"{entry['filename']}:")
        result_dict = entry.get('result', {})
        if 'output' in result_dict:
            output_lines.append(f"output: {result_dict['output'].strip()}")
        if 'runtime' in result_dict:
            output_lines.append(f"runtime: {result_dict['runtime']:.17f}")
        if 'error' in result_dict:
            output_lines.append(f"error: {result_dict['error']}")
    formatted_string = '\n'.join(output_lines)
    return formatted_string

#print(run_file_list('G:/Autoeval/sadlab/mainapp/Zips/python/','py','30\n30\n30\n','90.0\n'))
# result=run_file_list('G:/Autoeval/sadlab/mainapp/Zips/python','py')
#
# print(format_output_to_string(result))
