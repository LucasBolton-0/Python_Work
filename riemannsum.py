# This program computes the Riemann sum. Enter
# and format any equation below and change the
# subinterval count to increase or decrease
# Riemann sum accuracy.

# If Riemann sum value is smaller or larger than expected,
# double-check that all four intsances of your equation
# have been entered fully and formatted correctly.


# x_sub_1 value and x_sub_2 value

x_1 = float(input("Please enter lower x-value of interval:  "))

x_2 = float(input("Please enter upper x-value of interval:  "))

# Number of subintervals

subintervals = 1000000

# Equation: must be entered twice here; once each
# for x_sub_1 value and x_sub_2 value. Equation must
# be entered a total of four times.


e = 2.718281828

y_1 = (x_1)**3

y_2 = (x_2)**3

# Riemann sum approximation using a single
# Trapezoid area formula. Very innaccurate for
# higher order polynomial equations and for a
# large x-value range.

print("y_1 = " + str(y_1))
print("y_2 = " + str(y_2))

x_d = x_2 - x_1
y_d = y_2 - y_1

a = y_1 * x_d
b = x_d * y_d * 0.5
a_plus_b_t = a + b

# List to store subinterval area output values

list_0 = []

# while loop to compute area of each subinterval.

while x_1 < (x_2 - (x_1/subintervals)):

    x_1 = x_1
    x_3 = x_1 + (x_d/subintervals)

    y_1 = (x_1)**3
    y_3 = (x_3)**3

    x_d_1 = x_3 - x_1
    y_d_1 = y_3 - y_1

    a = y_1 * x_d_1
    b = x_d_1 * y_d_1 * 0.5
    a_plus_b_r = a + b
    list_0.append(a_plus_b_r)

#    print(a_plus_b_r)

    x_1 = x_1 + (x_d/subintervals)

# Prints Riemann sum value

print(' ')
print('---')
print("Riemann Sum; 1,000,000 subintervals: " + str(sum(list_0)))
print('---')

# The Trapezoid function computes the approximate (relative)
# area under the curve between some [x_1, x_2]
# interval. Function value is only useful for approximating
# area for relatviely small intervals. Determining whether
# the equation has been entered correctly can potentially be
# diagnosed by comparing the trapezoidal area to the
# Riemann sum value. On a small interval, if the functions
# within the while loop have been incorrectly entered, the
# trapezoidal area may be a better approxiamtion and thus
# likely necessitate equation reformatting of one of the
# instances of the equation in the program.

print(' ')
print('---')
print("Area approxiamtion using single Trapezoid formula: " + str(a_plus_b_t))
print('---')
