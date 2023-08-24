import subprocess
import time
import os.path


def run_python_code(filename,input_text='30\n30\n30\n', expected_output='90.0\n'):
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
                'error': 'Passed with 100% Grade'
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


def run_java_code(filename, input_text='', expected_output=''):
    if not os.path.isfile(filename):
        return {
            'output': '',
            'runtime': 0,
            'error': 'File does not exist'
        }

    try:
        start_time = time.time()
        completed_process = subprocess.run(['java', filename], input=input_text, text=True, capture_output=True, timeout=5)
        end_time = time.time()
        runtime = end_time - start_time

        if completed_process.returncode != 0:
            return {
                'output': completed_process.stdout,
                'runtime': runtime,
                'error': f'Error occurred during execution: {completed_process.stderr}'
            }

        # Check if the output matches the expected output
        if completed_process.stdout.strip() == expected_output.strip():
            return {
                'output': completed_process.stdout,
                'runtime': runtime
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

def run_c_code(filename, input_text='', expected_output=''):
    if not os.path.isfile(filename):
        return {
            'output': '',
            'runtime': 0,
            'error': 'File does not exist'
        }

    try:
        start_time = time.time()
        completed_process = subprocess.run(['gcc', filename], capture_output=True, text=True, timeout=5)
        if completed_process.returncode != 0:
            return {
                'output': completed_process.stdout,
                'runtime': 0,
                'error': f'Compilation error: {completed_process.stderr}'
            }

        compiled_filename = os.path.splitext(filename)[0]
        completed_process = subprocess.run([compiled_filename], input=input_text, capture_output=True, text=True, timeout=5)
        end_time = time.time()
        runtime = end_time - start_time

        if completed_process.returncode != 0:
            return {
                'output': completed_process.stdout,
                'runtime': runtime,
                'error': f'Error occurred during execution: {completed_process.stderr}'
            }

        # Check if the output matches the expected output
        if completed_process.stdout.strip() == expected_output.strip():
            return {
                'output': completed_process.stdout,
                'runtime': runtime
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

def run_cpp_code(filename, input_text='', expected_output=''):
    if not os.path.isfile(filename):
        return {
            'output': '',
            'runtime': 0,
            'error': 'File does not exist'
        }

    try:
        start_time = time.time()
        completed_process = subprocess.run(['g++', filename, '-o', 'output'], capture_output=True, text=True, timeout=5)
        if completed_process.returncode != 0:
            return {
                'output': completed_process.stdout,
                'runtime': 0,
                'error': f'Compilation error: {completed_process.stderr}'
            }

        completed_process = subprocess.run(['./output'], input=input_text, capture_output=True, text=True, timeout=5)
        end_time = time.time()
        runtime = end_time - start_time

        if completed_process.returncode != 0:
            return {
                'output': completed_process.stdout,
                'runtime': runtime,
                'error': f'Error occurred during execution: {completed_process.stderr}'
            }

        # Check if the output matches the expected output
        if completed_process.stdout.strip() == expected_output.strip():
            return {
                'output': completed_process.stdout,
                'runtime': runtime
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



