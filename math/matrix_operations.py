"""
Matrix Operations
Fundamental matrix operations implemented from scratch.
Useful for understanding linear algebra and numerical computing.
"""

from typing import List

def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiply two matrices.
    
    Args:
        A: First matrix (m x n)
        B: Second matrix (n x p)
    
    Returns:
        Result matrix (m x p)
    
    Raises:
        ValueError: If matrices cannot be multiplied
    """
    if not A or not B:
        raise ValueError("Matrices cannot be empty")
    
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError(f"Cannot multiply {rows_A}x{cols_A} by {rows_B}x{cols_B} matrices")
    
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def matrix_transpose(matrix: List[List[float]]) -> List[List[float]]:
    """
    Transpose a matrix.
    
    Args:
        matrix: Input matrix
    
    Returns:
        Transposed matrix
    """
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

def matrix_determinant(matrix: List[List[float]]) -> float:
    """
    Calculate the determinant of a square matrix.
    
    Args:
        matrix: Square matrix
    
    Returns:
        Determinant value
    
    Raises:
        ValueError: If matrix is not square
    """
    n = len(matrix)
    
    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square")
    
    if n == 1:
        return matrix[0][0]
    
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for j in range(n):
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]
        det += ((-1) ** j) * matrix[0][j] * matrix_determinant(minor)
    
    return det

# Example usage
if __name__ == "__main__":
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    
    print("Matrix A:")
    for row in A:
        print(row)
    
    print("\nMatrix B:")
    for row in B:
        print(row)
    
    print("\nA × B:")
    result = matrix_multiply(A, B)
    for row in result:
        print(row)
    
    print("\nTranspose of A:")
    transpose = matrix_transpose(A)
    for row in transpose:
        print(row)
    
    print(f"\nDeterminant of A: {matrix_determinant(A)}")
