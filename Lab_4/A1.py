import random
import time
cnt = 0
maxTime = 0
N = int(input("Введите количество примеров: "))
for i in range(N):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f"Вопрос {i+1}/{N}")
    start = time.time()
    num3 = int(input(f"{num1} × {num2} = "))
    end = time.time()
    e = end - start
    maxTime += e
    if num3 == num1*num2:
        print(f"Верно! (Время: {e:.2f} сек)")
        cnt += 1
    else:
        print(f"Неверно! Правильно: {num1*num2} (Время: {e:.2f} сек)")
sTime = maxTime/N
percent = (100 / N) * cnt
print("==================================================")
print("СТАТИСТИКА:")
print("==================================================")
print(f"Общее время: {maxTime:.2f} секунд")
print(f"Среднее время на вопрос: {sTime:.2f} сек")
print(f"Правильных ответов: {cnt}/{N}")
print(f"Процент правильных: {percent:.1f}%")
