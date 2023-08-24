import os
import difflib


def check_man_plagiarism(code_file_path):
    code_directory = os.path.dirname(code_file_path)
    with open(code_file_path, 'r') as code_file:
        code_content = code_file.read()
    files_in_directory = os.listdir(code_directory)
    similarity_list = []
    for file_name in files_in_directory:
        if file_name != os.path.basename(code_file_path) and file_name.endswith('.py'):
            other_file_path = os.path.join(code_directory, file_name)
            with open(other_file_path, 'r') as other_file:
                other_content = other_file.read()
            similarity_ratio = difflib.SequenceMatcher(None, code_content, other_content).ratio()
            formatted_similarity = format(similarity_ratio, ".2f")  # Format to 2 decimal places
            similarity_list.append((file_name, formatted_similarity))
    sorted_similarity = sorted(similarity_list, key=lambda x: float(x[1]), reverse=True)
    return sorted_similarity

def convert_to_line_separated(sorted_similarity):
    result_string = '\n'.join([f"{filename}: {similarity}" for filename, similarity in sorted_similarity])
    return result_string


def check_plagiarism(code1, code2):
    lines1 = code1.splitlines()
    lines2 = code2.splitlines()
    diff = difflib.unified_diff(lines1, lines2)
    num_differences = 0
    for line in diff:
        num_differences += 1
    similarity = 1 - (num_differences / max(len(lines1), len(lines2)))
    return similarity




def read_code(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def preprocess_code(code):
    # Implement your preprocessing steps here (e.g., removing comments, formatting)
    return code


def compare_similarity(code1, code2):
    # Compare the similarity of two preprocessed code snippets
    sm = difflib.SequenceMatcher(None, code1, code2)
    return sm.ratio()


def check_plagiarism_all(directory_path):
    filepaths = [os.path.join(directory_path, filename) for filename in os.listdir(directory_path)]

    results = []
    for i, filepath1 in enumerate(filepaths):
        for j, filepath2 in enumerate(filepaths):
            if i < j:
                code1 = preprocess_code(read_code(filepath1))
                code2 = preprocess_code(read_code(filepath2))
                similarity = compare_similarity(code1, code2)
                results.append({'filename1': os.path.basename(filepath1), 'filename2': os.path.basename(filepath2),
                                'similarity': similarity})

    results.sort(key=lambda x: x['similarity'], reverse=True)
    return results

def format_results(results):
    formatted_results = "\n".join([f"{result['filename1']} and {result['filename2']} : {result['similarity']:.2f}" for result in results])
    return formatted_results

code1 = '''
#include <stdio.h>

int is_prime(int num) {
    if (num <= 1) {
        return 0;
    }

    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0;
        }
    }

    return 1;
}

void print_primes(int N) {
    printf("Prime numbers between 0 and %d:\n", N);
    
    for (int i = 2; i <= N; i++) {
        if (is_prime(i)) {
            printf("%d ", i);
        }
    }

    printf("\n");
}

int main() {
    int N;

    printf("Enter a number: ");
    scanf("%d", &N);

    print_primes(N);

    return 0;
}

'''

code2 = '''
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }

    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

void printPrimes(int limit) {
    printf("Prime numbers between 0 and %d:\n", limit);

    for (int num = 2; num <= limit; num++) {
        if (isPrime(num)) {
            printf("%d ", num);
        }
    }

    printf("\n");
}

int main() {
    int userInput;

    printf("Enter a number: ");
    scanf("%d", &userInput);

    printPrimes(userInput);

    return 0;
}

'''

# similarity_score = check_plagiarism(code1, code2)
# print(f"Similarity score: {similarity_score}")


# for result in plagiarism_results:
#     print(f"Similarity between {result[0]} and {result[1]}: {result[2]}")