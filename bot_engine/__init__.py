"""
Bot Engine Package
Contains the core classification logic and LLM routing.
"""
from .router import classify_ticket

__all__ = ['classify_ticket']
