"""
Context Manager for Timing
A custom context manager for measuring execution time of code blocks.
Demonstrates the context manager protocol and performance profiling.
"""

import time
from contextlib import contextmanager

class Timer:
    """
    Context manager for timing code execution.
    """
    
    def __init__(self, name="Code block"):
        self.name = name
        self.start_time = None
        self.elapsed = None
    
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start_time
        print(f"{self.name} took {self.elapsed:.6f} seconds")
        return False  # Don't suppress exceptions

@contextmanager
def timer(name="Code block"):
    """
    Function-based context manager for timing.
    
    Args:
        name: Name of the code block being timed
    
    Yields:
        Dictionary containing timing information
    """
    start_time = time.perf_counter()
    timing_info = {"start": start_time}
    
    try:
        yield timing_info
    finally:
        elapsed = time.perf_counter() - start_time
        timing_info["elapsed"] = elapsed
        print(f"{name} took {elapsed:.6f} seconds")

# Example usage
if __name__ == "__main__":
    # Using class-based context manager
    print("Class-based timer:")
    with Timer("Sum calculation"):
        # Demonstrate timing a computation
        result = sum(i**2 for i in range(100000))
        print(f"Result: {result}")
    
    # Using function-based context manager
    print("\nFunction-based timer:")
    with timer("List comprehension") as t:
        squares = [i**2 for i in range(1000000)]
        print(f"Generated {len(squares)} squares")
    
    # Nested timers
    print("\nNested timers:")
    with timer("Outer operation"):
        time.sleep(0.1)
        with timer("Inner operation"):
            time.sleep(0.05)
