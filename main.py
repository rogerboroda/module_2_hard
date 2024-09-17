while True:
    result = []  # Пароль
    i = int(input('Введите число от 3 до 20: '))
    if i > 2 and i < 21:  # Число в первом поле от 3 до 20
        for j in range(1, i):  # Первое число суммы
            for n in range(1, i):  # Второе число суммы
                if i % (j + n) == 0 and j < n:
                    result.append(j)
                    result.append(n)
    else:
        print("¯¯¯VVVVVVVVVV¯¯¯ Шипы сверху уже движутся на вас.")
        continue
    print("password: ", *result)