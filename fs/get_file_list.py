#!/usr/bin/python3 

import os, glob 

# getting file list
def get_file_list(path):
    return glob.glob(path)


def filter_file_list(path, exp, dir_filter):

    def is_dir(fo):
        return True if os.path.isdir(fo) else False

    flist = glob.glob(os.path.join(path, exp))

    if dir_filter is None:
        return flist
    elif dir_filter:
        return list(filter(os.path.isdir, flist))
    else:
        return list(filter(lambda x:not os.path.isdir(x), flist))

    return glob.glob(os.path.join(path, exp))


def main():
    print("all list")
    flist = get_file_list("./*")
    print(flist+"\n")

    print("all list with filter")
    flist = filter_file_list("./", "*.py", None)
    print(flist+"\n")

    print("all list")
    flist = filter_file_list("./", "*", None)
    print(flist+"\n")

    print("all dir list")
    flist = filter_file_list("./", "*", True)
    print(flist+"\n")

    print("all file list")
    flist = filter_file_list("./", "*", False)
    print(flist+"\n")


if __name__ == '__main__':
    main()
