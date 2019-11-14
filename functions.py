from random import randrange
def choice_money():
    money=int(input("veuillez entrer le montant de la mise"))
    while money <= 0:
        print("erreur montant invalide, Veuillez resaisir votre montant de nouveau")
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


print(list(range(50)))
choice_money()
a=choice_number()
b=choice_random()
print(color(a))
print(color(b))
