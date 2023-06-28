#program which implements stack through list
stack=[]
def push():
    if len(stack)==n:
        print("Satck overflow")
    else:
        element=input("Enter an element:")
        stack.append(element)
        print(stack)
def pop() :
    if len(stack)==0:
        print("Stack underflow")
    else:
        e=stack.pop()
        print("Removed element: ",e)
        print(stack)
def isFull():
    if len(stack)==n:
        print("Stack is full")
    else:
        print("Stack is not full")
def isEmpty():
    if len(stack)==0:
        print("Stack is empty.You can add upto {} elements".format(n))
    else:
        print("Stack is not empty")
n=int(input("Enter the limit of a STACK:"))
while True:
    print("Select the operation   1.Push   2.Pop   3.IsFull   4.IsEmpty   5.Quit")
    choice=int(input("Enter your choice [1,2,3,4,5] :"))
    if choice==1:
        push()
    elif choice==2:
        pop()
    elif choice==3:
f        isFull()
    elif choice==4:
        isEmpty()
    elif choice==5:
        print("Process was terminated successfully")
        break
    else:
        print("Input not recognized,Enter properly..")
