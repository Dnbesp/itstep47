# # Завдання 1        Беспятий Дмитро
#
# number = input('введіть чотиризначне число: ')
# len = len(number)
# number = int(number)
#
# if len > 4 or len < 4:
#     lucky_number = 'введене число не є чотиризначним'
# else:
#     number_1 = number // 1000
#     number_2 = number // 100 % 10
#     number_3 = number // 10 % 10
#     number_4 = number % 10
#     lucky_number = 'щасливе число' if number_1 + number_2 == number_3 + number_4 else 'введене число є не щасливим'
#
# print(f'lucky_number = {lucky_number}')
#
#
# # Завдання 2         Беспятий Дмитро
#
# height = float(input('введіть значення зросту в метрах: '))
# mass = float(input('введіть значення маси в кілограмах: '))
# index = round(mass / (height * height), 2)
#
# if index < 18.5:
#     index_comparison = 'underweight'
# elif 18.5 <= index <= 24.9:
#     index_comparison = 'normal weight'
# elif index > 24.9:
#     index_comparison = 'overweight'
#
# print(f'Your body mass index is: {index}, Your body mass index is {index_comparison}')
#
#
# # Завдання 3         Беспятий Дмитро
#
# price = 1000
# customer_card = input('введіть чи є карта пост. клієнта "yes" чи "no": ')
# number = int(input('введіть кількість товарів, які купуються: '))
#
# if customer_card == 'yes':
#     price = price - 100
# if number < 10:
#     discount = 0
#     price = number * price
# elif 10 <= number <= 19:
#     discount = (number * price) * 0.1
#     price = number * price - discount
# elif 20 <= number <= 49:
#     discount = (number * price) * 0.2
#     price = (number * price) - discount
# elif 50 <= number <= 99:
#     discount = (number * price) * 0.3
#     price = (number * price) - discount
# elif 100 <= number:
#     discount = (number * price) * 0.4
#     price = (number * price) - discount
#
# print(f'Сума знижки складає: {discount} Загальна сума покупки: {price}')
#
#
# # Завдання 4         Беспятий Дмитро
#
# k = int(input('введіть ціле число k: '))
#
# if 1 <= k <= 365:
#     if (k - 1) % 7 < 5:
#         day = 'робочий день'
#     else:
#         day = 'не робочий день "неділя"' if k % 7 == 0 else 'не робочий день "субота"'
# else:
#     day = 'введений невірний день року'
#
# print(f'{day}')
print("ggg")