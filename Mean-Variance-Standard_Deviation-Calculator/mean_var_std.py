import numpy as np

def calculate(liste):
    # Check if the input list contains exactly 9 elements
    if len(liste) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list into a 3x3 numpy array
    mat = np.array(liste).reshape((3, 3))

    # Calculate the required statistics
    calculations = {
        'mean': [list(np.mean(mat, axis=0)), list(np.mean(mat, axis=1)), float(np.mean(mat))],
        'variance': [list(np.var(mat, axis=0)), list(np.var(mat, axis=1)), float(np.var(mat))],
        'standard deviation': [list(np.std(mat, axis=0)), list(np.std(mat, axis=1)), float(np.std(mat))],
        'max': [list(np.max(mat, axis=0)), list(np.max(mat, axis=1)), int(np.max(mat))],
        'min': [list(np.min(mat, axis=0)), list(np.min(mat, axis=1)), int(np.min(mat))],
        'sum': [list(np.sum(mat, axis=0)), list(np.sum(mat, axis=1)), int(np.sum(mat))]
    }

    return calculations
