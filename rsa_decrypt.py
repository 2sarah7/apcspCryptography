#   a212_rsa_decrypt.py
import rsa as rsa

key = input("Enter the Decryption Key: " )
while key.isdigit() == False:
    key = input("Enter the Decryption key: ")
else:
    key = int(key)
mod_value = input("Enter the Modulus: " )
while mod_value.isdigit() == False:
    mod_value = input("Enter the modulus: ")
else:
    mod_value = int(mod_value)
encrypted_msg = input("What message would you like to decrypt (No brackets): ")

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
