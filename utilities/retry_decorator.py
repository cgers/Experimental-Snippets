"""
Retry Decorator
A practical utility for retrying functions that may fail due to transient errors.
Useful for network requests, database operations, and other unreliable operations.
"""

import time
from functools import wraps
from typing import Callable, Type, Tuple

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """
    Decorator that retries a function if it raises specified exceptions.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay after each retry
        exceptions: Tuple of exception types to catch
    
    Returns:
        Decorated function that implements retry logic
    """
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying in {current_delay}s...")
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        print(f"All {max_attempts} attempts failed.")
            
            raise last_exception
        
        return wrapper
    return decorator

# Example usage
if __name__ == "__main__":
    call_count = 0
    
    @retry(max_attempts=3, delay=0.5, backoff=2, exceptions=(ValueError,))
    def unstable_function():
        global call_count
        call_count += 1
        print(f"Function called (attempt {call_count})")
        if call_count < 3:
            raise ValueError("Simulated transient error")
        return "Success!"
    
    try:
        result = unstable_function()
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Failed with error: {e}")
