def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(23, 32, False)
print_params(2, 'chek')
print_params(23)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [24, 'Game over', True]
values_dict = {'a' : True, 'b' : 45, 'c' : 'Win'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
