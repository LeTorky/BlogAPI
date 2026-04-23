"""
Test file for block: block-to-delete
Block ID: c5b21c5b-393d-4565-a297-0dee2631945d

Run locally:
    python -m pytest pipeline_builder/c5b21c5b-393d-4565-a297-0dee2631945d/test.py -v
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


def test_block_to_delete_runs():
    code = _load_code()
    config = {
        # Fill in sample config values matching input_fields.json
    }
    result = run_block(code, config)
    assert result is not None
