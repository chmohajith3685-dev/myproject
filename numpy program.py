import numpy as np
 
# --- 1. Create Arrays ---
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
print("Array A:", a)
print("Array B:", b)
 
# --- 2. Array Operations ---
print("\nAddition:      ", a + b)
print("Subtraction:   ", b - a)
print("Multiplication:", a * b)
print("Division:      ", b / a)
 
# --- 3. 2D Array (Matrix) ---
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print("\n2D Matrix:\n", matrix)
print("Shape:", matrix.shape)
print("Transpose:\n", matrix.T)
 
# --- 4. Built-in Functions ---
print("\nSum:  ", np.sum(a))
print("Mean: ", np.mean(a))
print("Max:  ", np.max(a))
print("Min:  ", np.min(a))
print("Std:  ", np.std(a))
 
# --- 5. Special Arrays ---
print("\nZeros:\n", np.zeros((2, 3)))
print("Ones:\n",  np.ones((2, 3)))
print("Range:",   np.arange(0, 10, 2))
print("Linspace:",np.linspace(0, 1, 5))
 
# --- 6. Random Numbers ---
print("\nRandom Array:", np.random.randint(1, 100, 5))
print("Random Matrix:\n", np.random.rand(2, 3).round(2))
 
