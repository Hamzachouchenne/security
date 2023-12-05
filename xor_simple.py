input_file = "image.jpg" 
output_file = "result1.jpg" 

with open(input_file, 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()
for xor_key in range(256):


    decrypted_data = bytes([byte ^ xor_key for byte in encrypted_data])


    with open(output_file, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    if decrypted_data[:2] == b'\xFF\xD8' :#un fichier jpg valide commmence par cette sequence
        break


 

        
        