# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
  words = []
  dictionary_file = open("dictionary.txt")
  for line in dictionary_file:
    # store word, omitting trailing new-line
    words.append(line[:-1])
  dictionary_file.close()
  return words

# analyze a one-word password
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses

# analyze a two-word password
def two_word(password):
  words = get_dictionary()
  guesses = 0
  
  # s p a c e
  if(" " in password):
    password_l = password.split(" ")
  
    # check each combination lmao
    for w1 in words:
      guesses += 1
      if(w1 == password_l[0]):
        for w2 in words:
          pass_guess = w1+" "+w2
          if(pass_guess == password):
            print(pass_guess)
            return True, guesses

  # nospace
  for w1 in words:
    current = password[:len(w1)]
    guesses += 1
    if(w1 == current):
      for w2 in words:
        pass_guess = w1+w2
        if(pass_guess == password):
          print(pass_guess)
          return True, guesses
  return False, guesses