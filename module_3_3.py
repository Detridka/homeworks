def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [55, False, 'string']
values_dict = {'a' : 77, 'b' : 'word','c' : False}
values_list_2 = 'worm', False


print_params()
print_params(b=25)
print_params(c= [1,2,3])
print_params(5)
print_params(13, 14, 15)
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 99)

