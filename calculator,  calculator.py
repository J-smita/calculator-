# A basic Calculator🧮
def add(a,b):
    return a+b
def subs(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if(b==0):
        print("ERROR")
    else:
        return a/b
    
"""Manu Bar"""
while True:
    print("1-> Add")
    print("2-> Substract")
    print("3-> Multiplication")
    print("4-> Divide")
    q=input("Enter according to the manu(1-4)->")

    if(q=="1"):
        c=float(input("Enter no1="))
        d=float(input("Enter no2="))
        print(add(c,d))
    elif(q=="2"):
        c=float(input("Enter no1="))
        d=float(input("Enter no2="))
        print(subs(c,d))
    elif(q=="3"):
        c=float(input("Enter no1="))
        d=float(input("Enter no2="))
        print(mult(c,d))
    elif(q=="4"):
        c=float(input("Enter no1="))
        d=float(input("Enter no2="))
        print(div(c,d))
    else:
        print("INVALID")
        
    Q=input("Do you want to use it further (yes/no)").lower()
    if(Q=="no"):
        print("OK")
        print("THANK YOU😊")
        break
