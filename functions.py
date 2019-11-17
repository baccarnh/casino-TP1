from random import randrange
from math import ceil

def choice_money():
    money = input("Saisissez une somme d argent a miser")
    try:
        money = int(money) # assert that money can be convert to integer
        assert money > 0 # assert that money is greater than 0
        print("vous miser {} euros".format(money))
        return money
    except ValueError:
        print("valeur invalide saisie en lettre") # manage the letter error
        return False
    except AssertionError:
        print("valeur negative") # manage the negative error
        return False

def choice_number():
    choice_player = input("veuillez choisir un nombre entre 0 et 49")
    list_choice = list(range(50))
    try:
        choice_player=int(choice_player) # assert that the player_choice is number
        assert choice_player in list_choice #assert that the number chosen is between 0 and 49
        print("vous miser sur le nombre {} ".format(choice_player))
        return choice_player
    except ValueError:
        print("valeur invalide saisie en lettre") # manage the letter error
        return False
    except AssertionError:
        print("valeur hors liste de choix") # manage the number chosen greater than 49 or smaller than 0
        return False

def color(number):
    if int(number)%2==0:
        return "noir"
    else:
        return "rouge"

def choice_random():
    choice_pc=randrange(50) # the machine choice random
    print("le choix du pc est {}".format(choice_pc))
    return choice_pc

def game():
    first_money = choice_money()
    while first_money == False: #manage possible user mistakes
        first_money = choice_money()
    while first_money>0: # replay if bet is greater than 0
        his_choice = choice_number()
        while his_choice == False: # manage the user mistakes
            his_choice = choice_number()
        print("la couleur correspondante est ", color(his_choice)) #message giving the color of the number chosen by the player
        my_choice = choice_random()
        print("la couleur correspondante est ", color(my_choice)) #message giving the color of the number chosen by the machine
        if his_choice == my_choice: #winer case
            first_money = 3*first_money
            print("vous avez gagne",first_money)
            money_again()
        elif color(his_choice) == color(my_choice): #same color
            first_money = ceil(first_money/2)
            print("vous recuperez la moitie de votre mise soit {} euros".format(first_money))
            money_again()
        else: #loser case
            first_money = 0
            print("vous une mise nulle")
            money_again() #ask if the player want to makes new bet

def money_again():
    answer = input("voulez vous remiser de nouveau? taper oui ou non").upper()#accept oui/non
    tag = ["OUI", "NON"]
    while answer not in tag:#if input different =error
        print("erreur de saisie taper oui ou non")
        answer = input("entrer votre réponce de nouveau").upper()
    if answer == "OUI":
        game()
    else:
        print("Merci Aurevoir".center(50))



