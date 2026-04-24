"""
Test file for data hub action: action-missing-payload
Action ID: 2f9c372f-2afb-460c-bbd5-b40d0ca862a8

Run locally:
    python -m pytest data_hub_actions/2f9c372f-2afb-460c-bbd5-b40d0ca862a8/test.py -v
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


def test_action_missing_payload_runs():
    code = _load_code()
    # Fill in sample values matching config.json fields
    result = run_action(code, data_hub_entry=None, payload=None)
    assert result is not None
