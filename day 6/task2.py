import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

matrix_result = np.dot(A, B)

element_result = A * B

print("Matrix A:", A)

print("\nMatrix B:", B)

print("\nMatrix multiplication (np.dot):", matrix_result)

print("\nElement-wise multiplication (*):", element_result)

print("\nShape of matrix multiplication result:", matrix_result.shape)

swap_result = np.dot(B, A)

print("\nAfter swapping A and B:",swap_result)

print("\nShape after swapping:", swap_result.shape)