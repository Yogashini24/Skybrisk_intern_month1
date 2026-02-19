import numpy as np
import pandas as pd


def numpy_demo():
    a = np.array([1, 2, 3])
    b = a * 2  # broadcasting
    print('a', a, 'b', b)


def pandas_demo(path='sample_data.csv'):
    df = pd.read_csv(path)
    print('Head:\n', df.head())
    print('\nIndexing example (temp column):')
    print(df['temp'].head())
    print('\nGroup by city and count rows:')
    print(df.groupby('city').size())


if __name__ == '__main__':
    numpy_demo()
    pandas_demo('sample_data.csv')
