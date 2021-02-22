#/usr/bin/python3

import pandas as pd

df = None

def load_data():
    global df
    df = pd.read_csv("./sample.csv")


def process():
    print("original df")
    print(df)
    print('\n')

    print("filtered df")
    df_filtered = df[df['B']==1][df['C']==1]
    print(df_filtered)
    print('\n')

    print("inplace=True")
    df_filtered = df[df['B']==1][df['C']==1]
    df_rst = df_filtered.reset_index(inplace=True)
    print(df_rst)
    print(df_filtered)
    print('\n')

    print("inplace=False")
    df_filtered = df[df['B']==1][df['C']==1]
    df_rst = df_filtered.reset_index(inplace=False)
    print(df_rst)
    print(df_filtered)
    print('\n')

    print("inplace=True, drop=True")
    df_filtered = df[df['B']==1][df['C']==1]
    df_rst = df_filtered.reset_index(inplace=True, drop=True)
    print(df_rst)
    print(df_filtered)
    print('\n')

    print("inplace=False, drop=True")
    df_filtered = df[df['B']==1][df['C']==1]
    df_rst = df_filtered.reset_index(inplace=False, drop=True)
    print(df_rst)
    print(df_filtered)
    print('\n')


def main():
    load_data()
    process()


if __name__ == "__main__":
    main()
