"""
Test file for block: test-block-create
Block ID: 2202874e-1ddc-4f17-b5a3-afcd2fdf84e1

Run locally:
    python -m pytest pipeline_builder/2202874e-1ddc-4f17-b5a3-afcd2fdf84e1/test.py -v
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


def test_test_block_create_runs():
    code = _load_code()
    config = {
        # Fill in sample config values matching input_fields.json
    }
    result = run_block(code, config)
    assert result is not None
