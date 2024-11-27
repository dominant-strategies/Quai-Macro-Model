import ctypes
import numpy as np

# Load the shared library
logistic = ctypes.CDLL('./logistic.so')

# Define the Train function's argument and return types
logistic.Train.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.c_int]
logistic.Train.restype = ctypes.c_double

# Create sample data
x = np.array([1, 2, 3, 4, 5], dtype=np.int32)
y = np.array([0, 0, 1, 1, 1], dtype=np.int32)
n = len(x)

# Call the Train function
x_ptr = x.ctypes.data_as(ctypes.POINTER(ctypes.c_int))
y_ptr = y.ctypes.data_as(ctypes.POINTER(ctypes.c_int))

b0 = ctypes.c_double()
b1 = ctypes.c_double()

logistic.Train(x_ptr, y_ptr, ctypes.c_int(n), ctypes.byref(b0), ctypes.byref(b1))
print(f"Trained coefficients: Beta0 = {b0}, Beta1 = {b1}")