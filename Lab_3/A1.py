x1 = float(input("Введите x1: "))
y1 = float(input("Введите x2: "))
x2 = float(input("Введите y1: "))
y2 = float(input("Введите y2: "))


if x1 > 0 and y1 > 0:
    q1 = 1
elif x1 < 0 and y1 > 0:
    q1 = 2
elif x1 < 0 and y1 < 0:
    q1 = 3
else:
    q1 = 4

if x2 > 0 and y2 > 0:
    q2 = 1
elif x2 < 0 and y2 > 0:
    q2 = 2
elif x2 < 0 and y2 < 0:
    q2 = 3
else:
    q2 = 4


if q1 == q2:
    print("Yes,", end=" ")
    if q1 == 1:
        print("I")
    elif q1 == 2:
        print("II")
    elif q1 == 3:
        print("III")
    else:
        print("IV")
else:
    print("No")
