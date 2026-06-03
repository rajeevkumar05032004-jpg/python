# Linear Equation Solver (2 variables)

# Taking input from user
a1 = int(input("Enter coefficient of x in eq1: "))
b1 = int(input("Enter coefficient of y in eq1: "))
c1 = int(input("Enter constant of eq1: "))
a2 = int(input("Enter coefficient of x in eq2: "))
b2 = int(input("Enter coefficient of y in eq2: "))
c2 = int(input("Enter constant of eq2: "))
# Determinant
D = a1*b2 - a2*b1
Dx = c1*b2 - c2*b1
Dy = a1*c2 - a2*c1
# Checking solution
if D != 0:
    x = Dx / D
    y = Dy / D
    print("Solution:")
    print("x =", x)
    print("y =", y)
else:
    print("No unique solution exists")