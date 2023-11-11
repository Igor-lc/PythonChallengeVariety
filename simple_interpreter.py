'''
My lesson 1. Что такое Python!
Яязык программирования, в частности Python - это интерпретатор и правила. Самая простая программа на Python — это пустой файл с расширением .py. Запуск этого файла приведет к выполнению программы без ошибок. Congratulations! Создав файл, вы создали свою первую программу! Просто она ничего не делает.

Теперь добавим функционала, напишем:
'''

# print("Hello, Our Planet! I'm your own simple interpreter!")

'''
Если вы запустите эту программу, она выведет указанный текст в консоль.
Если добавить еще 2 строки:
'''

with open('first_program.txt', 'w') as file:
    print("Greetings, Inhabitants of Our Planet! Let the coding adventures begin!", file=file)


'''
То программа создаст файл с именем first_program.txt и запишет в него указанный текст.
Теперь создадим собственный интерпретатор. Первый шаг — создать пустой Python файл.
Затем добавим базовую функцию сложения 2 чисел:
'''

while True:
    code = input('>>> ')
    if '+' in code:
        number1, number2 = code.split('+')
        number1, number2 = int(number1), int(number2)
        print(number1 + number2)

'''
Благодаря этому коду наш интерпретатор может складывать два числа. Просто запустите программу и введите два числа с плюсом между ними! Чтобы количество чисел было произвольным нужно доработать код.

А чтобы создать исполняемый файл .exe из файла .py, выполните следующие действия, для Windows:

Откройте PyCharm.
Откройте терминал в PyCharm (кнопка слева внизу).
Скопируйте следующие команды:


pip install pyinstaller
pyinstaller --onefile simple_interpreter.py


Первая скачает и установит библиотеку pyinstaller.
Вторая создаст файл simple_interpreter.exe из файла simple_interpreter.py
Вы можете запустить simple_interpreter.exe и сложить два числа з помощью собственного интерпретатора!
Congratulations!
'''