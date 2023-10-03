# Завдання 1        Беспятий Дмитро

a = int(input('введіть ціле число 1: '))
b = int(input('введіть ціле число 2: '))

if a < b:
    while a <= b:
        if a % 2 == 0:
            print(f'{a}')
        a += 1
elif a > b:
    while a >= b:
        if a % 2 == 0:
            print(f'{a}')
        a -= 1
else:
    print('числа рівні рішення немає')


# Завдання 2        Беспятий Дмитро

n = int(input('введіть ціле число n: '))
sum = 0
counter = 0

if 1 <= n <= 1000:
    while n <= 1000:
        if n % 3 == 0 or n % 5 == 0:
            print(n, end = ', ')
            sum += n
            counter += 1
        n += 1
else:
    print(f'число {n} знаходиться не в діапазоні "1 ≤ n ≤ 1000"')

print(f'\nсума чисел = {sum}, кількість всього чисел = {counter}')


# Завдання 3        Беспятий Дмитро

sum_plus = 0
sum_minus = 0
sum_zero = 0

while True:
    n = input('введіть значення n: ')

    if n == 'stop':
        break
    else:
        n = int(n)
        if n == 0:
            sum_zero += 1
        elif n < 0:
            sum_minus += 1
        elif n > 0:
            sum_plus += 1

print(f"кількість додатних чисел: {sum_plus}, кількість від'ємних чисел: {sum_minus}, кількість нулів: {sum_zero}")


# Завдання 4        Беспятий Дмитро

n = int(input('введіть кількість цілих чисел n: '))
max = 0
zero = 0

for i in range(n):
    n_number = int(input('введіть ціле число: '))
    i += 1
    if n_number == 0:
        zero += 1
    elif n_number > max:
        max = n_number

print(f'кількість введених нулів: {zero}, максимальне число: {max}')
