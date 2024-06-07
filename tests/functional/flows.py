from kari.flows.flow import make_flows
from kari.flows.config import load_config

def test_that_we_can_make_flows():
    config = load_config('tests/files/generic_flow.yml')
    flows = make_flows(config)
    for flow in flows:
        flow({})