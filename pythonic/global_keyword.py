#!/usr/bin/python3

text = "hello"

def read_text():
    print(text)


def append_text(add):
    global text

    text += add
    print(text)


def main():
    read_text()
    append_text(" world")


if __name__ == "__main__":
    main()
