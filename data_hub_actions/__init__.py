"""
data_hub_actions/__init__.py — helper utilities for local action development.

When developing a data hub action from your IDE, you can import from this module
to get a local approximation of the platform runtime:

    from data_hub_actions import run_action

The platform itself does not use this file at runtime.
"""
from typing import Any, Dict


def run_action(code: str, data_hub_entry: Any = None, payload: Any = None) -> Any:
    """Execute action code with the given context and return the result."""
    local_ns: Dict[str, Any] = {}
    exec(compile(code, "<action>", "exec"), local_ns)
    fn = local_ns.get("main") or local_ns.get("run") or local_ns.get("handler")
    if fn is None:
        raise RuntimeError("Action code must define a `main(...)`, `run(...)`, or `handler(...)` function.")
    return fn(data_hub_entry=data_hub_entry, payload=payload)
