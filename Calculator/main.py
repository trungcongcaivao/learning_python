import os

def add(x,y):                                  #define function
    return x + y
def minus(x,y):
    return x - y
def multi(x,y):
    return x * y
def divide(x,y):
    return x / y
print("mode:")                                  #choose mode
print("1. add")
print("2. minus")
print("3. multi")
print("4. divide")
while True:                                     #main
    mode = str(input("Choose mode:..."))
    if mode in ('1','2','3','4'):
        while True:
            try:                                #try correct input
                n1 = float(input("first number = "))
                n2 = float(input("second number = "))
            except ValueError:
                print("invalid value")
                continue
            else:
                break
        if mode == "1":
            print("result = ",add(n1,n2))
        elif mode == "2":
            print("result = ",minus(n1,n2))
        elif mode == "3":
            print("result = ",multi(n1,n2))
        elif mode == "4":
            if n2 == 0:
                print("can't divide 0")
            else:
                print("result = ",divide(n1,n2))
    else:
        print("invalid mode")
    cont = str(input("Continue?...(press any key to continue, press Q to quit)  ")) #continue chosing
    if cont == "q" or cont == "Q":
        break
    os.system('cls')