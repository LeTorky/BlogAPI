"""
Test file for data endpoint: test-data-endpoint-update
Endpoint ID: 935e91ee-588a-4eee-8afb-f7f748449bc9

Run locally:
    python -m pytest data_endpoints/935e91ee-588a-4eee-8afb-f7f748449bc9/test.py -v
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


def test_test_data_endpoint_update_runs():
    code = _load_code()
    config = {
        # Fill in sample config values matching config.json
    }
    result = run_endpoint(code, config)
    assert result is not None
