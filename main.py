# a213_pw_analyzer.py
import time
import pwalgorithms as pwa

type = input("one?(y/n) ")


password = input("Enter password:")

if(type.lower() == "y"):
  print("Analyzing a one-word password ...")
  time_start = time.time()

  # attempt to find password
  found, num_guesses = pwa.one_word(password)
  time_end = time.time()

  # report results
  if (found):
    print(password, "found in", num_guesses, "guesses")
  else: 
    print(password, "NOT found in", num_guesses, "guesses!")
  print("Time:", format((time_end-time_start), ".8f"))
else:
  
  print("Analyzing a two-word password ...")
  time_start = time.time()

  # attempt to find password
  found, num_guesses = pwa.two_word(password)
  time_end = time.time()

  # report results
  if (found):
    print(password, "found in", num_guesses, "guesses")
  else: 
    print(password, "NOT found in", num_guesses, "guesses!")
  print("Time:", format((time_end-time_start), ".8f"))