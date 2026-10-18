name = input("Enter student name: ")

english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))

total = english + maths + python
percentage = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 80:
    print("Grade A")

elif percentage >= 60:
    print("Grade B")

elif percentage >= 35:
    print("Grade C")

else:
    print("Fail")
