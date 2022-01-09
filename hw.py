from PIL import Image
import numpy as np
from numpy.linalg import norm


def isDiagonal(x):
    if (np.count_nonzero(x - np.diag(np.diagonal(x))) > 0):
        return False
    return True

def isLowerTriangular(x):
    return np.allclose(x, np.tril(x))
    
def isUpperTriangular(x):
    return np.allclose(x, np.triu(x))



im = Image.open("somepath")
image_array = np.array(im)

# Transpose: 

transposedIm = image_array.T


# Check if matrix is diagonal or triagonal:

print("Image is diagonal: " + isDiagonal(image_array))
print("Image is lower triangular: " + isLowerTriangular(image_array))
print("Image is upper triangular: " + isUpperTriangular(image_array))


# Choose a column vector and calculate both norms:

col = image_array[:,1]



print("L1 norm: " + norm(col, 1))
print("L2 norm: " + norm(col))





