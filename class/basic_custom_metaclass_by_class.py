#!/usr/bin/python3

class UpperAttrMetaclass(type):

    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(upperattr_metaclass, future_class_name, 
                            future_class_parents, uppercase_attr)



metaclass = UpperAttrMetaclass

def change_metaclass():

    class Foo(metaclass = UpperAttrMetaclass):
        value1 = 1

    a = Foo()
    print(Foo.__dict__)
   

def main():
    change_metaclass()


if __name__ == "__main__":
    main()
