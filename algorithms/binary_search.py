"""
Binary Search Algorithm
Classic binary search implementation with variations.
Demonstrates efficient searching in sorted sequences.
"""

from typing import List, Optional

def binary_search(arr: List[int], target: int) -> int:
    """
    Standard binary search that returns the index of target.
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
    
    Returns:
        Index of target if found, -1 otherwise
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def binary_search_leftmost(arr: List[int], target: int) -> int:
    """
    Find the leftmost (first) occurrence of target.
    
    Args:
        arr: Sorted list of integers (may contain duplicates)
        target: Value to search for
    
    Returns:
        Index of leftmost occurrence, -1 if not found
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left if left < len(arr) and arr[left] == target else -1

def binary_search_rightmost(arr: List[int], target: int) -> int:
    """
    Find the rightmost (last) occurrence of target.
    
    Args:
        arr: Sorted list of integers (may contain duplicates)
        target: Value to search for
    
    Returns:
        Index of rightmost occurrence, -1 if not found
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left - 1 if left > 0 and arr[left - 1] == target else -1

def binary_search_recursive(arr: List[int], target: int, left: int = 0, 
                           right: Optional[int] = None) -> int:
    """
    Recursive binary search implementation.
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
        left: Left boundary (default 0)
        right: Right boundary (default len(arr) - 1)
    
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9]
    
    print(f"Array: {arr}")
    print(f"\nBinary search for 5: {binary_search(arr, 5)}")
    print(f"Leftmost 5: {binary_search_leftmost(arr, 5)}")
    print(f"Rightmost 5: {binary_search_rightmost(arr, 5)}")
    print(f"Recursive search for 7: {binary_search_recursive(arr, 7)}")
    print(f"Search for 10 (not in array): {binary_search(arr, 10)}")
