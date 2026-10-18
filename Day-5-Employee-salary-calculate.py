basic=int(input("enter a employee salary="))

DA= basic*50/100
HRA=basic*10/100
medical=basic*4/100
gross_salary=basic+DA+HRA+medical
pf= gross_salary*5/100
insurance= gross_salary*7/100
deduction=pf+insurance
netsalary=gross_salary-deduction

print("DA=",DA)
print("HRA=",HRA)
print("medical=",medical)
print( "gross_salary",gross_salary )
print("pf=",pf)
print("insurance=",insurance)
print("deduction=",deduction)
print("netsalary=",netsalary)
