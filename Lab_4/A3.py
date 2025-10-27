while True:
    subsequence = input("Введите последовательность из 0 и 1 (не меньше 5 символов): ")
    if len(subsequence) < 5:
        print("Ошибка: последовательность слишком короткая.")
        continue
    if not all(c in '01' for c in subsequence):
        print("Ошибка: используйте только символы 0 и 1.")
        continue
    break

kolvo_packets = len(subsequence)
lost_packets = subsequence.count('0')

max_loss_streak = 0
current_streak = 0
for i in subsequence:
    if i == '0':
        current_streak += 1
        if current_streak > max_loss_streak:
            max_loss_streak = current_streak
    else:
        current_streak = 0

loss_percent = (lost_packets / kolvo_packets) * 100  # процент потерь

if loss_percent <= 1:
    quality = "Отличное качество"
elif loss_percent <= 5:
    quality = "Хорошее качество"
elif loss_percent <= 10:
    quality = "Удовлетворительное качество"
elif loss_percent <= 20:
    quality = "Плохое качество"
else:
    quality = "Критическое состояние сети"

print("\nРЕЗУЛЬТАТЫ АНАЛИЗА:")
print(f"• Общее количество пакетов: {kolvo_packets}")
print(f"• Количество потерянных пакетов: {lost_packets}")
print(f"• Длина самой длинной последовательности потерянных пакетов: {max_loss_streak}")
print(f"• Процент потерь: {loss_percent:.1f}%")
print(f"• Качество связи: {quality}")

