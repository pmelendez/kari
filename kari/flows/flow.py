from kari.flows.factory import create_step

def make_flows(config):
    flows = []
    for flow_config in config['flows']:
        steps = []
        # Let's create the steps
        for step_config in flow_config['steps']:
            step = create_step(step_config)
            steps.append(step)
        
        # We assume that there is a function called "make_{config['type']}_flow" and use it to create the flow
        # Let's call the function using a string
        flow_factory = f'make_{flow_config["type"]}_flow'
        flows.append(globals()[flow_factory](config = flow_config, steps= steps))

    return flows

def make_linear_flow(config, steps):
    def flow(state):
        output = ""
        for step in steps:
            output = step(output, state)
        return output
    return flow