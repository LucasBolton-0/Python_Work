# This program computes the Correlation
# Coefficient (Perason's 'r') and the
# Coefficient of Determination ('r' squared).

# list of x and y values
# x-values = list_0
# y-values = list_1

list_0 = [5, 10, 4 8, 2, 7, 9, 6, 1, 12]
list_1 = [5, 2, 8, 3, 8, 5, 5, 7, 10, 3]

# sum of x-values and sum of y-values

sum_x_values = sum(list_0)
sum_y_values = sum(list_1)

# 'n' total number of sample (x,y) value pairs

n = len(list_0)
n_minus_1 = (n - 1)

# Standard deviation of x-values

x_bar_x = sum_x_values/ n

list_3 = []
for value in list_0:
    output = (value - x_bar_x)**2
    list_3.append(output)

d = (float(sum(list_3)/n_minus_1))
e = d**0.5

# standard deviation of y-values

x_bar_y = sum_y_values/ n

list_4 = []
for value1 in list_1:
    output1 = (value1 - x_bar_y)**2
    list_4.append(output1)

f = (float(sum(list_4)/n_minus_1))
g = f**0.5

# Cross products

# Tests whether each (x,y) value pair is represented

if len(list_0) == len(list_1):

# Sum of cross products

    a = -1
    b = 0

    list_5 = []
    while a <= len(list_0) and b <= (len(list_0) - 1):
        a = a + 1
        b = b + 1
        for number in list_0[a:b]:
            for number2 in list_1[a:b]:
                c = number*number2
                list_5.append(c)
    aa = sum(list_5)

    # Computing Pearson's r

    # Numerator of Pearson's r

    h = (1/len(list_0))
    i = h * (sum_x_values) * (sum_y_values)
    r_numerator = aa - i

    # Denominator of Pearson's r

    r_denominator = (n_minus_1) * (e) * (g)

    # Pearson's r
    # r squared

    r = (r_numerator) / (r_denominator)

    print('---')
    print("Correlation Coefficient     " + "    [r]: " + str(round(r, 3)))
    print("Coefficient of Determination [r**2]: " + str(float(round(r**2, 3))))
    print('---')

else:
    print('---')
    print('Number of elements in list_0 and list_1 is not equal.')
    print('---')
