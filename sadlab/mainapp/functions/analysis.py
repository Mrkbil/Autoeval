import os


def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            return line_count
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")


def count_loops(file_path):
    loop_counts = {'for': 0, 'while': 0, 'do': 0}

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            # Count occurrences of keywords
            loop_counts['for'] += line.count('for')
            loop_counts['while'] += line.count('while')
            loop_counts['do'] += line.count('do')

    return loop_counts

def analyze_files_in_directory(directory_path):
    results = []

    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)) and filename.endswith('.py'):
            file_path = os.path.join(directory_path, filename)

            line_count = count_lines(file_path)
            loop_count = count_loops(file_path)

            file_result = {
                'filename': filename,
                'line_count': line_count,
                'loop_count': loop_count
            }

            results.append(file_result)

    return results


def format_results(results):
    formatted_strings = []

    for result in results:
        formatted_string = f"Filename: {result['filename']}\n"
        formatted_string += f"Line Count: {result['line_count']}\n"
        formatted_string += f"For Loops: {result['loop_count']['for']}\n"
        formatted_string += f"While Loops: {result['loop_count']['while']}\n"
        formatted_string += f"Do-While Loops: {result['loop_count']['do']}\n"
        formatted_strings.append(formatted_string)

    return '\n'.join(formatted_strings)


def analyze_single_file(file_path):
    line_count = count_lines(file_path)
    loop_count = count_loops(file_path)

    formatted_result = f"Filename: {os.path.basename(file_path)}\n"
    formatted_result += f"Line Count: {line_count}\n"
    formatted_result += f"For Loops: {loop_count['for']}\n"
    formatted_result += f"While Loops: {loop_count['while']}\n"
    formatted_result += f"Do-While Loops: {loop_count['do']}\n"

    return formatted_result

#print(format_results(analyze_files_in_directory('G:/Autoeval/sadlab/mainapp/Zips/python')))
# print(analyze_single_file('G:/Autoeval/sadlab/mainapp/Zips/python/011202295.py'))
# path='codes/python/011202295.py'
# print(count_lines(path))
# print(count_lines(path))

python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
    'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
    'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]
java_keywords = [
    "abstract", "assert", "boolean", "break", "byte", "case", "catch", "char",
    "class", "const", "continue", "default", "do", "double", "else", "enum",
    "extends", "final", "finally", "float", "for", "if", "implements",
    "import", "instanceof", "int", "interface", "long", "native", "new",
    "package", "private", "protected", "public", "return", "short", "static",
    "strictfp", "super", "switch", "synchronized", "this", "throw", "throws",
    "transient", "try", "void", "volatile", "while"
];
cpp_keywords = [
    "alignas", "alignof", "and", "and_eq", "asm", "auto", "bitand", "bitor",
    "bool", "break", "case", "catch", "char", "char16_t", "char32_t", "class",
    "compl", "const", "constexpr", "const_cast", "continue", "decltype",
    "default", "delete", "do", "double", "dynamic_cast", "else", "enum",
    "explicit", "export", "extern", "false", "float", "for", "friend", "goto",
    "if", "inline", "int", "long", "mutable", "namespace", "new", "noexcept",
    "not", "not_eq", "nullptr", "operator", "or", "or_eq", "private",
    "protected", "public", "register", "reinterpret_cast", "return", "short",
    "signed", "sizeof", "static", "static_assert", "static_cast", "struct",
    "switch", "template", "this", "thread_local", "throw", "true", "try",
    "typedef", "typeid", "typename", "union", "unsigned", "using", "virtual",
    "void", "volatile", "wchar_t", "while", "xor", "xor_eq"
];
c_keywords = [
    "auto", "break", "case", "char", "const", "continue", "default", "do",
    "double", "else", "enum", "extern", "float", "for", "goto", "if", "int",
    "long", "register", "return", "short", "signed", "sizeof", "static",
    "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"
];



