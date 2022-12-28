from tkinter import * 
from tkinter import ttk
import numpy as np

root=Tk()
root.title("Meow Meow Matrix Calculator")
root.geometry("600x600")

order=0
matrix1=np.array([])
matrix2=np.array([])
def orderButton():
    global order
    integar=orderbox.get()
    order=int(integar)
    elementslabel.configure(text=f"enter {order*order} elements here")
    m1label.configure(text="Enter the elements of first matrix here separated by space")
    m2label.configure(text="Enter the elements of second matrix here separated by space")

def inputmatrixgui():
    m1lst=m1box.get().split()
    m1lst=[int(i) for i in m1lst]
    matrixarr1=np.array(m1lst).reshape(order,order)

    m2lst=m2box.get().split()
    m2lst=[int(i) for i in m2lst]
    matrixarr2=np.array(m2lst).reshape(order,order)
    
    global matrix1
    matrix1=matrixarr1
    global matrix2
    matrix2=matrixarr2
    # print(matrix1)
    # print(matrix2)
    

def addMatrix():
    # print(matrix1+matrix2) 
    sum=matrix1+matrix2
    resultlabel.configure(text=f"{sum}")


def subMatrix():
    # print(matrix1-matrix2)
    diff=matrix1-matrix2
    resultlabel.configure(text=f"{diff}")


def mulMatrix():
    
    mullist=[]
    # order=order

    for i in range(order):
        for j in range(order):
            mullist.append(matrix1[i]*matrix2[:,j])

    mularr=np.array(mullist)

    summedlist=[]

    for i in mularr:
        sum=0
        for j in i:
            sum+=j
        summedlist.append(sum)

    summedarr=np.array(summedlist).reshape(order,order)
    # print(summedarr)
    resultlabel.configure(text=f"{summedarr}")


orderlabel=Label(root,text="enter the order",font="Courier 22 bold")
orderlabel.pack()

orderbox=Entry(root,width=40)
orderbox.pack()
orderbox.focus_set()

ttk.Button(root, text= "Submit",width= 20, command= orderButton).pack(pady=20)



elementslabel=Label(root,text="",font="Courier 22 bold")
elementslabel.pack()

m1label=Label(root,text="")
m1label.pack()
m1box=Entry(root,width=40)
m1box.pack()
gap1=Label()
gap1.pack()

m2label=Label(root,text="")
m2label.pack()
m2box=Entry(root,width=40)
m2box.pack()
gap2=Label()
gap2.pack()

lollabel=Label(text="Dont forget to submit each time you change the values before performing the calculations!").pack()
matrixinputbtn=ttk.Button(root, text= "Submit Matrix",width= 20,command=inputmatrixgui).pack(pady=20)


addbtn=ttk.Button(root,text= "Add them",width= 20,command=addMatrix).pack(padx=20)
subbtn=ttk.Button(root,text= "Subtract them",width= 20,command=subMatrix).pack(padx=20)
mulbtn=ttk.Button(root,text= "Multiply them",width= 20,command=mulMatrix).pack(padx=20)

resultlabel=Label(root,text="Hi how are you",font="Courier 22 bold")
resultlabel.pack()




root.mainloop()