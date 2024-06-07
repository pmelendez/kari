from ollama import Client

def make_llm_ollama_step(config):
    promp_template = config['prompt_template']
    host = 'localhost' if 'host' not in config else config['host']
    port =  11434 if 'port' not in config else config['port']
    protocol = 'http' if 'protocol' not in config else config['protocol']
    model = 'llama3' if 'model' not in config else config['model']
    
    client = Client(host = f'{protocol}://{host}:{port}')

    def step(input, state):
        # Merge the state with the input
                
        # Apply the prompt template to the input
        prompt = promp_template.format(input=input, **state)
        output = client.chat(model, messages=[{ 'role': 'user', 'content': prompt}])
        return output["message"]["content"]
    return step