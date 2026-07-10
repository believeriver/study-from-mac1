import pandas as pd
import os

def test_read_csv(file_name):
    print(file_name)
    dir_name = os.getcwd()
    df = pd.read_csv(file_name)
    print(df.head())

    dates = df['Date']
    print(dates.head())
    datas = df['Sandybridge']
    print(datas.head())


if __name__ == '__main__':
    file_name = '202303.csv'
    test_read_csv(file_name)