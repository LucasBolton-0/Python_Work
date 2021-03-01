# This program detemines and prints all
# of the prime numbers between 1 and 100
# through exhaustive enumeration. As well,
# it prints the total number of prime numbers
# between 1 and 100.


list_2 = []

s_number = 0
end_number = 100

while s_number < end_number:
    s_number = s_number + 1

    list_0 = []
    a = s_number
    n = 1
    while n <= a:
        output = a % n
        n = n + 1
        if output == 0:
            list_0.append(output)

    list_1 = []
    if len(list_0) == 2:
        list_1.append(a)

        for value in list_1:
            list_2.append(value)

print(list_2)
print("Total number of prime numbers between 1 and " +
    str(end_number) + ": [" + str(len(list_2)) + "]")
