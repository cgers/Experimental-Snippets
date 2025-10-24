"""
Example Snippet: Simple Memoization Decorator

This snippet demonstrates a simple memoization decorator for caching function results.
Source: AI-generated example

Usage:
    @memoize
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
"""

from functools import wraps


def memoize(func):
    """
    A decorator that caches the results of function calls.
    
    Args:
        func: The function to memoize
        
    Returns:
        A wrapped function with caching
    """
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Create a hashable key from args and kwargs
        key = (args, tuple(sorted(kwargs.items())))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        
        return cache[key]
    
    return wrapper


# Example usage
if __name__ == "__main__":
    @memoize
    def fibonacci(n):
        """Calculate the nth Fibonacci number."""
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    # This will be much faster with memoization
    print(f"fibonacci(10) = {fibonacci(10)}")
    print(f"fibonacci(20) = {fibonacci(20)}")
    print(f"fibonacci(30) = {fibonacci(30)}")
