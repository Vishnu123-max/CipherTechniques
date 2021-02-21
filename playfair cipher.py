#Take plaintext input from user
 
text = str(input("Enter the text you want to encrypt: "))
text_caps = text.upper()
#replacing J with I in the plaintext
plaintext = text_caps.replace("J","I")
key = str(input("Enter the key value to be used for Cipher: ")).upper()
 
#defining the string of all alphabets
alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
remaining_alphabets = ""
 
#finding out remaining letters from alphabets except the ones in the key
for letter in alphabets:
  if letter not in key:
    remaining_alphabets += letter
 
#creating and printing the key matrix
key_string = key+remaining_alphabets
number_columns = 5
l = [list(key_string[i:i+number_columns]) for i in range(0, len(key_string), number_columns)]
key_matrix = [s if len(s) == number_columns else s+[None]*(number_columns-len(s)) for s in l]
print("\nThe key matrix is:\n")
for i in range(5): 
    for j in range(5): 
        print(key_matrix[i][j], end = " ") 
    print()
 
#splitting the plaintext in digraphs
 
if (len(plaintext)%2==0):
  plaintext_list = list(plaintext[i:i+2] for i in range(0, len(plaintext), 2))
else:
  plaintext += "Z"
  plaintext_list = list(plaintext[i:i+2] for i in range(0, len(plaintext), 2))
print("\nThe plaintext in pairs of two is:",plaintext_list)
 
#creating a matrix of to identify positions of the letters in the key matrix
index_letters = []
 
for pair in plaintext_list:
  for letter in pair:
    for i in range(5):
      if letter in key_matrix[i]:
        index_letters.append((i,key_matrix[i].index(letter)))
        break
      else:
        continue
 
index_letters_pairs = list(index_letters[i:i+2] for i in range(0, len(index_letters), 2))
 
coded_letters_index = []
for pair in index_letters_pairs:
  #if letters are in same row
  if pair[0][0] == pair[1][0]:
   #if letters are not the rightmost in the row
   if pair[0][1] <= 3 and pair[1][1] <=3:
    #increase the column value for each letter
    coded_letters_index.append([(pair[0][0],pair[0][1]+1),(pair[1][0],pair[1][1]+1)])
   #if letters are the rightmost in row
   else:
     if pair[0][1] == 4:
       coded_letters_index.append([(pair[0][0],0),(pair[1][0],pair[1][1]+1)])
     elif pair[1][1] == 4:
       coded_letters_index.append([(pair[0][0],pair[0][1]+1),(pair[1][0],0)])
     elif pair[0][1] == 4 and pair[1][1] == 4:
       coded_letters_index.append([(pair[0][0],0),(pair[1][0],0)])
   
    #if letters are in same column
  elif pair[0][1] == pair[1][1]:
    #if letters are not the bottommost in the column
      if pair[0][1] <= 3 and pair[1][1] <=3:
      #increase the row value for each letter
       coded_letters_index.append([(pair[0][0]+1,pair[0][1]),(pair[1][0]+1,pair[1][1])])
    #if letters are the bottommost in row
      else:
        if pair[0][0] == 4:
          coded_letters_index.append([(0,pair[0][1]),(pair[1][0]+1,pair[1][1])])
        elif pair[1][0] == 4:
          coded_letters_index.append([(pair[0][0]+1,pair[0][1]),(0,pair[1][1])])
        elif pair[0][0] == 4 and pair[1][0] == 4:
          coded_letters_index.append([(0,pair[0][1]),(0,pair[1][1])])
    
    #if none of the above conditions are true
  else:
      #create a rectangle and take vertex values
       coded_letters_index.append([(pair[0][0],pair[1][1]),(pair[1][0],pair[0][1])])
 
encrypted_text = ""
#printing the corresponding elements from the key_matrix
for pair in coded_letters_index:
  for i in range(2):
    row = pair[i][0]
    column = pair[i][1]
    
    encrypted_text += key_matrix[row][column]
 
print("\nThe encrypted text is:",encrypted_text)
