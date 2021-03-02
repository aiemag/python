#!/usr/bin/python3

def main():

    o_list = [1,2,3,4,5,6]

    c_list = [x*x for x in o_list]
    print("comprehension list : ",c_list)
    
    c_list = [x for x in o_list if x%2==0]
    print("comprehension list with condition(if x%2==0) : ",c_list)
    
    c_list = [x*10 if x<=3 else x*100 for x in o_list]
    print("comprehension list with ternary operator(x*10 if x<=3 else x*100) : ",c_list)


if __name__ == "__main__":
    main()
