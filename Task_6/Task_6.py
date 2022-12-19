while (True):
    number_str = input("Введите номер билета ")
    try:
        number = int(number_str)
        if (number < 0):
            raise
        else:
            if (len(number_str) % 2 == 0):
                break
            else:
                # намерено оставил регистрозависимым
                if ((input("Длина номера не четная. Просчитать исключая центральную цифру?(Yes/No) ")) == "Yes"):
                    Odd = True
                    break
                else:
                    raise
    except:
        print("Неккоректный номер билета")
tmp_summ_left = 0
tmp_summ_right = 0
Odd = False
for i in range(int(len(number_str)/2)):
    tmp_summ_left += int(number_str[i])
    tmp_summ_right += int(number_str[-i-1])
print(str(tmp_summ_left)+"  " + str(tmp_summ_right))
if (tmp_summ_left == tmp_summ_right):
    if (Odd):
        print('билет "условно" счастливый')
    else:
        print("билет счастливый")
else:
    print("билет не счастливый")
