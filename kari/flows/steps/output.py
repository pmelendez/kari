def make_output_step(config):
    def step(input, state):
        
        # Let's write the input into a file
        output = input
        with open(config["output_path"], "w") as f:
            f.write(output)
            f.close()

        state[f'step_{config["name"]}_output'] = output
        return output
    return step