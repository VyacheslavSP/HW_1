while (True):
    number_str = input("Введите общее число журавликов ")
    try:
        number = int(number_str)
        # меньше 6 сделать невозможно,число должно быть кратно 6 при условии целых журавликов
        if (number >= 6 and number % 6 == 0):
            break
        else:
            raise
    except:
        print("Неккоректное число журавликов")
print(number_str+"->"+str((number//6))+" " +
      str((4*(number//6)))+" " + str((number//6)))
