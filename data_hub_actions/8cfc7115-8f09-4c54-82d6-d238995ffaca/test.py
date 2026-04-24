"""
Test file for data hub action: action-invalid-payload
Action ID: 8cfc7115-8f09-4c54-82d6-d238995ffaca

Run locally:
    python -m pytest data_hub_actions/8cfc7115-8f09-4c54-82d6-d238995ffaca/test.py -v
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


def test_action_invalid_payload_runs():
    code = _load_code()
    # Fill in sample values matching config.json fields
    result = run_action(code, data_hub_entry=None, payload=None)
    assert result is not None
