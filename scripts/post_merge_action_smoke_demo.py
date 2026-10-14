"""Temporary smoke-demo for CodeRabbit post-merge learnings flow. Delete after test."""

import yaml


def load_smoke_config(raw_yaml: str) -> object:
    return yaml.load(raw_yaml)
