first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print('Одинаковых чисел: 3')
elif first == second or first == third or second == third:
    print('Одинаковых чисел: 2')
else:
    print('Одинаковых чисел: 0')


