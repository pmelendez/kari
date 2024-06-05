import importlib
import sys


def create_step(config):
    factory_name = f'make_{config["type"]}_step'
    step_path = f'kari.flows.steps.{config["type"]}'
    if 'step_path' in config:
        step_path = config['step_path']

    module = importlib.import_module(step_path)
    step_factory = getattr(module, factory_name)
    step = step_factory(config)

    return step
