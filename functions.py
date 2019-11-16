from random import randrange
from math import ceil

def choice_money():
    money = input("Saisissez une somme d argent a miser")
    try:
        money = int(money) # Conversion de la somme
        assert money > 0
        print("vous miser {} euros".format(money))
        return money
    except ValueError:
        print("valeur invalide saisie en lettre")
        return False
    except AssertionError:
        print("valeur negative")
        return False

def choice_number():
    choice_player = input("veuillez choisir un nombre entre 0 et 49")
    list_choice = list(range(50))
    try:
        choice_player=int(choice_player)
        assert choice_player in list_choice
        print("vous miser sur le nombre {} ".format(choice_player))
        return choice_player
    except ValueError:
        print("valeur invalide saisie en lettre")
        return False
    except AssertionError:
        print("valeur hors liste de choix")
        return False

def color(number):
    if int(number)%2==0:
        return "noir"
    else:
        return "rouge"


def choice_random():
    choice_pc=randrange(50)
    print("le choix du pc est {}".format(choice_pc))
    return choice_pc

def game():
    first_money = choice_money()
    while first_money == False:
        first_money = choice_money()
    his_choice = choice_number()
    while his_choice == False:
        his_choice = choice_number()
    print("la couleur correspondante est ", color(his_choice))
    my_choice = choice_random()
    print("la couleur correspondante est ", color(my_choice))
    if his_choice == my_choice:
        first_money = 3*first_money
        print("vous avez gagne",first_money)
    elif color(his_choice) == color(my_choice):
        first_money = ceil(first_money/2)
        print("vous recuperez la moitie de votre mise soit {} euros".format(first_money))
    else:
        first_money = 0
        print("vous une mise nulle")
    return first_money

game()