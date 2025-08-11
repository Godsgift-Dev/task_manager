#Ask user to input the length of the 3 sides of a triangle
x = float(input("Enter the first side:\n" ))
y = float(input("Enter the second side:\n" ))
z = float(input("Enter the third side:\n" ))
# if all sides are equal print Equilateral
if x == y == z: 
    print("Equilateral")
# if 2 sides are equal print Isoceles
elif x == y or y == z or x == z:
    print ("isosceles")
# if no sides are equal print Scalene
    print ("Scalene")


