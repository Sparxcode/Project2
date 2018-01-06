# ver 1.1

# Gra kamien, nożyczki, papier
# Super gra

from random import choice
atrybut = ('kamień', 'papier', 'nożyczki')

'''
Kamień win with Nożyczki
Kamień lose with Papier

Papier win with Kamień
Papier lose with Nożyczki

Nożyczki win with Papier
Nożyczki lose with Kamień
'''

jeszcze_raz = "tak"
while jeszcze_raz == "tak":
    human = input('Podaj kamień, nożyczki lub papier: ')
    if human.lower() in atrybut:
        computer = choice(atrybut)
        print('Wybrałeś: ',human.lower())
        print('Komputer wybrał: ',computer)
        if human.lower() == computer:
            print('REMIS')
        elif human.lower() == 'kamień' and computer == 'nożyczki':
            print('WYGRAŁEŚ!')
        elif human.lower() == 'nożyczki' and computer == 'papier':
            print('WYGRAŁEŚ!')
        elif human.lower() == 'papier' and computer == 'kamień':
            print('WYGRAŁEŚ!')
        else:
            print('PRZEGRAŁEŚ!')
        print ("Czy chcesz zagrać jeszcze raz? (tak/nie)")
        jeszcze_raz = input()
    else:
        print('Jakiś błąd w wyrazie, popraw proszę.')
        jeszcze_raz = 'tak'

print('Koniec')




