n = int(input("Ваедите номер карты: "))
length = len(str(n))
n_str = str(n)
first_cnt = 0
second_cnt = 0
if length in [13, 15, 16]:

        for i in range(length-2, -1, -2):
            a = int(n_str[i])*2
            if a > 9:
                a -= 9
            first_cnt += a
        for i in range(length-1, -1, -2):
            second_cnt += int(n_str[i])

        control_procedure = first_cnt+second_cnt

        if control_procedure % 10 == 0:

            if n_str[:2] == '34' or n_str[:2] == '37':

                print(f"{n} - American Express")
            elif n_str[:2] == '51' or n_str[:2] == '52' or n_str[:2] == '53' or n_str[:2] == '54' or n_str[:2] == '55':

                print(f"{n} - MasterCard")
            elif n_str[0] == '4':

                print(f"{n} - Visa")
            else:
                print("the card is invalid")
        else:
            print("the card is invalid")
else:
    print("the card is invalid")