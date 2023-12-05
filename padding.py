#############################################################
#########IL FAUT UTILISER LINUX POUR CET EXERCICE############
#############################################################



from pwn import *

io = remote('@ serveur', port serveur)

cbc_ciphertext = "saisir votre cipher text"
VI = cbc_ciphertext[:32]
C1 = cbc_ciphertext[32:64]
C2 = cbc_ciphertext[64:]




def padding(C):
	
	S = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	decalage=0
	padd=1
	K = ["00","00","00","00","00","00","00","00","00","00","00","00","00","00","00","00"]

	for nb_bytes in range(16):
	
		#pour nb_bytes=0
	
	
		for i in range(256):

			K[15-nb_bytes]=hex(i)[2:].zfill(2)
			#K[15] va prendre une valeur entre 00 et ff


			request=''.join(K)+C
			#ici en va faire une concatination entre le ciphertext et notre K le resultat est 00000000000000K[15]CIPHERTEXT

			io.sendline(request)
			#on va envoyer la request et enregistrer la reponse de serveur

			print("Trying:"+ request)
			response = io.recvline()
			print(response)


			if response == b'Successfully decrypted.\n':
				#si la request est accepté par le serveur on fait ces etapes
				
				X=K[15-decalage]
				#dans notre cas X=K[15]
				
				S[15-decalage]= hex(padd ^ int(X, 16))[2:].zfill(2)
				#on calcule S qui est la partie d la clé pour decrypter le ciphertext dans ce cas on fait K[15]XOR1
				
				for x in range(padd):
					K[15-x] = hex(int(S[15 - x], 16) ^ (padd + 1))[2:].zfill(2)
					#ici on trouve que la valeur de K va changer K[15]=S[15]XOR2 et K[14]XOR1
			
				break
		padd=padd+1
			
		decalage=decalage+1
		#on suite in incremente le padding et le decalage on refait tout avec un nb_bytes=1
			
		
	s=''.join(S)
	#apres q"on parcourt toutes les byets on trouve notre clé s qui sert a dechiffrement de ciphertext
	return s



def decrypt_message(S,KEY):
	int_P2=int(S,16)
	int_C1=int(KEY,16)

	int_message=int_C1 ^ int_P2

	message=hex(int_message)[2:]
	
	byte_data = bytes.fromhex(message)
	text = byte_data.decode('utf-8')  

	return text
	

S2=padding(C2)
text2=decrypt_message(C1,S2)
S1=padding(C1)
text1=decrypt_message(S1,VI)
plain_text=text1+text2
print(plain_text)

io.interactive()

