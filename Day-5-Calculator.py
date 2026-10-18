A=int(input("please enter a 1st value="))
B=int(input("please enter a 2nd value="))
print("Your Option")
print("(1)sum")
print("(2)sub")
print("(3)mul")
print("(4)div")

d=int(input("enter your choice:"))
if d==1:
    print("sum=",A+B)
elif d==2:
    print("sub=",A-B)
elif d==3:
    print("mul=",A*B)
elif d==4:
    print("div=",A/B)    
