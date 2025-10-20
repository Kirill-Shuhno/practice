previous = int(input("Сколько куб. метров в прошлом месяце: "))
now = int(input("Сколько куб. метров в этом месяце: "))
now1 = now
if now < previous:
    now+=10000
used = now-previous
money = 0
if used <= 300:
    money = 21
elif used <= 600:
    money = 21 + (used - 300) * 0.06
elif used <= 800:
    money = 21 + 300 * 0.06 + (used - 600) * 0.04
else:
    money = 21 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025
print(f"{'Предыдущее':<12}{'Текущее':<10}{'Использовано':<15}{'К оплате':<10}{'Ср. цена m^3':<12}")
print(f"{previous:<12}{now1:<10}{used:<15}{round(money, 2):<10}{round(money/(now-previous),2):<12}")