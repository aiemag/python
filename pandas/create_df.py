#/usr/bin/python3

import pandas as pd

def process():

    print("create empty dataframe")
    df = pd.DataFrame()
    print(df)
    print('\n')

    print("create dataframe by using list")
    df = pd.DataFrame(data=[[1,2],[3,4]], columns=['A', 'B'])
    print(df)
    print('\n')

    print("create dataframe by using dictionary")
    df = pd.DataFrame(data={'A':[1,3], 'B':[2,4]})
    print(df)
    print('\n')


def main():
    process()


if __name__ == "__main__":
    main()
