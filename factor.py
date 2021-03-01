a = int(input("Please input any integer number, the "
                "factors of which you would like to "
                "know: "))

c = 1

list_0 = []

while c <= a:
    d = a % c
    c = c + 1
    if d == 0:
        list_0.append(int(c - 1))

print("Factors of " + str(a) + ": " + str(list_0))

length = int(len(list_0))

print('---')

if (length/2) % 2 == 0:
    e = len(list_0)
    f = int(e)/2
    g = int(f)

    aaa = 0
    bbb = int(e) - 1
    while aaa <= (g - 1) or bbb >= f:
        print(str(a) + " = " + (str(int(list_0[aaa])) + " x " + str(int(list_0[bbb]))))

        aaa = aaa + 1
        bbb = bbb - 1

    print('---')

    print(len(list_0))

if (length/2) % 2 != 0:
    e = len(list_0)
    h = e + 1
    k = h / 2
    middle = k - 1
    p = (len(list_0)/2) + 1
    f = (int(e)/2) - 0.5
    g = int(f)

    aaa = 0
    bbb = int(e) - 1
    while aaa <= (g) or bbb >= f:
        print(str(a) + " = " + (str(int(list_0[aaa])) + " x " + str(int(list_0[bbb]))))

        aaa = aaa + 1
        bbb = bbb - 1

    print('---')

    print(len(list_0))
