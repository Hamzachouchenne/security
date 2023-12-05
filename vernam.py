import socket 
import string
import random

address_de_serveur = "@ de serveur"
port_de_serveur = port de serveur


text_clair = ""
message_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
x = len(message_secret)
   
for indice_de_lettre in range(x):
    lettres = string.ascii_uppercase


    while len(lettres)!=1:

        #connecter au serveur
        client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client_socket.connect((address_de_serveur,port_de_serveur))
    	

    	#enregistre la reponse sous la fore d'une chaine des caracteres
        ciphertext = client_socket.recv(1024).strip().decode('utf-8')
        client_socket.close()
        

        #si en trouve la meme lettre dans la chaine de lettres et le ciphertext on supprime cette lettre
        #de chainnes des lettres dans la resultat il n'y reste qu'une seuls lettre ,cette lettres appartient dans le message originale
        if ciphertext[indice_de_lettre] in lettres :
            lettres=lettres.replace(ciphertext[indice_de_lettre],'')
    
    text_clair = text_clair + lettres

    #on arrete la boucle loorsque le message secret et le texte clair ont la meme longueur
    if len(text_clair)==len(message_secret):
    	break

print("le message clair est ",text_clair)
