import os

def save_uploaded_file(file,upload_path='C:\Autoeval\sadlab\mainapp\Storage\Analysis'):
    file_path = os.path.join(upload_path, 'code.py')
    with open(file_path, 'wb') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

def save_string_as_py_file(code_string, file_name='code', save_path='C:\Autoeval\sadlab\mainapp\Storage\Analysis'):
    if not file_name.endswith('.py'):
        file_name += '.py'
    file_path = os.path.join(save_path, file_name)
    with open(file_path, 'w',newline='') as file:
        file.write(code_string)

def read_file(file_path='C:\Autoeval\sadlab\mainapp\Storage\Analysis\code.py'):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return None

def analyze_syntax(code):
    analysis = {
        'syntax_valid': False,
        'syntax_error_message': None
    }

    try:
        ast.parse(code)
        analysis['syntax_valid'] = True
    except SyntaxError as e:
        analysis['syntax_error_message'] = str(e)

    return analysis


import ast


def count_lines_and_entities(code):
    lines = code.split('\n')

    try:
        code_tree = ast.parse(code)
        class_count = len([node for node in ast.walk(code_tree) if isinstance(node, ast.ClassDef)])
        function_count = len([node for node in ast.walk(code_tree) if isinstance(node, ast.FunctionDef)])
    except SyntaxError:
        class_count = 0
        function_count = 0

    result = {
        'lines': len(lines),
        'class_count': class_count,
        'function_count': function_count
    }

    return result


def count_loops_and_conditionals(code):
    loop_keywords = ['for', 'while']
    conditional_keywords = ['if']

    loop_count = sum(code.count(keyword) for keyword in loop_keywords)
    conditional_count = sum(code.count(keyword) for keyword in conditional_keywords)
    do_while_count = code.count('do:')
    for_count = code.count('for')
    while_count = code.count('while')

    result = {
        'loop_count': loop_count,
        'conditional_count': conditional_count,
        'do_while_count': do_while_count,
        'for_count': for_count,
        'while_count': while_count
    }

    return result


import ast


def count_variables(code):
    try:
        code_tree = ast.parse(code)

        all_variables = set()

        for node in ast.walk(code_tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        all_variables.add(target.id)

    except SyntaxError:
        all_variables = set()

    result = {
        'num_variables': len(all_variables),
        'variables': list(all_variables)
    }

    return result


import keyword


def count_python_keywords(code):
    code_words = code.split()
    keyword_count = {kw: 0 for kw in keyword.kwlist}

    for word in code_words:
        if word in keyword.kwlist:
            keyword_count[word] += 1

    return keyword_count



def analyze_code(code):
    syntax_analysis = analyze_syntax(code)
    lines_and_entities = count_lines_and_entities(code)
    loops_and_conditionals = count_loops_and_conditionals(code)
    variables_analysis = count_variables(code)
    python_keywords_count = count_python_keywords(code)

    complete_analysis = {
        'syntax_analysis': syntax_analysis,
        'lines_and_entities': lines_and_entities,
        'loops_and_conditionals': loops_and_conditionals,
        'variables_analysis': variables_analysis,
        'python_keywords_count': python_keywords_count
    }

    return complete_analysis

def format_analysis_result(analysis_result):
    syntax_analysis = analysis_result['syntax_analysis']
    lines_and_entities = analysis_result['lines_and_entities']
    loops_and_conditionals = analysis_result['loops_and_conditionals']
    variables_analysis = analysis_result['variables_analysis']
    python_keywords_count = analysis_result['python_keywords_count']

    presentation = f"Syntax Analysis:\n"
    presentation += f"Syntax Valid: {syntax_analysis['syntax_valid']}\n"
    if not syntax_analysis['syntax_valid']:
        presentation += f"Syntax Error: {syntax_analysis['syntax_error_message']}\n"

    presentation += f"\nLines and Entities Analysis:\n"
    presentation += f"Total Lines: {lines_and_entities['lines']}\n"
    presentation += f"Class Count: {lines_and_entities['class_count']}\n"
    presentation += f"Function Count: {lines_and_entities['function_count']}\n"

    presentation += f"\nLoops and Conditionals Analysis:\n"
    presentation += f"Loop Count: {loops_and_conditionals['loop_count']}\n"
    presentation += f"Conditional Count: {loops_and_conditionals['conditional_count']}\n"
    presentation += f"Do-While Count: {loops_and_conditionals['do_while_count']}\n"
    presentation += f"For Count: {loops_and_conditionals['for_count']}\n"
    presentation += f"While Count: {loops_and_conditionals['while_count']}\n"

    presentation += f"\nVariables Analysis:\n"
    presentation += f"Number of Variables: {variables_analysis['num_variables']}\n"
    presentation += f"Variables: {', '.join(variables_analysis['variables'])}\n"

    presentation += f"\nPython Keywords Count:\n"
    used_keywords = {keyword: count for keyword, count in python_keywords_count.items() if count > 0}
    presentation += "\n".join([f"{keyword}: {count}" for keyword, count in used_keywords.items()])

    return presentation

