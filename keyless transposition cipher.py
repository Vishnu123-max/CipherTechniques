#take input from user
text = str(input("Enter the text you want to encrypt: "))
text_caps = text.upper()
plaintext = "".join(text_caps.split(" "))
 
#arranging the text in a matrix
number_columns = 4
l = [list(plaintext[i:i+number_columns]) for i in range(0, len(plaintext), number_columns)]
transposition_matrix = [s if len(s) == number_columns else s+[None]*(number_columns-len(s)) for s in l]
 
#calculating the number of rows, here the text is divided into length of 4 substrings
#taking +1 for ceil value of the calculation
number_rows = len(plaintext)//4 + 1
 
print("\nThe letters arranged in matrix are as:\n")
for i in range(number_rows):
  for j in range(number_columns):
    print(transposition_matrix[i][j],end= " ")
  print(" ")
#reading the text column-wise
encrypted_text = ""
for j in range(4): 
    for i in range(number_rows): 
        if transposition_matrix[i][j]!=None:
         encrypted_text += transposition_matrix[i][j]
 
print("\nThe encrypted text is:",encrypted_text) 
