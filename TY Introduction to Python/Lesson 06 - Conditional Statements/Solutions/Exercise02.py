# Lesson 06 - Exercise 02
# Task 01

marks = int(input("What mark did you get on the exam? "))

if marks < 25:
    print("Grade F")
elif marks < 45:
    print("Grade E")
elif marks < 50:
    print("Grade D")
elif marks < 60:
    print("Grade C")
elif marks < 80:
    print("Grade B")
else:
    print("Grade A")

# Task 02
items = int(input("How many items are you buying? "))
if items >= 1000:
    cost = items * 100
    discount = cost / 10
    total = cost - discount
    print("Your total cost with 10 percent discount applied is ",total," Euro")
else:
    cost = items * 100
    print("Your total cost is ",cost," Euro")

#Task 02
print("The Categories of vehicles are \nCar = c\nMotorbike = m\nbus = b\nTruck = t \nVan = v")
cat = str(input("Please choose category of vehicle "))
if cat == "c":
    print("The toll value is €2.00")
elif cat == "m":
    print("The toll value is €1.10")
elif cat == "b":
    print("The toll value is €4.25")
elif cat == "t":
    print("The toll value is €6.70")
elif cat == "v":
    print("The toll value is €4.00")