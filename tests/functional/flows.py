from kari.flows.flow import make_flow
from kari.flows.config import load_config

def test_that_we_can_make_flows():
    config = load_config('tests/files/generic_flow.yml')
    flow = make_flow(config)
    flow({})