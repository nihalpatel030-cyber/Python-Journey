no = int (input("please enter number="))
rem=0
rev=0
original=no

while no>0:
rem=no % 10
rev=rev*10+rem
no=no//10

print(rev)
