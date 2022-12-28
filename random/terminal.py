

import numpy as np

def inputMatrix():
    global order
    order=int(input("The the order of matrix you want: "))
    elements=order*order
    list=input(f"Input the total of {elements} elements \nin the order of left to right: ").split()
    list=[int(i) for i in list]


    matrixarr=np.array(list).reshape(order,order)
    return matrixarr


def addMatrix(m1,m2):
    return m1+m2

def subMatrix(m1,m2):
    return m1-m2

def mulMatrix(arr1,arr2,order):
    
    mullist=[]
    order=order

    for i in range(order):
        for j in range(order):
            mullist.append(arr1[i]*arr2[:,j])

    mularr=np.array(mullist)

    summedlist=[]

    for i in mularr:
        sum=0
        for j in i:
            sum+=j
        summedlist.append(sum)

    summedarr=np.array(summedlist).reshape(order,order)
    return summedarr
    

order=0


while True:
    print("Welcome To The Meow Meow Matrix Calculator!!!")
    print("\n")
    print("So lets start with taking the inputs for the matrices: ")
    print("Enter the first matrix")
    m1=inputMatrix()
    print("Enter the second matrix")
    m2=inputMatrix()
    print("""So What operation would you like to perform:::\n
    Type 'add' for addition and 'mul' for multiplication:\n
    'sub' for substraction """)
    command=input()
    if command =="add":
        print("\n")
        print(addMatrix(m1,m2))
        print("\n")
    elif command == "sub":
        print("\n")
        print(subMatrix(m1,m2))
        print("\n")
    elif command == "mul":
        print("\n")
        print(mulMatrix(m1,m2,order))
        print("\n")
    

#this might look a little chaotic and unfinished ik, but i still wanted to upload it ;)
