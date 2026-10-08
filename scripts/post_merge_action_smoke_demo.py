"""Temporary smoke-demo file for CodeRabbit post-merge learnings test.

Delete this file after the fork smoke test. Intentionally violates a pattern
that is not currently spelled out in AGENTS.md (mutable default argument).
"""


def collect_vm_names(vm_name: str, collected_names: list[str] = []) -> list[str]:
    collected_names.append(vm_name)
    return collected_names
