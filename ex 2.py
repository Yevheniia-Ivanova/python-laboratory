print("Іванова Євгенія Сергіївна\nЛабораторна робота№1\nВаріант3\n2 Визначити чи існує трикутник та чи є він прямокутним.")
while True:
    d = str(input("Введіть yes якщо хочете виконати розрахунки:"))
    if d == "yes":
        a = float(input("Введіть значення кута 1: "))
        b = float(input("Введіть значення кута 2: "))
        if (a+b) == 90:
            print("Трикутник існує і є прямокутним")
        elif (a+b) >= 180 or (a+b) <= 0:
            print("Трикутник не існує")
        else:
            print("Трикутник існує, але не є прямокутним")
    else:
        raise SystemExit

