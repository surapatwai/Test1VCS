import random
def generate_list():
    alist = [x for x in range(random.randint(-10,10))]
    assert len(alist)!=0,"A list in null"
    sum=0
    for i in alist:
        sum=sum+alist[i]
    assert sum>-1," sum of data in list is less than 0"
    return alist

"""
print a generate_list
"""
def printIt():
    print(generate_list())

def main():
    printIt()

"""
IF this script file is called, it will run main() directly
"""

if __name__ == '__main__' :
    print("Test printIT():")
    main()

