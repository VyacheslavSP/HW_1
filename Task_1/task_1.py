while (True):
    number_str = input("Введите трехзначное число ")
    try:
        number = int(number_str)
        if (100 <= abs(number) <= 1000):
            tmp_num = abs(number)
            break
        else:
            raise
    except:
        print("Неккоректный ввод числа")
result = 0
while (tmp_num > 0):
    result += tmp_num % 10
    tmp_num //= 10
print(result)
