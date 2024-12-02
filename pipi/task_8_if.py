# проверка + или - числа

num = 5
if num >=0:
    print('Число больше или равно 0')
else:
    print('Число отрицательное')


def task(str_1, str_2):
    if str_1 in str_2:
        print("Yes")
    else:
        print ("No")
task(str_1='test',str_2='test2')

num_float=-9.4
if num_float > 0:
    print('+ число')
elif num_float == 0:
    print('0')
else:
    print('- число')

permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def zvanie(kurs: int):
    if kurs==1 or kurs==2 or kurs==3 or kurs==4:
        print("бакалавр")
    elif kurs in range(5,7):
        print("магистр")
    elif 7<=kurs<=9:
            print("аспирант")
    else:
        print ("Введите корректный год обучения")
zvanie(3)