
a=int (input("please enter a number=")) 
i = 1 
sum=0
while i<=a:
  print("1/",i,"+",end="") 
  sum=sum+(1/i) i+=1
  print("\b=",sum)
