'''
Let's access elements in NumPy arrays! Your task is to convert a square two-dimensional array square of size size to a list created by following a spiral pattern:

Rather than simply accessing certain slices, you will define a more general solution using a for loop (the solution should work for all the square two-dimensional arrays of odd size).

The module numpy is already imported as np.

You will need the reversed() function, which reverses an Iterable.    (Image has been attached for the reference)
'''

import numpy as np

square = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]])

spiral = []
size = len(square)

for i in range(0, size):
    # Convert each part marked by a red arrow to a list
    spiral += list(square[i, i:size-i])
    # Convert each part marked by a green arrow to a list
    spiral += list(square[i+1:size-i, size-i-1])
    # Convert each part marked by a blue arrow to a list
    spiral += list(reversed(square[size-i-1, i:size-i-1]))
    # Convert each part marked by a magenta arrow to a list
    spiral += list(reversed(square[i+1:size-i-1, i]))
    
print(spiral)
