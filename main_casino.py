def choice_number():
    choice_player = input("veuillez choisir un nombre entre 0 et 49")
    list_choice = list(range(50))
    try:
        choice_player=int(choice_player)
        assert choice_player in list_choice
        print("vous miser sur le nombre {} ".format(choice_player))
    except ValueError:
        print("valeur invalide saisie en lettre")
        return False
    except AssertionError:
        print("valeur hors liste de choix")
        return False

while choice_number() == False:
    choice_number()