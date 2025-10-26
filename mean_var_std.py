import numpy as np

# Create a function named calculate() that uses Numpy for the calculation
# The input of the function should be a list containing 9 digits.
def calculate(main):
    if len(main) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix= np.array(main)

# Convert the list to a 3×3 Numpy array
    matrix = matrix.reshape(3,3)

# Define a helper function to calculate along both axes and for the flattened matrix.
    def calc_state(func, array):
        return [func(array, axis=0).tolist(),
         func(array, axis=1).tolist(),
         func(array).tolist()]

# Calculate the mean, variance, standard deviation, max, min and sum
    result = {'mean': calc_state(np.mean, matrix),
              'variance': calc_state(np.var, matrix),
              'standard deviation': calc_state(np.std, matrix),
              'max': calc_state(np.max, matrix),
              'min': calc_state(np.min, matrix),
              'sum': calc_state(np.sum, matrix),
              }
    
    return result
