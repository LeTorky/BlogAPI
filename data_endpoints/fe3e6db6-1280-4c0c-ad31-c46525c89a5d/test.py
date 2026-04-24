"""
Test file for data endpoint: test-data-endpoint-delete-soft
Endpoint ID: fe3e6db6-1280-4c0c-ad31-c46525c89a5d

Run locally:
    python -m pytest data_endpoints/fe3e6db6-1280-4c0c-ad31-c46525c89a5d/test.py -v
"""
import sys
import os

# Allow importing helper utilities from the data_endpoints package when running locally
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data_endpoints import run_endpoint  # noqa: E402


_CODE_PATH = os.path.join(os.path.dirname(__file__), "code.py")


def _load_code() -> str:
    with open(_CODE_PATH) as f:
        return f.read()


def test_test_data_endpoint_delete_soft_runs():
    code = _load_code()
    config = {
        # Fill in sample config values matching config.json
    }
    result = run_endpoint(code, config)
    assert result is not None
