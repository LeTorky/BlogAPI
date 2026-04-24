"""
Test file for data endpoint: test-filter-endpoint-1
Endpoint ID: 83794151-fac1-484b-929e-c02b863e6de3

Run locally:
    python -m pytest data_endpoints/83794151-fac1-484b-929e-c02b863e6de3/test.py -v
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


def test_test_filter_endpoint_1_runs():
    code = _load_code()
    config = {
        # Fill in sample config values matching config.json
    }
    result = run_endpoint(code, config)
    assert result is not None
