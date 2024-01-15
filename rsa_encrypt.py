#   a212_rsa_encrypt.py
import rsa as rsa

key = input("Enter the Encryption Key: " )
while key.isdigit() == False:
    key = input("Enter the Encryption key: ")
else:
    key = int(key)
mod_value = input("Enter the Modulus: " )
while mod_value.isdigit() == False:
    mod_value = input("Enter the modulus: ")
else:
    mod_value = int(mod_value)
plaintext = input("Enter a message to encrypt: ")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message:", encrypted_msg)
