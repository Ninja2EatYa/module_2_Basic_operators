first = int(input('First: ',))
second = int(input('Second: '))
third = int(input('Third: '))

if first == second == third:
    print('Equal numbers: 3')
elif first == second or second == third or first == third:
    print('Equal numbers: 2')
else:
    print('Equal numbers: 0')