#!/usr/bin/env python3
"""Module for measuring the execution time of an asynchronous coroutine.

This module provides a function to calculate the average runtime per execution
of the concurrent coroutine `wait_n` imported from a dynamic module.
"""
import asyncio
import importlib
import time

# Dynamically import the helper module that provides `wait_n`.
# Using importlib because module name starts with a number.
basic_async_syntax = importlib.import_module("1-concurrent_coroutines")

# Pull the function into this module's namespace for convenience.
wait_n = basic_async_syntax.wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the total execution time for wait_n(n, max_delay).

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        float: The average execution time per iteration (total_time / n).
    """
    # Start high-resolution performance counter
    start_time = time.perf_counter()
    # Run the async code inside the synchronous function using event loop
    asyncio.run(wait_n(n, max_delay))
    # End performance counter
    end_time = time.perf_counter()
    # Calculate the total elapsed time
    total_time = end_time - start_time
    # Return average time per execution
    return total_time / n
