import random

with open('wordlelist1.txt', 'r') as file1:
  list1 = file1.readlines()
  for i in range(len(list1)):
    list1[i] = list1[i][:-1]
  choose_word_list = list1

with open('wordlelist2.txt', 'r') as file2:
  list2 = file2.readlines()
  for i in range(len(list2)):
    list2[i] = list2[i][:-1]
  check_word_list = list2

past_trys = []

def printer():
  wipe_screen()
  print_trys()
  return

def print_trys():
  for i in past_trys:
    print(i)
  return

def wipe_screen():
  for i in range(50):
    print("")
  return

trys = 0
word = random.choice(choose_word_list)
green = "\033[42;30m"
yellow = "\033[43;30m"
end = "\033[0m"
win = False

def checker(entered_input):
  global win
  pos = [0, 0, 0, 0, 0]
  letters_colored =  []
  input_list = list(entered_input)
  result = input_list.copy()


  for i in range(5):
    if entered_input[i] == word[i]:
      pos[i] = 2
      letters_colored.append(entered_input[i])
    else:
      pass
  for i in range(5):
    if entered_input[i] in word and entered_input[i] not in letters_colored:
      pos[i] = 1
      letters_colored.append(entered_input[i])

  for i in range(5):
    if pos[i] == 1:
       result[i] = yellow + input_list[i]
       result[i] = result[i] + end
    elif pos[i] == 2:
      result[i] = green + input_list[i]
      result[i] = result[i] + end
    else:
      result[i] = input_list[i]
  result = ''.join(result)

  if pos == [2, 2, 2, 2, 2]:
    win = True
  return result



while True:
  win = False
  trys = 0
  past_trys = []
  word = random.choice(choose_word_list)
  while True:
    while True:
      entered_input = input()
      if entered_input.isalpha() and len(entered_input.strip()) == 5:
        if entered_input in check_word_list:
          break
        else:
          print(">Not a valid word")
      else:
        print(">Input must be 5 LETTERS long")
    past_trys.append(checker(entered_input))
    printer()
    trys += 1
    if win == True or trys == 6:
      break
    else:
      pass
  if win == True:
    print(">You win!")
  else:
    print(">You lose! The word was", word)
  while True:
    x = input(">Play again? (y/n): ")
    if x.lower() == 'y':
      break
    elif x.lower() == 'n': 
      print(">Thanks for playing!")
      break
    else:
      print(">Please enter 'y' or 'n'")
  if x.lower() == 'n':
    break
