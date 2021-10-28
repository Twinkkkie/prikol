def calc(a, b):
    q = input('Введите знак: ')
    if q == '+':
        res = a + b
    elif q == '-':
        res = a - b
    elif q == '/':
        res = a / b
    elif q == '*':
        res = a * b
    else:
        print('Вы ввели не тот знак')
    return res


num_1 = int(input('Введие первое число: '))
num_2 = int(input('Введие второе число: '))
result = calc(num_1, num_2)
print(result)
