# kari
*kari* is a Python library for orchestrating Large Language Models (LLMs) inference pipelines. The goal is to offer a configuration-driven platform to describe LLM workflows.

The goals of the library are:
- Easy to adopt
- Workflows are defined via YAML files
- Support for multi-model inference within the same workflow
- Additional supporting features such as chunking, parallel evaluation, output styling, etc.

## Installation

```bash
# Install dependencies with Poetry
poetry install

# Use Poetry to run commands in the virtual environment
poetry shell
```

## Running Tests

```bash
# Run all tests (from poetry shell)
pytest

# Or with poetry run (without activating shell)
poetry run pytest

# Run a specific test file
pytest tests/functional/flows.py

# Run a specific test
pytest tests/functional/ollama_flow.py::test_ollama_flows
```

Note: Ollama integration tests require a running Ollama server with the `llama3.2:1b` model installed.


==
_The name kari is a reference to the indigenous people known as [Kariñas](https://en.wikipedia.org/wiki/Kalina_people)_
