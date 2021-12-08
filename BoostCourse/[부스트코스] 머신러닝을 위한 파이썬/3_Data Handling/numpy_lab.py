import numpy as np


def n_size_ndarray_creation(n, dtype=np.int):
    X = np.arange((n ** 2), dtype = dtype).reshape(n, n)
    return X


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0 :
        X = np.zeros(shape = shape, dtype = dtype)
    elif type == 1 :
        X = np.ones(shape = shape, dtype = dtype)
    else :
        X = np.empty(shape = shape, dtype = dtype)
    return X


def change_shape_of_ndarray(X, n_row):
    if n_row == 1 :
        return X.flatten()
    return X.reshape(n_row, -1)


def concat_ndarray(X_1, X_2, axis):
    try :
        if X_1.ndim == 1:
            X_1 = X_1.reshape(1, -1)
        if X_2.ndim == 1 :
            X_2 = X_2.reshape(1, -1)
        return np.concatenate((X_1, X_2), axis = axis)
    except ValueError:
        return False


def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 99 :
        return np.array((X - np.mean(X)) / X.std(), dtype = dtype)
    elif axis == 0 :
        return np.array([(X[i] - np.mean(X[i])) / X[i].std() for i in range(len(X))], dtype = dtype)
    else :
        return np.array([(i - np.mean(i)) / np.array(i).std() for i in zip(*X)], dtype = dtype).T


def save_ndarray(X, filename="test.npy"):
    file_test = open(filename, 'wb')
    return np.save(file_test, X)


def boolean_index(X, condition):
    condition = eval(str('X') + condition)
    return np.where(condition)


def find_nearest_value(X, target_value):
    return target_value - min(abs(X - target_value))


def get_n_largest_values(X, n):
    return np.sort(X)[::-1][ : n]