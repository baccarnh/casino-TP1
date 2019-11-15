from random import randrange
from math import ceil

def choice_money():
    money = input("veuillez entrer le montant de la mise")
    try:
        money=int(money)
        while money <= 0:
            print("erreur montant invalide, Veuillez resaisir votre montant de nouveau")
            money = int(input("veuillez entrer le montant de la mise"))
            print("vous avez choisi de miser {} euros".format(money))
    except ValueError:
        print("vous n avez saisi de chiffres")
        money = int(input("veuillez entrer le montant de la mise"))
        print("vous avez choisi de miser {} euros".format(money))

def choice_number():
    choice_player=int(input("veuillez choisir un nombre entre 0 et 49"))
    list_choice=list(range(50))
    while choice_player not in list_choice:
        print("erreur choix non valide, veuillez resaisir votre choix")
        choice_player =int(input("veuillez choisir un nombre entre 0 et 49"))
    print("vous avez choisi de miser sur {} ".format(choice_player))
    return choice_player

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
    his_choice = choice_number()
    my_choice = choice_random()
    if his_choice == my_choice:
        first_money = 3*first_money
        print("vous qvez gqgne",first_money)
    elif color(his_choice) == color(my_choice):
        first_money = ceil(first_money/2)
        print("vous recuperez la moitie de votre mise",first_money)
    else:
        first_money = 0
        print("vous une mise nulle")
    return first_money

game()