import numpy as np
import pandas as pd

def get_rating_matrix(filename):
    file_df = pd.read_csv(filename).pivot_table(['rating'], index = ['source'],
                    columns = 'target', fill_value = 0)
    return np.array(file_df)


def get_frequent_matrix(filename):
    df = pd.read_csv(filename, header = 0)
    df['rating'] = 1
    return np.array(df.groupby(['source', 'target']).sum().unstack().fillna(0))
