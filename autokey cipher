#Take plaintext input from user
 
text = str(input("Enter the text you want to encrypt: "))
plaintext = text.upper()
iter_text = plaintext.split(" ")
key = int(input("Enter the key value to be used for Cipher: "))
 
#Polyalphabetic Cipher
#Autokey Cipher
 
#Encryption
#Creating a list of keys to be used in autokey cipher
key_values = [key]
#traversing each letter in the text and adding the equivalent key
for word in iter_text:
  for letter in word:
    key_values.append(ord(letter)-65)
#removing the last letter's key as it will not be used
key_values.pop(-1)
 
encrypted_word = ""
value_of_key = 0
for word in iter_text:
  for letter in word:
    #adding the value of key to the ascii value of letter and getting shifted letter
    #if ascii value of shifted letter is beyond the value of Z, we shift
    #the ascii values by 65 and take modulus with 26
    #adding 65 back to the new_letter to get the ascii equivalent character 
    #considering A=0 and Z=25 (that's why 65)
    new_letter = chr((((ord(letter)-65)+key_values[value_of_key])%26)+65)
    encrypted_word += new_letter
    value_of_key += 1
  encrypted_word += " "
print("The Cipher Text through Autokey Cipher is:",encrypted_word)
 
#Decryption
 
iter_ciphertext = encrypted_word.split(" ")
decrypted_word = " " 
value_of_key = 0
for word in iter_ciphertext:
  for letter in word:
    old_letter = chr((((ord(letter)-65)-key_values[value_of_key])%26)+65)
    decrypted_word += old_letter
    value_of_key += 1
  decrypted_word += " "
print("The original plaintext was:", plaintext)
print("The decrypted text after decryption is:",decrypted_word)
