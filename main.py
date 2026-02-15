m = int(input("enter your score in maths :"))
b = int(input("enter your score in biology :"))
e = int(input("enter your score in english :"))
total = m + b + e
print("your total is",total)
p = total / 3
print("your percentage is",p)
if p >=90 :
    print("your grade is A1")
elif p>=80 :
    print(" your grade is A2")
elif p>=70 :
    print(" your grade is B1")
elif p>=60 :
    print(" your grade is B2")
elif p>=50 :
    print(" your grade is C")
else :  
    print(" your grade is F ")




