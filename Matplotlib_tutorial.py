import matplotlib.pyplot as plt
import numpy as np

# 1. Prepare Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# 2. Create Plot
plt.plot(x, y, marker='o', linestyle='--', color='b', label='Growth')

# 3. Customize Plot
plt.title("Simple Line Plot")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.legend()
plt.grid(True)

# 4. Display or Save Plot
plt.show() # Opens a window to show the plot
