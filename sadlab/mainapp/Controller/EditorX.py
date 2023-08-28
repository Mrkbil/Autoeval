import os


def get_all_file_names(directory_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\CheckCodes'):
    try:
        file_names = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return file_names
    except Exception as e:
        print(f"Error getting file names in directory '{directory_path}': {e}")
        return []

def getcode(name,file_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\CheckCodes/'):
    try:
        with open(file_path+name, 'r') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

def check_eval(file_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\eval.py'):
    return os.path.exists(file_path)

def check_plagpath(file_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\plagpath.txt'):
    return os.path.exists(file_path)

def read_test_cases(file_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\TestCase.txt'):
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


def get_all_file_paths(directory_path='C:\Autoeval\sadlab\mainapp\Storage\Editor\CheckCodes/'):
    try:
        file_paths = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        return file_paths
    except Exception as e:
        print(f"Error getting file paths in directory '{directory_path}': {e}")
        return []


def format_output_results(output_results):
    formatted_output = []

    for result in output_results:
        formatted_output.append(f"Output: {result['output'].strip()}, Runtime: {result['runtime']:.2f}, Error: {result['error']}")

    return '\n'.join(formatted_output)