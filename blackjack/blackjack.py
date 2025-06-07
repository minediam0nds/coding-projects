
import random
import time
money = 1000

def askpot(theinput):
  if theinput.isdigit():
    return True
  else:
    print("Invalid input. Please enter a number")
    return False
def moneysense(money, num):
  while True:
    if int(money) < (num):
      return False
      break
    else:
      return True
      break

def checkforace():
  if "[Ace/Hearts]" in playercards or "[Ace/Diamonds]" in playercards or "[Ace/Clubs]" in playercards or "[Ace/Spades]":
    return True
#def acehigh(num):
  #if num = 111111
    #return True
  #else:
    #return False

while True:
  blackjack = False
  tie = False
  win = False
  pot = 0
  numcards = 0
  playercards = ""
  firstcard = ""
  secondcard = ""
  dealercards = ""
  numdealer = 0
  ended = False
  cards = {
    '[Ace/Hearts]': 1, '[Ace/Diamonds]': 1, '[Ace/Clubs]': 1, '[Ace/Spades]': 1,
    '[Two/Hearts]': 2, '[Two/Diamonds]': 2, '[Two/Clubs]': 2, '[Two/Spades]': 2,
    '[Three/Hearts]': 3, '[Three/Diamonds]': 3, '[Three/Clubs]': 3, '[Three/Spades]': 3,
    '[Four/Hearts]': 4, '[Four/Diamonds]': 4, '[Four/Clubs]': 4, '[Four/Spades]': 4,
    '[Five/Hearts]': 5, '[Five/Diamonds]': 5, '[Five/Clubs]': 5, '[Five/Spades]': 5,
    '[Six/Hearts]': 6, '[Six/Diamonds]': 6, '[Six/Clubs]': 6, '[Six/Spades]': 6,
    '[Seven/Hearts]': 7, '[Seven/Diamonds]': 7, '[Seven/Clubs]': 7, '[Seven/Spades]': 7,
    '[Eight/Hearts]': 8, '[Eight/Diamonds]': 8, '[Eight/Clubs]': 8, '[Eight/Spades]': 8,
    '[Nine/Hearts]': 9, '[Nine/Diamonds]': 9, '[Nine/Clubs]': 9, '[Nine/Spades]': 9,
    '[Ten/Hearts]': 10, '[Ten/Diamonds]': 10, '[Ten/Clubs]': 10, '[Ten/Spades]': 10,
    '[Jack/Hearts]': 10, '[Jack/Diamonds]': 10, '[Jack/Clubs]': 10, '[Jack/Spades]': 10,
    '[Queen/Hearts]': 10, '[Queen/Diamonds]': 10, '[Queen/Clubs]': 10, '[Queen/Spades]': 10,
    '[King/Hearts]': 10, '[King/Diamonds]': 10, '[King/Clubs]': 10, '[King/Spades]': 10
}

  while True:
      potinput = input("How much do you want to bet? (1-" + str(money) + "): ")
      if askpot(potinput) == True:
        if moneysense(int(money), int(potinput)) == True:
          break
        else:
          print("Not enough money")


  pot = int(potinput)
  money -= pot
  print("--------------------------------")
  print("You have " + str(money) + " left")
  print("Pot: " + str(pot))
  print("--------------------------------")


  firstcard = random.choice(list(cards.keys()))
  playercards += firstcard + " "
  numcards += int(cards.get(firstcard))
  cards.pop(firstcard)

  secondcard = random.choice(list(cards.keys()))
  playercards += " " + secondcard
  numcards += int(cards.get(secondcard))
  cards.pop(secondcard)
  print("Your Cards: ")
  print(playercards)
  print("--------------------------------")
  num = 0

  firstdealer = random.choice(list(cards.keys()))
  dealercards += firstdealer + " "
  numdealer += int(cards.get(firstdealer))
  print("Dealer's Upcard: ")
  print(firstdealer + "  [HOLE CARD]")
  print("--------------------------------")
  print("")
  print("")
  cards.pop(firstdealer)

  seconddealer = random.choice(list(cards.keys()))
  dealercards += " " + seconddealer
  numdealer += int(cards.get(seconddealer))
  cards.pop(seconddealer)

  while True:
    num += 1
    print("--------------------------------")
    choice = input("Hit or Stand? (h/s): ")
    print("--------------------------------")
    if choice == "h":
      print("You chose hit")
      newcard = random.choice(list(cards.keys()))
      playercards += " " + newcard
      numcards += cards.get(newcard)
      cards.pop(newcard)
      print(playercards)
      if numcards > 21:
        print("\033[1mYOU LOSE\033[0m (bust) >>" + str(numcards))
        ended = True
        win = False
        break
      elif numcards == 21:
          print("\033[1mYOU WIN!\033[0m (blackjack)")
          ended = True
          blackjack = True
          win = True
          break
    elif choice == 's':
        print("You chose stand")
        print("--------------------------------")
        break
    else:
        print("Invalid choice")
  if not ended:

      print("Dealer's Turn")
      print("Dealer's Cards:")
      print(dealercards)
      while numdealer < 17:
        print("Dealer choosing...")
        time.sleep(3)
        print("Dealer chose hit: ")
        newdealer = random.choice(list(cards.keys()))
        dealercards += " " + newdealer
        numdealer += cards.get(newdealer)
        cards.pop(newdealer)
        print(dealercards)
        if numdealer > 17:
          break
        elif numdealer == 21:
          break
      print("Dealer choosing ...")
      time.sleep(3)
      print("Dealer chose stand")




      print("--------------------------------")
      print("--------------------------------")
      print("--------------------------------")
      print("Your Cards: " + str(numcards))
      print(playercards)
      print("--------------------------------")
      print("Dealer's Cards: " + str(numdealer))
      print(dealercards)
      print("--------------------------------")

      if numdealer > 21:
          print("\033[1mYOU WIN!\033[0m (dealer bust)")
          win = True
      elif numcards > numdealer:
          print("\033[1mYOU WIN!\033[0m (more than dealer)")
          win = True
      elif numcards < numdealer:
          print("\033[1mYOU LOSE\033[0m (less than dealer)")
          win = False
      else:
          print("it's a tie!")
          tie = True
          win = False

  print("--------------------------------")
  print("--------------------------------")
  if win == True:
    money += pot * 2
    print("You won " + str(pot * 2) + "!")
  elif win == False:
    print("You lost " + str(pot) + "!")
  elif tie == True:
    money += pot
    print("It's a tie! (No loss/win)")
  print("You have " + str(money) + " left")
  print("--------------------------------")
  print("")
  print("")



  while True:
    gamechoice = input("Do you want to play again? (y/n): ")
    if gamechoice == "y" or gamechoice == "n":
      break
    else:
      print("Invalid choice")
  if gamechoice == "n":
    print("You had " + str(money) + " left")
    print("Thanks for playing!")
    break

