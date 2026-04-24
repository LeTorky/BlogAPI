"""
Test file for data hub action: test-action-create
Action ID: 6ba26c90-94ce-4db9-a829-46026cb67dfd

Run locally:
    python -m pytest data_hub_actions/6ba26c90-94ce-4db9-a829-46026cb67dfd/test.py -v
"""
import sys
import os

# Allow importing helper utilities from the data_hub_actions package when running locally
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_hub_actions import run_action  # noqa: E402


_CODE_PATH = os.path.join(os.path.dirname(__file__), "code.py")


def _load_code() -> str:
    with open(_CODE_PATH) as f:
        return f.read()


def test_test_action_create_runs():
    code = _load_code()
    # Fill in sample values matching config.json fields
    result = run_action(code, data_hub_entry=None, payload=None)
    assert result is not None
