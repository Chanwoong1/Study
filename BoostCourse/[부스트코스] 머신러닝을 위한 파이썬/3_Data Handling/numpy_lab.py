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
    pass


def concat_ndarray(X_1, X_2, axis):
    pass


def normalize_ndarray(X, axis=99, dtype=np.float32):
    pass


def save_ndarray(X, filename="test.npy"):
    pass


def boolean_index(X, condition):
    pass


def find_nearest_value(X, target_value):
    pass


def get_n_largest_values(X, n):
    pass
