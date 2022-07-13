# Zadanie 1: Nie powtarzaj się!
#
# W każdym języku programowania ważne jest by się nie powtarzać DRY - dlatego też warto starać się korzystać z funkcji. W związku z tym:
#
# Wylosuj 10 liczb z zakresu od 0 do 10, jeżeli któraś liczba się powtórzy wyświetl napis: Oh no! I repeated myself!


import random

def repated_myself():
    set_numbers = set()

    for i in range(10):
        number = random.randint(0,10)
        set_numbers.add(number)

    if len(set_numbers) < 10:
        print('Oh no I repeated myself!')


repated_myself()
#TODO: talk about other methods with Dawid










