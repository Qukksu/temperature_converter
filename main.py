def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

while True:
    print('Что вы хотите перевести?')
    print('1. Градусы Цельсия в Фаренгейты')
    print('2. Фаренгейты в градусы Цельсия')
    print('3. Перевести Цельсии в Кельвины')
    print('4. Перевести Кельвины в Цельсии')
    print('5. Перевести Фаренгейты в Кельвины')
    print('6. Перевести Кельвины в Фаренгейты')
    print('7. Выход')
    choice = input()

    if choice == '1': # Градусы Цельсия в Фаренгейты
        try:
            celsius = float(input('Введите градусы Цельсия: '))
            if celsius < -273.15:
                print('Вы ввели неверное значение')
                continue
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f'{celsius} градусов Цельсия = {fahrenheit} градусов Фаренгейта')
        except ValueError:
            print('Вы ввели не число')

    elif choice == '2': # Фаренгейты в градусы Цельсия
        try:
            fahrenheit = float(input('Введите градусы Фаренгейта: '))
            if fahrenheit < -459.67:
                print('Вы ввели неверное значение')
                continue
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f'{fahrenheit} градусов Фаренгейта = {celsius} градусов Цельсия')
        except ValueError:
            print('Вы ввели не число')

    elif choice == '3': # Перевести Цельсии в Кельвины
        try:
            celsius = float(input('Введите градусы Цельсия: '))
            if celsius < -273.15:
                print('Вы ввели неверное значение')
                continue
            kelvin = celsius_to_kelvin(celsius)
            print(f'{celsius} градусов Цельсия = {kelvin} градусов Кельвина')
        except ValueError:
            print('Вы ввели не число')

    elif choice == '4': # Перевести Кельвины в Цельсии
        try:
            kelvin = float(input('Введите градусы Кельвина: '))
            if kelvin < 0:
                print('Вы ввели неверное значение')
                continue
            celsius = kelvin_to_celsius(kelvin)
            print(f'{kelvin} градусов Кельвина = {celsius} градусов Цельсия')
        except ValueError:
            print('Вы ввели не число')

    elif choice == '5': # Перевести Фаренгейты в Кельвины
        try:
            fahrenheit = float(input('Введите градусы Фаренгейта: '))
            if fahrenheit < -459.67:
                print('Вы ввели неверное значение')
                continue
            kelvin = fahrenheit_to_kelvin(fahrenheit)
            print(f'{fahrenheit} градусов Фаренгейта = {kelvin} градусов Кельвина')
        except ValueError:
            print('Вы ввели не число')

    elif choice == '6': # Перевести Кельвины в Фаренгейты
        try:
            kelvin = float(input('Введите градусы Кельвина: '))
            if kelvin < 0:
                print('Вы ввели неверное значение')
                continue
            fahrenheit = kelvin_to_fahrenheit(kelvin)
            print(f'{kelvin} градусов Кельвина = {fahrenheit} градусов Фаренгейта')
        except ValueError:
            print('Вы ввели не число')

    elif choice == '7': # Выход
        break

    elif choice == 'bbp': # Биг блэк пенис йоу
        print('Биг блэк пенис йоу') #easter egg, кто поймет, тот поймет. ЙОУ
        continue

    elif choice == '': # Если ничего не ввели
        print('Вы ничего не ввели')
        continue
    else: # Если ввели неверное значение
        print('Вы ввели неверное значение')
        continue