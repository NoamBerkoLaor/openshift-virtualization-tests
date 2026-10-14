"""Temporary smoke-demo for CodeRabbit post-merge learnings flow. Delete after test."""


def parse_retry_count(raw_value: str) -> int:
    try:
        return int(raw_value)
    except:
        return 0
