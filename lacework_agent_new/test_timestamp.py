#!/usr/bin/env python3
"""
Test script for the get_utc_timestamp function.
"""

from src.utils import get_utc_timestamp

if __name__ == "__main__":
    # Get and print the current UTC timestamp
    timestamp = get_utc_timestamp()
    print(f"Current UTC timestamp: {timestamp}")
