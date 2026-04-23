"""
Test file for block: string
Block ID: a700c79e-ee72-4479-8f62-32f45b72e1f4

Run locally:
    python -m pytest pipeline_builder/a700c79e-ee72-4479-8f62-32f45b72e1f4/test.py -v
"""
import sys
import os

# Allow importing helper utilities from the pipeline_builder package when running locally
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipeline_builder import run_block  # noqa: E402


_CODE_PATH = os.path.join(os.path.dirname(__file__), "code.py")


def _load_code() -> str:
    with open(_CODE_PATH) as f:
        return f.read()


def test_string_runs():
    code = _load_code()
    config = {
        # Fill in sample config values matching input_fields.json
    }
    result = run_block(code, config)
    assert result is not None
