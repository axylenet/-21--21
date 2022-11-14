'''
Группа 21ИС-21
Гаврюшкин Максим
14.11.2022
Задача №4:
Даны три числа. Найти сумму двух наибольших из них.
'''
a = int(input())
b = int(input())
c = int(input())
if a > c and b > c:
    a = a + b
elif a > b and c > b:
    a = a + c
elif c > a and b > a:
    a = c + b
print(a)