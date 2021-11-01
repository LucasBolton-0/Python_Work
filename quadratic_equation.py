#quadratic_equation.py

import math

print("ax^2 + bx + c")

a = float(input("constant a: "))
b = float(input("constant b: "))
c = float(input("constant c: "))

A = -1 * b
B_1 = (b**2)
B_2 = (4 * a * c)
B_3 = B_1 - B_2

if B_3 < 0:
    print("Equation has no real roots")

else:

    B_4 = math.sqrt(B_3)
    C = 2 * a

    D = A + B_4
    E = A + (-1 * B_4)

    F = D / C
    G = E / C

    zero_1 = F
    zero_2 = G

    print("---")
    print("root one: " + str(round((zero_1), 5)))
    print("root two: " + str(round((zero_2), 5)))
    print("---")
