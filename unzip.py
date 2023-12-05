import string
from itertools import product
import zipfile

zip_file_path ="fichier.zip"


alphabet = string.ascii_lowercase
list_de_mots_de_passe = []
for i in range(1,5):
    for combination in product(alphabet, repeat=i):
        s = ''.join(combination)
        list_de_mots_de_passe.append(s)


with zipfile.ZipFile(zip_file_path,'r') as z :
    for password in list_de_mots_de_passe:

        try:
            z.extractall(pwd=password.encode('utf-8'))
            test=True
        except:
            print("wrong password",password)


        if test== True:
            print("correct",password)
            break


        





    
    

        