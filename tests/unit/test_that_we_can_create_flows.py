from kari.flows.config import load_config
from kari.flows.flow import make_flow
config_path = "tests/functional/files/generic_flow.yml"

def test_that_we_read_flows_config_files():
    config = load_config(config_path)

    assert config['type'] == 'linear'
    assert len(config['steps']) == 2
    assert config['steps'][0]['type'] == 'command'
    assert config['steps'][0]['name'] == 'step1'
    assert config['steps'][0]['command'] == 'print("My Step")'

def test_that_we_create_a_flow():
    config = load_config(config_path)
    flow = make_flow(config)
    print(flow)
    # Assert that flow is a function
    assert callable(flow)
    output = flow({})
