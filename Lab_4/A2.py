#ПРЯМОУГОЛЬНИК
# n = int(input("Введите количество строк: "))
# m = int(input("Введите количество столбцов: "))
# for i in range(n):
#  for j in range(m):
#      print("#", end='')
#   print()

def draw_rectangle(rows, columns, ch):
    for i in range(rows):
     for j in range(columns):
         print(ch, end='')
     print()
draw_rectangle(5, 10, '#')

print()
# ТРЕУГОЛЬНИК
# n = int(input("Введите количество строк: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("#", end='')
#     print()

def draw_triangle(rows, ch):
    for i in range(1,rows+1):
     for j in range(i):
         print(ch, end='')
     print()
draw_triangle(5, '#')

print()
# РАМКА
# n = int(input("Введите количество строк: "))
# m = int(input("Введите количество столбцов: "))
# print("#"*m)
# for i in range(n - 2):
#     print("#", end='')
#     for j in range(m - 2):
#         print(" ", end='')
#     print("#")
# if n > 1:
#     print("#" * m)

def draw_frame(rows, columns, ch):
    print(ch * columns)
    for i in range(rows-2):
        print(ch, end='')
        for j in range(columns-2):
            print(" ", end='')
        print(ch)
    if rows > 1:
        print(ch * columns)
draw_frame(5, 10, '#')