"""
Fibonacci with Memoization
An efficient implementation of Fibonacci sequence using memoization technique.
Demonstrates dynamic programming and decorator pattern in Python.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Calculate the nth Fibonacci number using memoization.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The nth Fibonacci number
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
if __name__ == "__main__":
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}")
