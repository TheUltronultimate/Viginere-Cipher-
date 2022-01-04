import Viginère
import string
import itertools


text =  'kuakshuiiavrfalgfwrlemfswyrctiypxjyixlvgugghrfyiiyivmstusplgqbpfaeolswywcceilwqbpufivfswalgjlcspgukgtiv' #sample CipherText used for testing
text = text.lower()

print('Text length:', len(text))
Kp= 0.065
Kr = 0.0385
c = len(alphabet)
MinKeyLen = 2 # ignores key lengths that would be unreasonably long to save time

def LetterFrequencies(CipherText):
  """Finds the frequency of each letter in the CipherText"""
  Frequencies = {letter: 0 for letter in alphabet}
  for letter in CipherText:
    if letter == ' ':
      continue
    Frequencies[letter] += 1

  return Frequencies


def LetterPercentages(Frequencies, CipherText):
  """Transforms frequencies into percentages"""
  PercentFrequencies = {}
  for letter in Frequencies.keys():
    PercentFrequencies[letter] = (Frequencies[letter] / len(CipherText)) 
  return PercentFrequencies



def ObservedCoincidenceRate(Frequencies, CipherText):
  N = sum(Frequencies.values())
  n = list(Frequencies.values())
  numerator = n[0]*(n[0]-1)
  print(numerator)
  for i in range(1, c):
    numerator += (n[i]*(n[i]-1))
  denominator = N*(N-1)
  Ko = numerator / denominator
  return Ko

def GuessKeyLen(Kp, Kr, Ko):
  numerator = Kp - Kr
  denominator = Ko - Kr
  return numerator / denominator

def GuessKeyLen2(CipherText, Ko, Kp, Kr):
  n = len(CipherText)
  numerator = 0.027*n
  denominator = (Kp- Ko) + n*(Ko- Kr)
  return numerator / denominator

NewFrequencies = LetterFrequencies(text)
Lp = LetterPercentages(NewFrequencies, text)
Ko = ObservedCoincidenceRate(NewFrequencies, text)
print('Observed Index of coincidece:', Ko)
KeyLen = GuessKeyLen2(text,  Ko, Kp, Kr)
print('Key length guess:', KeyLen)



   

def FindEnglish(string, words):
  """Attributes a score to each possible plaintext depending on how many of the words known are present"""
  score = 0
  a = False
  for word in words:
    if word in string:
      score += 2
    else:
      score -=2
  return score

def ComputeAllKeys(MinKeyLen, MaxKeyLen, CipherText, KnownWord):
  MaxKeyLen = round(MaxKeyLen*2)
  Scores = []
  score = 0
  PossibleDecrypts = []
  print(CipherText)
  for key in range(MinKeyLen, MaxKeyLen):
    #tries every key for given Max length
    
    AllKeys = itertools.permutations(alphabet, key)
    #attempt to solve with given key
    for PossibleKey in list(AllKeys):
      print(PossibleKey)
      PossibleKey = "".join(PossibleKey)
      if PossibleKey == " ": # ignores empty keys
        continue
      Decode = decode_viginère_cipher(CipherText, PossibleKey)
      score = FindEnglish(Decode, KnownWord)
      if score  > len(KnownWord):  # arbitrary measure of what scores are good enough to be considered solved ( I found it randomly through testing)   
         return PossibleKey, Decode, score
   

print("FinalScore and Final message:", ComputeAllKeys(MinKeyLen=MinKeyLen, MaxKeyLen=KeyLen, CipherText=text, KnownWord= [ 'your', 'they', 'and']))





