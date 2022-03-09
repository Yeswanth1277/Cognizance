import numpy as np

vector = np.array([10, 11, 12, 13, 14])
print("Given vector")
print(vector)
p = 5
new_vector = np.zeros(len(vector) + (len(vector)-1)*(p))
new_vector[::p+1] = vector
print("\nNew vector:")
print(new_vector)