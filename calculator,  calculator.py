 # A basic Calculator🧮

while True:
    print("      Manu bar      ")
    c = input("What do you want me to do?\n\na) Addition\nb) Substraction\nc) Multiplication\nd) Division\n\nEnter according to the menu(a or b or c or d)\n--> ").lower()

    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))

    def add(a,b):
        print("Addition = ",a+b)

    def subs(a,b):
        print("Substraction = ",a-b)

    def mult(a,b):
        print("Multiplication = ",a*b)

    def divn(a,b):
        if(b == 0):
            print("It is not divisible")
        else:
            print("Division = ",a/b)

    def divm(a,b):
        if(b == 0):
            print("It is not divisible")
        else:
            print("Division = ",a%b)

    def divi(a,b):
        if(b == 0):
            print("It is not divisible")
        else:
            print("Division = ",a//b)

    if(c == "d"):
        d = input("what kind of division you want?\n\n1) Noraml division (quotient value)\n2) Modulo division (only reminder value)\n3) Division (intiger value)\n4) All\n\nEnter according to the menu(1 or 2 or 3 or 4)\n--> ").lower()

        if(d == "1"):
            divn(a,b)
        elif(d == "2"):
            divm(a,b)
        elif(d == "3"):
            divi(a,b)
        elif(d == "4"):
            divn(a,b)
            divm(a,b)
            divi(a,b)
        else:
            print("Wrong input")

    elif(c == "a"):
        add(a,b)

    elif(c == "b"):
        subs(a,b)

    elif(c == "c"):
        mult(a,b)

    else:
        print("Wrong input")

    Q=input("Do you want to use it further (yes/no): ").lower()
    if(Q=="no"):
        print("OK")
        print("THANK YOU😊")
        break
