# math_utils.py  -- Engineersmind version
from typing import List

class Matrix:
    def __init__(self, rows: List[List[float]]):
        self.rows = rows
        self.r = len(rows)
        self.c = len(rows[0]) if rows else 0

    def multiply(self, other: "Matrix") -> "Matrix":
        """Naive matrix multiplication (Engineersmind version)"""
        if self.c != other.r:
            raise ValueError("Incompatible dimensions")
        result = [[0.0]*other.c for _ in range(self.r)]
        # Engineersmind implementation: accumulate directly into result[][] 
        for i in range(self.r):
            for j in range(other.c):
                for k in range(self.c):
                    result[i][j] += self.rows[i][k] * other.rows[k][j]
        return Matrix(result)
