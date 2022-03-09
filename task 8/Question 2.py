import numpy as np

x = input(np.array)
print('First array:')
print(x)

y = input(np.array)
print('Second array:')
print(y)

print('Testing if the above two arrays are equal or not!')
array_equal = np.array_equal(np.array(x),np.array(y))

print(array_equal)