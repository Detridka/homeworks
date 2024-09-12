call = 0
def count_call():
    global call
    call += 1
def string_info(string):
    return len(string), string.upper(), string.lower()
    count_call()
def is_contains(string, list_to_search):
    for item in list_to_search:
        if item.casefold() == string.casefold():
            return True
    return False
    count_call()
count_call()

print(string_info('dva'))
print(string_info('krevetka'))
print(is_contains('Бар', ['бАР', 'Банан', 'Вася']))
print(is_contains('круг', ['квадрат', 'треугольник']))
print(call)

