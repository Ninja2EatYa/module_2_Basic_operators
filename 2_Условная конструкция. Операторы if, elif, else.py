first = input('Enter integer number: ',)
int_first = int(float(first))
print(('First:'), int_first)

second = input('Enter integer number: ')
int_second = int(float(second))
print(('Second:'), int_second)

third = input('Enter integer number: ')
int_third = int(float(third))
print(('Third:'), int_third)

if int_first == int_second == int_third:
    print('Equal numbers: 3')
elif int_first == int_second != int_third or int_first != int_second == int_third or int_first == int_third != int_second:
    print('Equal numbers: 2')
else:
    print('Equal numbers: 0')