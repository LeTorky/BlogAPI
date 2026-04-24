"""
pipeline_builder/__init__.py — helper utilities for local block development.

When developing a block from your IDE, you can import from this module
to get a local approximation of the platform runtime:

    from pipeline_builder import run_block

The platform itself does not use this file at runtime.
"""
from typing import Any, Dict


def run_block(code: str, config: Dict[str, Any]) -> Any:
    """Execute block code with the given config and return the result."""
    local_ns: Dict[str, Any] = {}
    exec(compile(code, "<block>", "exec"), local_ns)
    fn = local_ns.get("main") or local_ns.get("run")
    if fn is None:
        raise RuntimeError("Block code must define a `main(config)` or `run(config)` function.")
    return fn(config)
