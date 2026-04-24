"""
data_endpoints/__init__.py — helper utilities for local endpoint development.

When developing a data endpoint from your IDE, you can import from this module
to get a local approximation of the platform runtime:

    from data_endpoints import run_endpoint

The platform itself does not use this file at runtime.
"""
from typing import Any, Dict


def run_endpoint(code: str, config: Dict[str, Any]) -> Any:
    """Execute endpoint code with the given config and return the result."""
    local_ns: Dict[str, Any] = {}
    exec(compile(code, "<endpoint>", "exec"), local_ns)
    fn = local_ns.get("main") or local_ns.get("run") or local_ns.get("handler")
    if fn is None:
        raise RuntimeError("Endpoint code must define a `main(config)`, `run(config)`, or `handler(config)` function.")
    return fn(config)
