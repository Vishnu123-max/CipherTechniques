#Take plaintext input from use
text = str(input("Enter the text you want to encrypt: "))
plaintext = text.upper()
iter_text = plaintext.split(" ")
key = int(input("Enter the shift value to be used for Cipher: "))
 
#Monoalphabetic Cipher
#Additive Cipher
#Encryption
encrypted_word = ""
for word in iter_text:
  for letter in word:
    #adding the value of key to the ascii value of letter and getting shifted letter
    #if ascii value of shifted letter is beyond the value of Z, we shift
    #the ascii values by 65 and take modulus with 26
    #adding 65 back to the new_letter to get the ascii equivalent character 
    #considering A=0 and Z=25 (that's why 65)
    new_letter = chr((((ord(letter)-65)+key)%26)+65)
    encrypted_word += new_letter
  encrypted_word += " "
print("The Cipher Text through Additive Cipher is:",encrypted_word)
 
#Decryption
 
iter_ciphertext = encrypted_word.split(" ")
decrypted_word = " " 
for word in iter_ciphertext:
  for letter in word:
    old_letter = chr((((ord(letter)-65)-key)%26)+65)
    decrypted_word += old_letter
  decrypted_word += " "
print("The original plaintext was:", plaintext)
print("The decrypted text after decryption is:",decrypted_word)
 
#Ceaser Cipher
encrypted_word = ""
for word in iter_text:
  for letter in word:
    #adding the value of key to the ascii value of letter and getting shifted letter
    #if ascii value of shifted letter is beyond the value of Z, we shift
    #the ascii values by 65 and take modulus with 26
    #adding 64 back to the new_letter to get the ascii equivalent character 
    new_letter = chr((((ord(letter)-65)+3)%26)+65)
    encrypted_word += new_letter
  encrypted_word += " "
print("The Cipher Text through Ceaser Cipher is:",encrypted_word)
 
#Decryption
 
iter_ciphertext = encrypted_word.split(" ")
decrypted_word = " " 
for word in iter_ciphertext:
  for letter in word:
    old_letter = chr((((ord(letter)-65)-3)%26)+65)
    decrypted_word += old_letter
  decrypted_word += " "
print("The original plaintext was:", plaintext)
print("The decrypted text after decryption is:",decrypted_word)

 
