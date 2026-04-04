import numpy as np 

# Create a 1D array
arr1d=np.array([1,2,3,4,5,6])
print(f"1D Array:{arr1d}")

# Create a 2D array
arr2d=np.array([[1,2,3],[4,6,8]])
print(f"2D Array:{arr2d}")

# Performing Basic Mathematical operations
a=np.array([12,56,89])
b=np.array([1,0,1])
arr_sum = np.add(a,b)
print(f"\na:{a}")
print(f"b:{b}") 
print(f"Element wise addition:{arr_sum}")


#Statistics
data=np.array((23,56,78,90,45))
mean_val=np.mean(data)
min_val=np.min(data)
max_val=np.max(data)
print(f"\nArray:{data}")
print(f"Mean:{mean_val}")
print(f"Minimum:{min_val}")
print(f"Maximum:{max_val}")