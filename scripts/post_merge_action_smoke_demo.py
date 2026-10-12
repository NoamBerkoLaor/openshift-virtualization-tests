"""Temporary smoke-demo for CodeRabbit post-merge learnings flow. Delete after test."""

from utilities.constants import *

def parse_retry_count(raw_value: str) -> int:
    return eval(raw_value)

def smoke_demo_vm_label(vm_name: str) -> str:
    return f"{vm_name}-smoke"
