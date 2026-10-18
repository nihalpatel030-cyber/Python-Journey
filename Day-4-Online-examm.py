right=0
wrong=0
skip=0
attempt=0

print("(Q1) 5x2= ?")
print("(a)5 (b)20 (c)10 (d)skip")

answer=(input("your choice="))
if  answer == 'a':
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "b":
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "c":
right +=1
attempt+=1
print("answer is right")
elif answer == "d":
skip+=1
print("answer is skip")

print("(Q2) 1+9= ?")
print("(a)4 (b)9 (c)10 (d)skip")

answer=(input("your choice="))
if  answer == 'a':
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "b":
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "c":
right +=1
attempt+=1
print("answer is right")
elif answer == "d":
skip += 1
print("you skip answer")

print("(Q3) 5x3= ?")
print("(a)5 (b)20 (c)15 (d)skip")

answer=(input("your choice="))
if  answer == 'a':
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "b":
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "c":
right +=1
attempt+=1
print("answer is right")
elif answer == "d":
skip += 1
print("answer is skip")

print("(Q4) 5+4= ?")
print("(a)5 (b)9 (c)10 (d)skip")

answer=(input("your choice="))
if  answer == 'a':
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "b":
right +=1
attempt+=1
print("answer is right")
elif answer == "c":
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "d":
skip +=1
print("answer is skip")

print("(Q5) 5x4= ?")
print("(a)5 (b)50 (c)20 (d)skip")

answer=(input("your choice="))
if  answer == 'a':
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "b":
wrong +=1
attempt+=1
print("answer is wrong")
elif answer == "c":
right +=1
attempt+=1
print("answer is right")
elif answer == "d":
skip+=1
print("answer is skip")

print(wrong,"=wrong")
print(skip,"=skip")
print(right,"=right")
print(attempt,"=attempt")

totalright = right * 10
totalwrong = wrong * 10
totalmarks = totalright - totalwrong

print("rightMarks=",totalright)
print("wrongMarks=",totalwrong)

print("total marks=",totalmarks)
