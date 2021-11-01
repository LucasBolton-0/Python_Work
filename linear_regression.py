#method_of_least_squares.py

#lists of data point value pairs by dimension

x_values = [0, 10, 20, 30, 40]

y_values = [32.4, 26.0, 18.1, 13.2, 9.0]




#list length

total_x_values = len(x_values)

total_y_values = len(y_values)

### 'a' constant ###

#cross products

# Tests whether each (x,y) value pair is represented

if len(x_values) == len(y_values):

# Sum of cross products

    a = -1
    b = 0

    cross_products = []
    while a <= len(x_values) and b <= (len(x_values) - 1):
        a = a + 1
        b = b + 1
        for number in x_values[a:b]:
            for number2 in y_values[a:b]:
                c = float(number*number2)
                cross_products.append(c)

    aa = sum(cross_products)

#number of value pairs time cross products

n_times_cross_products = total_x_values * aa

#Sum of x and y values

sum_x_values = sum(x_values)

sum_y_values = sum(y_values)

#square of x values

squared_x_values = []

for value in x_values:
    x_squared = value**2
    squared_x_values.append(x_squared)

#sum of square of x values

sum_of_squared_x_values = sum(squared_x_values)

#total number of value pairs time sum of squared of x values

n_times_sum_of_squared_x_values = total_x_values * sum_of_squared_x_values

#square of the sum of x values
#(sigma x_sub_n)**2

square_of_sum_x_values = sum_x_values ** 2

#numerator for 'a' constant
#n time cross products minus sum of x values time sum of y values

numerator_a = n_times_cross_products - (sum_x_values * sum_y_values)

#denominator for 'a' constant
#n times sum of square of x values minus square of sum of x values

denominator_a = n_times_sum_of_squared_x_values - square_of_sum_x_values

#'a'

constant_a = numerator_a / denominator_a

### 'b' constant ###

#numerator_b
# sum of y values minus 'a' times sum of x values

numerator_b = sum_y_values - (constant_a * sum_x_values)

#denomminator_b
#denominator of constant 'b' is 'n'

denominator_b = total_y_values

constant_b = numerator_b / denominator_b

print("constant a: " + str(round(constant_a, 5)))
print("constant b: " + str(round(constant_b, 5)))
print("---")
print("linear regression equation: " + "y" + "= " + (str(round(constant_a, 5)))
    + "x " + "+ " + (str(round(constant_b, 5))))
print("---")
