from kari.flows.flow import make_flows
from kari.flows.config import load_config

def test_ollama_flows():
    config = load_config('tests/files/ollama_flow.yml')
    flows = make_flows(config)
    output = flows[0]({})
    assert 'Caracas' in output

    output = flows[1]({})
    assert 'Wozniak' in output