no = int (input("please enter number="))
sum=0
a=no

while no>0:
digit=no % 10
sum=sum+digit
no=no//10

print("digit sum=",sum)

if a % sum ==0:
print("this is nevine number")
else:
print("this is not nevine number")
