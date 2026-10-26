a = int (input("enter a number="))
print("odd\teven",end="\n")
for i in range (1,a+1):
if i % 2!=0:
print(i,end="\t")

elif i % 2==0:  
    print(i)
