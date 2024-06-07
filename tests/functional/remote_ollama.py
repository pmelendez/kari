from kari.flows.flow import make_flow
from kari.flows.config import load_config

def test_ollama_flows():
    config = load_config('tests/files/ollama_test.yml')
    flow = make_flow(config)
    output = flow({})
    assert 'Caracas' in output