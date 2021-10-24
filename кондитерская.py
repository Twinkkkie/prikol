import pyttsx3

engine = pyttsx3.init()     # инициализация движка

# зададим свойства
engine.setProperty('rate', 170)     # скорость речи
engine.setProperty('volume', 0.9)   # громкость (0-1)

pastry = {'наполеон': [['масло', 'мука', 'сахар'], 7, 1000],
          'медовик': [['мука', 'масло', 'сахар'], 4, 1025],
          'киевский': [['сахар', 'мука', 'масло'], 5, 985]}

choices = [0, 1, 2, 3, 4, 5]

while True:
    engine.say('''Если вы хотите посмотреть описание, нажмите 1.
     Посмотреть цену - нажмите 2.
     Посмотреть кол-во - нажмите 3.
     Посмотреть всю информацию - нажмите 4.
     Если вы хотите купить торт, нажмите 5.
     Для выхода из программы нажмите 0''')
    engine.runAndWait()
    choice = input('Что  вас интересует?  ')

    try:
        choice = int(choice)
    except ValueError:
        engine.say('Вы ввели неправильный номер')
        engine.runAndWait()
    else:
        if choice == 0:
            engine.say('Приходите снова!')
            engine.runAndWait()
            break
        elif choice not in choices:
            engine.say('Такой функции нет')
            engine.runAndWait()
        else:
            while True:
                engine.say('''Если хотите продолжить, укажите, какой торт вас интересует.
                 Если вы хотите выйти в меню, введите 0.''')
                engine.runAndWait()
                cake = input('Введите, какой торт вас интересует, или 0 для выхода в меню: ').lower()

                if cake == '0':
                    break
                elif cake not in pastry.keys():
                    engine.say('Такого торта нет')
                    engine.runAndWait()
                else:
                    for k, v in pastry.items():
                        if cake == k:
                            if choice == 1:
                                engine.say(f'Торт {cake} состоит из {v[0]}')
                                engine.runAndWait()
                            elif choice == 2:
                                engine.say(f'Торт {cake} стоит {v [1]} рублей')
                                engine.runAndWait()
                            elif choice == 3:
                                engine.say(f'Торта {cake} осталось {v [2]} грамм')
                                engine.runAndWait()
                            elif choice == 4:
                                engine.say(f'Торт {cake} состоит из {v[0]}')
                                engine.say(f'Торт {cake} стоит {v [1]} рублей')
                                engine.say(f'Торта {cake} осталось {v [2]} грамм')
                                engine.runAndWait()
                            elif choice == 5:
                                while True:
                                    engine.say('''Если вы хотите продолжить, введите, сколько тортиков вам положить.
                                     Если вы хотите выйти в меню выше, введите 0''')
                                    engine.runAndWait()
                                    amount = input('Введите количество в граммах или 0 для выхода: ')

                                    try:
                                        amount = int(amount)
                                    except ValueError:
                                        engine.say('Вы не ввели количество')
                                        engine.runAndWait()
                                    else:
                                        if amount == 0:
                                            break
                                        elif amount <= v[2]:
                                            total = amount * v[1] / 100
                                            engine.say(f'К оплате {total} рублей')
                                            engine.say(f'Торта {cake} осталось {v [2] - amount} грамм')
                                            engine.runAndWait()
                                            v[2] = v[2] - amount
                                        else:
                                            engine.say(f'Вы ввели больше, чем осталось: {cake} всего {v [2]} грамм')
                                            engine.runAndWait()
