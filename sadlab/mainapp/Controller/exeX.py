import os

def save_uploaded_file(file,name,upload_path='C:\Autoeval\sadlab\mainapp\Storage\Editor'):
    file_path = os.path.join(upload_path, name)
    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
def save_string_as_py_file(code_string, file_name='eval', save_path='C:\Autoeval\sadlab\mainapp\Storage\Editor'):
    if not file_name.endswith('.py'):
        file_name += '.py'
    file_path = os.path.join(save_path, file_name)
    with open(file_path, 'w',newline='') as file:
        file.write(code_string)

def delete_file(file_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\eval.py'):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except OSError as e:
        print(f"Error deleting file '{file_path}': {e}")


def read_test_cases(file_path='C:\Autoeval\sadlab\mainapp\Storage\ManualEva\TestCase.txt'):
    case=0
    input_list=[]
    output_list=[]
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines.append(None)
    for i in range(len(lines)):
        if(lines[i] is None):
            break
        if lines[i].startswith('Test Case-'):
            case+=1
        elif lines[i].startswith('Input:'):
            inp=lines[i].strip('Input:')
            i+=1
            while(lines[i].startswith('Output:')!=True):
                inp+=lines[i]
                i += 1
            input_list.append(inp)
        elif lines[i].startswith('Output:'):
            out=lines[i].strip('Output:')
            i+=1
            while(lines[i] is not None and lines[i].startswith('Test Case-')!=True):
                out+=lines[i]
                i+=1
            output_list.append(out)
    return case,input_list,output_list


def format_test_cases(test_data):
    formatted_cases = []
    for index, data in enumerate(test_data, start=1):
        formatted_case = (
            f"Test case-{index}: {data['error']} with Runtime {data['runtime']}")
        if data['output'] !='':
            formatted_case+=f" Output: {data['output'].strip()}"
        formatted_cases.append(formatted_case)
    return formatted_cases