first = int(input('vvedite pervoe chislo: '))
second = int(input('vvedite vtoroechislo: '))
third = int(input('vvedite tretiechislo: '))
if first == second and second == third:
    print('3')
elif first == second or first == third or second == third:
    print('2')
elif first != second != third:
    print('0')


