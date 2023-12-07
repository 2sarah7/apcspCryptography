# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary2.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
# def one_word(password):
#   words = get_dictionary()
#   guesses = 0
#   # get each word from the dictionary file
#   for w in words:
#     guesses += 1
#     if (w in password):
#       return True, guesses
#   return False, guesses

def two_words(password):
  words = get_dictionary()
  guesses = 0

  for w in words:
    for w2 in words:
      combinedWords = w + w2
      guesses += 1
      if combinedWords == password:
        return True, guesses
      
  return False, guesses

digits = "0123456789"

def two_words_and_digit(password):
  global digits
  words = get_dictionary()
  guesses = 0
  for w in words:
    for w2 in words:
      combinedWords = w + w2
      for number in digits:
        numWords = number + combinedWords 
        guesses += 1
        if numWords == password:
          return True, guesses
        else:
          wordsNum = combinedWords + number
          if wordsNum == password:
            return True, guesses
        # for number in digits:
        #   numWordsNum = numWords + number
        #   guesses += 1
        #   if numWordsNum == password:
        #     return True, guesses
        
      # for number in digits:
      #   wordsNum = combinedWords + number
      #   guesses += 1
      #   if wordsNum == password:
      #     return True, guesses
        
      
  return False, guesses