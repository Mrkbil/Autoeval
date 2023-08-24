import json

def save_dict_to_json(data, filename):
    filename=f'G:/Autoeval/sadlab/mainapp/Metadata/{filename}'
    json_data = json.dumps(data, indent=4)
    with open(filename, 'w') as json_file:
        json_file.write(json_data)

def load_dict_from_json(filename):
    filename = f'G:/Autoeval/sadlab/mainapp/Metadata/{filename}'
    with open(filename, 'r') as json_file:
        json_data = json_file.read()
    retrieved_data = json.loads(json_data)
    return retrieved_data
