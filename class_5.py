# r W >
class_5 = print
name = input("Enter Your Name")
year = int(input("Enter year"))
marks = int(input("Enter Your to see Your CGPA   "))
if name == "Rifat":
    class_5("Your name is Rifat")
else:
    class_5("Your name is not here")

if year % 100 == 5 or year % 4 == 0:
    class_5("This  year is leap year")
else:
    class_5("This year is not leap year")

if marks==0 or marks>100:
    class_5('Undefiend');
elif marks>=80 and marks<=100:
    class_5('A+')
elif marks>=70 and marks<=79:
    class_5('A')
elif marks>=60 and marks<=69:
    class_5('A+')
elif marks>=50 and marks<=59:
    class_5('A-')
elif marks>=40 and marks<=49:
    class_5('B')
elif marks<=39 and marks>=33:
    class_5('B-')
else:
    class_5('Fail');
#py class_5.py

