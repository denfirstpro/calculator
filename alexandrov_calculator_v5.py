d = "да"
while d == "да" :
    a = input("Введите первое число без пробела в начале,конце(не забывайте,что анализ вещественного числа провести невозможно)")
    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False
    while (is_number(a)) == False:     #честно я понятия не имею как это работает,я взял этот способ из интернета так как не знаю,каким другим способом можно проверить является ли строка числом.
        print("Введите пожалуйста число")
        a = input()
    a = float(a)
    ghb = 123
    while ghb == 123:
        c = input("Введите знак действия без пробела в начале,конце(если не знаете знаки то введите 'действия'")
        if c == "+" or c == "-" or c == "//" or c == "%" or c == "/" or c == "*" or c == "**" or c == "///" or c == "действия" or c == "анализ" or c == "перевод":
            if c == "анализ":
                abc = a
                bca = int(a)
                if abc == bca:
                    a = int(a)
                    dx = a
                    y = 0
                    while (dx // 10) < dx:
                        dx = dx // 10
                        y = y + 1
                    print("число разрядов в числе =", y)
                    om = a
                    a = str(a)
                    om = str(om)
                    lp = len(om) + 1 
                    a = int(a)
                    om =str(om)
                    while len(om) != 1:
                        lp = lp - 1 
                        om = int(om)
                        print(om % 10, ",", lp, "цифра", a)
                        om = om // 10
                        om = str(om)
                    om = int(om)
                    print(om , ",", "1", "цифра", a)  
                    rt = a
                    if rt % 2 == 0:
                        print("число четное")
                    else:
                        print("число нечетное")
                    p = 0
                    pc = a
                    pc = str(pc)
                    while len(pc) != 1:
                        pc = int(pc)
                        n = pc % 10
                        pc = pc // 10
                        p = p + n
                        pc = str(pc)
                    pc = int(pc)
                    print("Сумма цифр числа =", p + pc)
                    r = 1
                    nc = 0
                    while r != a:
                        r = r + 1
                        if a % r == 0 and r != a:
                            print(r, "делитель", a)
                            nc = nc + 1
                    if nc == 0:
                        print(a, "простое число")
                    hf = a
                    hf = int(hf)
                    v = hf ** 2
                    v = str(v)
                    if "." not in v:
                        print("число является полным квадратом:", v)
                    else:
                        print("Число не является полным квадратом какого либо числа")
                    yt = a
                    u = yt ** 3
                    u = str(u)
                    if "." not in u:
                        print("число является полным кубом:", u)
                    else:
                        print("Число не является полным кубом какого либо числа")
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                else:
                    print(a, "вещественное число")
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
            if c == "действия":
                print("+ сложение;- вычитание;* умножение;/ деление;// целочисленное деление;% взятие остатка;** возведение в степень;/// взятие квадратного корня первого числа;анализ анализ числа")
                c = input()
            if c == "///":
                print("корень из", a, "=", a ** 0.5)
                print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                d = input()
            if c == "перевод":
                nbv = a
                a = int(a)
                print(nbv, "при переводе в десятичную систему =", a)
                print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                d = input()
            if c == "+" or c == "-" or c == "//" or c == "%" or c == "/" or c == "*" or c == "**":
                b = input("Введите второе число без пробела в начале,конце")
                def is_number(str):
                    try:
                        float(str)
                        return True
                    except ValueError:
                        return False
                while (is_number(b)) == False:     #честно я понятия не имею как это работает,я взял этот способ из интернета так как не знаю,каким другим способом можно проверить является ли строка числом.
                    print("Введите пожалуйста число")
                    b = input()
                b = float(b)
                while b == 0 and c == "/" or b == 0 and c == "//" or b ==0 and c == "%":
                    print("на ноль делить нельзя,введите другое число")
                    b = input("Введите второе число без пробела в начале,конце")
                    def is_number(str):
                        try:
                            float(str)
                            return True
                        except ValueError:
                            return False
                    while (is_number(b)) == False:     #честно я понятия не имею как это работает,я взял этот способ из интернета так как не знаю,каким другим способом можно проверить является ли строка числом.
                        print("Введите пожалуйста число")
                        b = input()
                    b = float(b)
                if c == "+":
                    print(a, "+", b, "=", a + b)
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                    ghb = 121
                if c == "-":
                    print(a, "-", b, "=", a - b)
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                    ghb = 121
                if c == "/":
                    print(a, "/", b, "=", a / b)
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                    ghb = 121
                if c == "//":
                    print(a, "//", b, "=", a // b)
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                    ghb = 121
                if c == "%":
                    print(a, "%", b, "=", a % b)
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                    ghb = 121
                if c == "**":
                    print(a, "в степени", b, "=", a ** b)
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                    ghb = 121
                if c == "*":
                    print(a, "*", b, "=", a * b)
                    print("Если желаете продолжить введите да,если нет то любое другое слово,букву")
                    d = input()
                    ghb = 121
            else:
                print("введите пожалуйста знак действия,вы можете ознакомится с ними,если введете 'действия'")
                ghb = 123
else:
    print("Спасибо,что использовали программу, до свидания.")
