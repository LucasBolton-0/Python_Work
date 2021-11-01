#free_fall.py

import math

one = "Distance as a function of time"
two = "Time as a function of distance"

print(one)
print(two)

print("Enter A for one, B for two.")

choice = str(input())

list = []

list.append(choice)

if choice == A:
    time_1 = float(input("Please input time (sec): "))

    distance_1 = (4.905 * (time_1**2))
    print(distance_1)


if choice == B:
    distance_2 = float(input("Please input distance measure: "))

    time_2 = math.sqrt((distance_2) / 4.905)
    print(time_2)
