from os import path
from ollama import Client

def make_llm_ollama_step(config):
    host = 'localhost' if 'host' not in config else config['host']
    port =  11434 if 'port' not in config else config['port']
    protocol = 'http' if 'protocol' not in config else config['protocol']
    model = 'llama3' if 'model' not in config else config['model']

    prompt_template = config['prompt_template']

    #Let's detect if prompt_template is a string or a path to a file
    if path.isfile(prompt_template):
        with open(prompt_template, 'r') as f:
            prompt_template = f.read()
    
    client = Client(host = f'{protocol}://{host}:{port}')

    def step(input, state):
        # Merge the state with the input
                
        # Apply the prompt template to the input
        prompt = prompt_template.format(input=input, **state)
        output = client.chat(model, messages=[{ 'role': 'user', 'content': prompt}])
        return output["message"]["content"]
    return step