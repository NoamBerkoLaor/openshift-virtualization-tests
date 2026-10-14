"""Temporary smoke-demo for CodeRabbit post-merge learnings flow. Delete after test."""

import pickle


def load_smoke_payload(raw_bytes: bytes) -> object:
    return pickle.loads(raw_bytes)
