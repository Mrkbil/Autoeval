import os
import subprocess
import time


def save_uploaded_file(file,name,upload_path='C:\Autoeval\sadlab\mainapp\Storage\ManualEva'):
    file_path = os.path.join(upload_path, name)
    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def save_string_as_py_file(code_string, file_name='code', save_path='C:\Autoeval\sadlab\mainapp\Storage\ManualEva'):
    if not file_name.endswith('.py'):
        file_name += '.py'
    file_path = os.path.join(save_path, file_name)
    with open(file_path, 'w',newline='') as file:
        file.write(code_string)


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


def run_python_code(filename='C:\Autoeval\sadlab\mainapp\Storage\ManualEva\code.py',input_text='', expected_output=''):
    if not os.path.isfile(filename):
        return {
            'output': '',
            'runtime': 0,
            'error': 'File does not exist'
        }

    try:
        start_time = time.time()
        completed_process = subprocess.run(['python', filename], input=input_text, text=True, capture_output=True,timeout=5)
        end_time = time.time()
        runtime = end_time - start_time

        if completed_process.returncode != 0:
            return {
                'output': completed_process.stdout,
                'runtime': runtime,
                'error': f'Error occurred during execution : {completed_process.stderr}'
            }

        # Check if the output matches the expected output
        if completed_process.stdout.strip() == expected_output.strip():
            return {
                'output': completed_process.stdout,
                'runtime': runtime,
                'error': 'Passed'
            }
        else:
            return {
                'output': completed_process.stdout,
                'runtime': runtime,
                'error': 'Output does not match expected output'
            }
    except subprocess.TimeoutExpired:
        return {
            'output': '',
            'runtime': 0,
            'error': 'Timeout occurred during execution'
        }
    except subprocess.CalledProcessError as e:
        return {
            'output': '',
            'runtime': 0,
            'error': f'Error: {e}'
        }

def evaulate_func(file='C:\Autoeval\sadlab\mainapp\Storage\ManualEva\evaluation.py'):
    code_res=run_python_code('C:\Autoeval\sadlab\mainapp\Storage\ManualEva\code.py')
    inp=code_res['output']
    eve = {'output': code_res['output'],
           'runtime': code_res['runtime'],
           'error': code_res['error']}
    result=run_python_code(file,input_text=inp)
    if(result['output']=='1\n'):
        eve['error']='Passed'
    else:
        eve['error']=f"Failed { code_res['error'] }"

    res_lst=[]
    res_lst.append(eve)
    return res_lst

evaulate_func()