import openai

openai.api_key = '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'

def generate_chat_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n = 1,
        stop=None,
    )
    return response.choices[0].text.strip()


def generate_code_explanation_prompt(code_path):
    with open(code_path, 'r') as file:
        code_content = file.read()
    prompt = f"Please provide an explanation for the following code:\n{code_content}\n in 100 words."
    return prompt



print(generate_code_explanation_prompt('codes/python/011202295.py'))
#generate_chat_response("hi")
