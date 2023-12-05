def decalage(c):
    if c.islower():
        shift = ord(c) - ord('a')
    elif c.isupper():
        shift = ord(c) - ord('A')
    else:
        shift = 0
    return shift


def chiffrement_vigenere(complete_key, text):
    chaine = ""
    for i in range(len(text)):
        if text[i].islower():
            chaine += chr((ord(text[i]) - ord('a') +
                          decalage(complete_key[i])) % 26 + ord('a'))
        elif text[i].isupper():
            chaine += chr((ord(text[i]) - ord('A') +
                          decalage(complete_key[i])) % 26 + ord('A'))
        else:
            chaine += text[i]
    print("la chaine cryptée est ", chaine)


def dechiffrement_vigenere(complete_key, text):
    chaine = ""
    for i in range(len(text)):
        if text[i].islower():
            chaine += chr((ord(text[i]) - ord('a') -
                          decalage(complete_key[i])) % 26 + ord('a'))
        elif text[i].isupper():
            chaine += chr((ord(text[i]) - ord('A') -
                          decalage(complete_key[i])) % 26 + ord('A'))
        else:
            chaine += text[i]
    print("la chaine initiale est ", chaine)


text = input("entrer le text\n")
input_key = input("choisir la clé\n")
choix = input("chiffrer ou dechiffrer\n")


while len(input_key)<len(text):
    input_key+=input_key


if choix == "chiffrer":
    chiffrement_vigenere(input_key, text)
elif choix == "dechiffrer":
    dechiffrement_vigenere(input_key, text)
else:
    print("eurreur")


