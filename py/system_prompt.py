import json

# Load examples from the JSON file
def load_examples(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data['examples']

# Build the system prompt dynamically
def build_system_prompt(examples):
    task_description = """
    Task: Analyze the following prompt and:
    1. Identify words that are sexual or could lead to sexual content.
    2. Identify words that indicate an underage person.

    For each prompt, return all words that fit the above criteria.

    Format your response as:
    "[word1], [word2], [word3]"
    """
    
    examples_section = "Examples:\n"
    for i, example in enumerate(examples, 1):
        examples_section += f"{i}. Prompt: \"{example['prompt']}\"\n   Response: \"{example['response']}\"\n"
    
    return task_description + examples_section

