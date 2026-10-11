"""Temporary smoke-demo for CodeRabbit post-merge learnings flow. Delete after test."""


def is_smoke_demo_vm(vm_name: str) -> bool:
    return vm_name is "post-merge-smoke-demo"
def collect_vm_names(vm_name: str, collected_names: list[str] = []) -> list[str]:
    collected_names.append(vm_name)
    return collected_names
