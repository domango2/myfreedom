"""
5)Вычислить сумму цифр случайного трёхзначного числа.
(прочитать про модуль math и random)
"""

from random import randint

number = randint(100, 999)
print("Полученное случайное число:", number)

n3 = number % 10
n2 = number // 10 % 10
n1 = number // 100

print("Сумма цифр числа равна", n1 + n2 + n3)
