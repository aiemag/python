#!/usr/bin/python3

import glob, os
import pandas as pd


def read_parquet_to_df(path):
    if os.path.isdir(path):
        files = glob.glob(os.path.join(path, "*.parquet"))
    else:
        files = [path]

    rst = pd.concat([[pd.read_parquet(f, engine='pyarrow') for f in files]])

    return res.reset_index()



def main():
    pass


if __name__ == "__main__":
    main()
