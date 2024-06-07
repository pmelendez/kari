from pathlib import Path
def make_output_step(config):
    def step(input, state):
        
        # Let's write the input into a file
        output = input

        # Check subdirectories in the output path and create them if they don't exist
        output_path = Path(config["output_path"])
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(config["output_path"], "w") as f:
            f.write(output)
            f.close()

        state[f'step_{config["name"]}_output'] = output
        return output
    return step