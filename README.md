# Password
Password Cracker Lesson

## How to use
1. Clone files
2. Run code

It should look like this:
```
One?(y/n) 
```
3. Input 'y' if password is one "word", else, input 'n' for a 2-word password.

```
Enter Password: 
```

4. Input your password.
5. You will recieve info on password.

## How does it work?
### The main algorithm
#### One Word
```ruby
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
print("Time:", format((time_end-time_start), ".8f")
```
#### Two Word
```ruby
# Analize a One-Word Password
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
```
### PWA File
#### One word
```ruby
def one_word(password):
  words = get_dictionary()
  guesses = 0
  # get each word from the dictionary file
  for w in words:
    guesses += 1
    if (w == password):
      return True, guesses
  return False, guesses
 ```
 #### Two Word
 ```ruby
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
```





# C. SAP Or Lcc




