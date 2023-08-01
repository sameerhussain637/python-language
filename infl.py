a=input("enter the value")
# b=input("enter the value")

a=int(a)
# b=int(b)

if(type(a)== int  or type(a)== float):
    if(a%2==0):
        print("it is even")
    else:
        print("it is odd")
else:
    print("it is nor int ")