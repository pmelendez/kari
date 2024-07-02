from kari.flows.config import load_config
from kari.flows.flow import make_flows
config_path = "tests/files/generic_flow.yml"

def test_that_we_read_flows_config_files():
    config = load_config(config_path)['flows'][0]
    
    assert config['type'] == 'linear'
    assert len(config['steps']) == 4
    assert config['steps'][0]['type'] == 'command'
    assert config['steps'][0]['name'] == 'step1'
    assert config['steps'][0]['command'] == 'print("My Step")'

def test_that_we_create_a_flow():
    config = load_config(config_path)
    flow = make_flows(config)

    # Assert that flow is a function
    assert callable(flow[0])
    output = flow[0]({})
