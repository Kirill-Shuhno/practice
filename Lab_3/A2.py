import string

password = input("Enter password: ")

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
ok = True

if len(password) != 8:
    print("Длина пароля не равна 8")
    ok = False

if password.lower() == password:
    print("В пароле отсутствуют заглавные буквы")
    ok = False

if password.upper() == password:
    print("В пароле отсутствуют строчные буквы")
    ok = False

if not any(ch.isdigit() for ch in password):
    print("В пароле отсутствуют цифры")
    ok = False

if not any(ch in "*-#" for ch in password):
    print("В пароле отсутствуют специальные символы")
    ok = False

if not all(ch in allowed for ch in password):
    print("В пароле используются непредусмотренные символы")
    ok = False

if ok:
    print("Надежный пароль")
