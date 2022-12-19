# требуется определить, можно ли от шоколадки рамером mxn долек отломить k долек, если разрешается сделать один разлом прямой между дольками
class MyError(Exception):
    def __init__(self, text):
        self.txt = text


while (True):
    start = -1
    count = 0
    number_str = input(
        "Введите размер шоколадки(длина x ширина) и количество долек через разделитель ';'")
    try:
        while True:
            start = number_str.find(";", start+1)
            if start == -1:
                break
            count += 1
        if (count != 2):
            raise MyError(
                "В строке не корректное число разделителей. повторите ввод")
        else:
            tmp_string = number_str.split(";")
            len = int(tmp_string[0])
            width = int(tmp_string[1])
            pieces = int(tmp_string[2])
            if (len < 1 or width < 1 or pieces < 1):
                raise MyError(
                    "парметр не может быть меньше 1. повторите ввод")
            else:
                break
    except ValueError:
        print("Неккоректный параметр")
    except MyError as mr:
        print(mr)
correct = False
if (pieces >= min(len, width)):
    i = 1
    j = 1
    while (i <= len):
        if (width*i == pieces):
            correct = True
            break
        i += 1
        while (j < width):
            if (width*i == pieces):
                correct = True
                break
            j += 1
else:
    correct = False     # излишняя строка, по умолчанию Ложь
if (correct):
    print("Разделить можно")
else:
    print("Разделить нельзя")
