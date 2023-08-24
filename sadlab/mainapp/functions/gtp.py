import openai

def grade_assignment(assignment):
  api_key = "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"
  client = openai.Client(api_key=api_key)
  prompt = f"Grade the following assignment: {assignment}"
  completion = client.completions.create(prompt=prompt)
  grade = completion["choices"][0]["text"].strip()
  grade = int(grade)
  return grade

code='print(hello)'

print(grade_assignment(code))