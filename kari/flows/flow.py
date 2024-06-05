from kari.flows.factory import create_step

def make_flow(config):
    steps = []
    # Let's create the steps
    for step_config in config['steps']:
        step = create_step(step_config)
        steps.append(step)
    
    # We assume that there is a function called "make_{config['type']}_flow" and use it to create the flow
    # Let's call the function using a string
    flow_factory = f'make_{config["type"]}_flow'
    flow = globals()[flow_factory](config = config, steps= steps)

    return flow

def make_linear_flow(config, steps):
    def flow(state):
        output = ""
        for step in steps:
            output = step(output, state)
        return output
    return flow