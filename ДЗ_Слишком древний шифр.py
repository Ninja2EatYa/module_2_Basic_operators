def get_pass(n):
    pass_list = ''
    for a in range(1, n):
        for b in range(a+1, n):
            if n % (a + b) == 0:
                pass_list += str(a) + str(b)
    return pass_list

for n in range(3, 21):
    pass_list = get_pass(n)
    print(f'{n} - {pass_list}')
