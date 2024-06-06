def make_append_all_outputs_step(config):
    def step(input, state):
        output = ""
        for k in state:
            if k.startswith('step_') and k.endswith('_output'):
                output = f'{output}{state[k]}\n'
        
        state[f'step_{config["name"]}_output'] = output
        return output
    return step