#!/usr/bin/python3

def foo():
    text = "hello"
    
    def read_text():
        print(text)

    def append_text(add):
        nonlocal text
        
        text += add
        print(text)

    read_text()
    append_text(" world")


def main():
    foo()


if __name__ == "__main__":
    main()
