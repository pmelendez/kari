
def make_command_step(config):
    def step(input, state):
        output = eval(config.command)
        state[f'step_{config["name"]}_output'] = output
        return output
    return step