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

    print("unique KEY")
    unique_key = df_filtered['KEY'].unique()
    print(unique_key)
    print('\n')

    print("result df")
    df_rst = df[df['KEY'].isin(unique_key)]
    df_rst.reset_index(inplace=True, drop=True)
    print(df_rst)
    print('\n')


def main():
    load_data()
    process()


if __name__ == "__main__":
    main()
