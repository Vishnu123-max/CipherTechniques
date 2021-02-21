#check if coprime
 
def gcd(a,b):
    if(a>b):
        if b == 0:
            return a
        return gcd(a%b,b)
    return gcd(b,a)
 
def coprime(a,b):
  if(gcd(a,b)==1):
    return True
  return False
 
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x
    
    #Take plaintext input from user
 
text = str(input("Enter the text you want to encrypt: "))
plaintext = text.upper()
iter_text = plaintext.split(" ")
mult_key = int(input("Enter the value to be used for Cipher multiplication key: "))
add_key = int(input("Enter the value to be used for Cipher addition key: "))
if(coprime(mult_key,26)==False):
  print("This function has no inverse, so you will not be able to decrypt it. Choose another value for key.")
  mult_key = int(input("Enter the value to be used for Cipher multiplication key:"))
 
#Affine Cipher
 
encrypted_word = ""
for word in iter_text:
  for letter in word:
    #if ascii value of shifted letter is beyond the value of Z, we shift
    #the ascii values by 65 and take modulus with 26
    #adding 64 back to the new_letter to get the ascii equivalent character 
      new_letter = chr(int(((((ord(letter)-65)*mult_key)+add_key)%26)+65))
      encrypted_word += new_letter
  encrypted_word += " "
print("The Cipher Text through Affine Cipher is:",encrypted_word)
 
#Decryption
 
iter_ciphertext = encrypted_word.split(" ")
decrypted_word = " " 
inverse_key = modInverse(mult_key,26)
for word in iter_ciphertext:
  for letter in word:
    old_letter = chr(int(((((ord(letter)-65)-add_key)*inverse_key)%26)+65))
    decrypted_word += old_letter
  decrypted_word += " "
print("The original plaintext was:", plaintext)
print("The decrypted text after decryption is:",decrypted_word)
