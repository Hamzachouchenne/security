
def chiffrement(decalage, chaine):
    new_string = ""
    for car in chaine:
        if car.isupper() == False:
            new_string = new_string + \
                chr((ord(car)+int(decalage)-ord('a')) % 26+ord('a'))
        else:
            new_string = new_string + \
                chr((ord(car)+int(decalage)-ord('A')) % 26+ord('A'))
    print("la chaine crypté\n", new_string)


def dechiffrement(decalage, chaine):
    new_string = ""
    for car in chaine:
        if car.isupper() == False:
            new_string = new_string + \
                chr((ord(car)-int(decalage)-ord('a')) % 26+ord('a'))
        else:
            new_string = new_string + \
                chr((ord(car)-int(decalage)-ord('A')) % 26+ord('A'))
    print("la chaine initial\n", new_string)


decalage = input("donner un nombre de decalage\n")
chaine = input("donner la chaine \n")


choix = input("faire un choix(chiffrer/dechiffrer)\n")
if choix == "chiffrer":
    chiffrement(decalage, chaine)
else:
    dechiffrement(decalage, chaine)
