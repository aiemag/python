#!/usr/bin/python3
# This code operates at python2.X version.

def upper_attr(future_class_name, future_class_parents, future_class_attr):

    uppercase_attr = {}
   
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    return type(future_class_name, future_class_parents, uppercase_attr)


__metaclass__ = upper_attr

def change_metaclass():

    class Foo():
        value1 = 1

    a = Foo()
    print(Foo.__dict__)
   

def main():
    change_metaclass()


if __name__ == "__main__":
    main()
