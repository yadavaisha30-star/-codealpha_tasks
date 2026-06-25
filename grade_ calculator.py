print("=" * 40)
print("      STUDENT GRADE CALCULATOR")
print("=" * 40)

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

print("\nEnter marks out of 100")

sub1 = float(input("English: "))
sub2 = float(input("Maths: "))
sub3 = float(input("Science: "))
sub4 = float(input("Computer: "))
sub5 = float(input("Hindi: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
    result = "Excellent"
elif percentage >= 80:
    grade = "A"
    result = "Very Good"
elif percentage >= 70:
    grade = "B"
    result = "Good"
elif percentage >= 60:
    grade = "C"
    result = "Average"
elif percentage >= 50:
    grade = "D"
    result = "Pass"
else:
    grade = "F"
    result = "Fail"

print("\n" + "=" * 40)
print("         STUDENT REPORT")
print("=" * 40)
print("Name       :", name)
print("Roll No.   :", roll)
print("Total Marks:", total, "/ 500")
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("Result     :", result)
print("=" * 40)