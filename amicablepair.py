# This program computes all of the numbers that
# have an amicable counterpart between 1 and 10000

a = 0
while a < 10000:
    a = a + 1
    c = 1

    list_0 = []

    while c <= a:
        d = a % c
        c = c + 1
        if d == 0:
            list_0.append(int(c - 1))
    e = len(list_0)

    sum1 = int(sum(list_0) - a)

    list_2 = []

    f = 1
    while f <= sum1:
        g = sum1 % f
        f = f + 1
        if g == 0:
            list_2.append(int(f - 1))

    sum2 = int(sum(list_2) - sum1)

    if a == sum2 and sum1 != sum2:
        print('---')
        print(": " + str(a))
        print(sum1)
        print(sum2)

print(" ")

print('---')
