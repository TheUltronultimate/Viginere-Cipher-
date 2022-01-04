

#Constants

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~.@·¿Ç0123456789" +' '
standard_frequency = [ 0.082,  0.015,  0.028 ,  0.043, 0.13, 0.022, 0.02, 0.061 , 0.07, 0.0015 , 0.0077,  0.04 , 0.024, 0.067, 0.075, 0.019, 0.00095, 0.06, 0.063,  0.091, 0.028, 0.0098, 0.024, 0.0015, 0.02,  0.00074 ]

#Caesar cipher code
def caesar_cipher_letter(letter, key):
  alphabet="abcdefghijklmnopqrstuvwxyz"
  x=alphabet.find(letter) 
  x=(x+key)%26
  return x

def caesar_cipher_letter_cap(letter, key):
  x=alphabet_cap.find(letter) 
  x=(x+key)%26
  return x

def caesar_cipher(text, shift):
  """Encodes a plaintext using caesar cipher for a given shft"""
  coded_message = ""
  for letter in text:
    if letter == ' ':
      coded_message += ' '
      continue
    if letter in alphabet_cap: 
      coded_message = coded_message +  alphabet_cap[caesar_cipher_letter_cap(letter, shift)]
    else:
      coded_message = coded_message +  alphabet[caesar_cipher_letter(letter, shift)]
  return coded_message






# Code for Viginère Cipher

def Update_key(a,b):
  """this function takes in 2 texts and repeats the second one character by character until they are the same length
  input : a : str, b : str
  output b : str
  IMPORTANT!!!! --> ORDER OF INPUT MATTERS
  """
  i = 0
  while len(a) > len(b):
      b += b[i]
      i+=1
  return b

def create_tabula_recta():
  """this function has no input and creates the tabula_recta used to encode the viginère cipher"""
  tabula_recta = []
  tabula_recta_cap = []
  for i in range(26):
    tabula_recta.append(caesar_cipher(alphabet, i))
  for i in range(26):
    tabula_recta_cap.append(caesar_cipher(alphabet_cap, i))
  return (tabula_recta, tabula_recta_cap)


  



def encode_viginère_cipher(text, key_word):
  """ this function encodes a text of text following a viginère cipher with a given key.
      input: text : str, key_word : str
      output: dode_text : str"""
  tabula_recta = create_tabula_recta()#creates tabula_recta
  key_word = Update_key(text, key_word)#repeats key_word until both texts are the same length 
  coded_text = ''
  for element in range(len(key_word)):#loops over the final length of the key_word
    if text[element] == ' ':
      coded_text += ' '
    if text[element] in punctuation: #or blank_space or digits == True:
      coded_text += text[element]
      continue
    if text[element] in alphabet_cap:
      text_index = alphabet_cap.find(text[element]) # looks for indes of colummn of the given letter of the text 
      key_index = alphabet.find(key_word[element]) # looks for the index of row for the given letter of the key_word
      coded_text += tabula_recta[1][key_index][text_index] #adds the letter situated at the resulting row-column
      continue
    else:
      text_index = alphabet.find(text[element]) # looks for indes of colummn of the given letter of the text 
      key_index = alphabet.find(key_word[element]) # looks for the index of row for the given letter of the key_word
      coded_text += tabula_recta[0][key_index][text_index] #adds the letter situated at the resulting row-column
      continue

  return coded_text


def decode_viginère_cipher(coded_text, key_word):
  tabula_recta = create_tabula_recta()
  decoded_text = ''
  key_word = Update_key(coded_text, key_word)
  space_count = 0 
  
  for element in range(len(key_word)):
    if coded_text[element] == ' ':
      decoded_text[element] += ' '
      space_count +=1
    if coded_text[element] in punctuation:
      decoded_text += coded_text[element]
      continue
    if coded_text[element] in alphabet_cap:
      key_index = alphabet.find(key_word[element])
      #print(key_index)
      temporary_list = tabula_recta[1][key_index]
      #print(tabula_recta[1])
      #print(temporary_list)
      decoded_text_index = temporary_list.find(coded_text[element])
      #print(decoded_text_index)
      decoded_text += alphabet_cap[decoded_text_index]
    else:
      key_index = alphabet.find(key_word[element-space_count])
      temporary_list = tabula_recta[0][key_index]
      decoded_text_index = temporary_list.find(coded_text[element])
      decoded_text += alphabet[decoded_text_index]
      


  return decoded_text



