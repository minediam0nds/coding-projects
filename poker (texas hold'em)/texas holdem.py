
import math
import random
import time

def fastcardscheck(playernum):
  if royalflush(playernum):
    num = 10
  elif straightflush(playernum):
    num = 9
  elif fourofakind(playernum):
    num = 8
  elif fullhouse(playernum):
    num = 7
  elif flush(playernum):
    num = 6
  elif straight(playernum):
    num = 5
  elif threeofakind(playernum):
    num = 4
  elif twopair(playernum):
    num = 3
  elif pair(playernum):
    num = 2
  else:
    num = 1
  return num


def comparecards():
  global player1value
  global player2value
  global player3value
  global player4value
  global player5value
  global player6value
  global player7value
  global player8value
  global player9value
  global comcardstocompare
  global allplayersingame
  global allinplayers
  global wonwithwhatdict
  breaking = False
  currentwinners = []
  finalplayerwinner = []
  comcardswins = False
  playersincompare = []
  standardmin = 0
  playersnotincompare = []
  allplayersingame.extend(allinplayers)
  for number1 in range(1, 7):
    standardmin = 0
    for playernumber in allplayersingame:
      if playernumber not in playersnotincompare:
        num = globals()[f"player{playernumber}value"][number1]
        if num > standardmin:
          standardmin = num
        elif num == standardmin:
          pass
        else:
          playersnotincompare.append(playernumber)
    for playernumber in allplayersingame:
      if playernumber not in playersnotincompare:
        num = globals()[f"player{playernumber}value"][number1]
        if num < standardmin:
          playersnotincompare.append(playernumber)
  currentwinners = allplayersingame.copy()
  for i in playersnotincompare:
    currentwinners.remove(i)




  winningvalue = globals()[f"player{currentwinners[0]}value"][1]
  wonwithwhat = wonwithwhatdict[winningvalue]
  if len(currentwinners) == 1:
    return ["solewinner", currentwinners[0] , f"{currentwinners[0]} WON WITH A {wonwithwhat}"]
  elif len(currentwinners) < len(allplayersingame):
    return ["morewinner", currentwinners  , f"TIE WITH PLAYERS {currentwinners} , ALL HAD {wonwithwhat}"]
  else:
    return ["comwinner", currentwinners , f"TIE WITH PLAYERS {currentwinners} , ALL HAD {wonwithwhat}"]






def cardscheck():
  global royalflush
  global straightflush
  global fourofakind
  global fullhouse
  global flush
  global straight
  global threeofakind
  global twopair
  global pair
  global highcard
  global player1value
  global player2value
  global player3value
  global player4value
  global player5value
  global player6value
  global player7value
  global player8value
  global player9value
  global communitycards
  global comcardstocompare
  global allplayersingame
  global allplayersingamenochange
  playervalue = [[] for _ in range(len(allplayersingamenochange))]
  print(allplayersingamenochange)
  for i in allplayersingame:
      if royalflush(i):
          globals()[f"player{i}value"] = royalflush(i).insert(0, i)
      elif straightflush(i):
          globals()[f"player{i}value"] = straightflush(i)
      elif fourofakind(i):
          globals()[f"player{i}value"] = fourofakind(i)
      elif fullhouse(i):
          globals()[f"player{i}value"] = fullhouse(i)
      elif flush(i):
          globals()[f"player{i}value"] = flush(i)
      elif straight(i):
          globals()[f"player{i}value"] = straight(i)
      elif threeofakind(i):
          globals()[f"player{i}value"] = threeofakind(i)
      elif twopair(i):
          globals()[f"player{i}value"] = twopair(i)
      elif pair(i):
          globals()[f"player{i}value"] = pair(i)
      else:
          globals()[f"player{i}value"] = highcard(i)

  if royalflush(47):
    comcardstocompare = royalflush(47)
  elif straightflush(47):
    comcardstocompare = straightflush(47)
  elif fourofakind(47):
    comcardstocompare = fourofakind(47)
  elif fullhouse(47):
    comcardstocompare = fullhouse(47)
  elif flush(47):
    comcardstocompare = flush(47)
  elif straight(47):
    comcardstocompare = straight(47)
  elif threeofakind(47):
    comcardstocompare = threeofakind(47)
  elif twopair(47):
    comcardstocompare = twopair(47)
  elif pair(47):
    comcardstocompare = pair(47)
  else:
    comcardstocompare = highcard(47)

  comcardstocompare.insert(0, 47)

  for i in range(1, 10):
    globals()[f"player{i}value"].insert(0, i)


  return comparecards()


def botplayerchoice(playernum):
  global playerbluffrate
  global pot
  global potstandard
  global playerraised
  global oneplayerleft
  playernumpos = playernum - 1
  callforplayer = potstandard - playercalls[playernum - 1]
  playermoney = playermoneys[playernum - 1]
  sunkcost = playercalls[playernum - 1]
  choice = 0
  num = fastcardscheck(playernum)
  randominteger = random.randint(1, 101)
  print("_____________________________________________")
  print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
  print(f"PLAYER {playernum} IS CHOOSING...")
  time.sleep(1)
  if callforplayer == 0:
    if currentround == 1:
      if num > 1:
        betwillingness = 50 + num*15
      else:
        betwillingness = 20
      moneywillingtobet = 25 + random.randint(1,4)*25+ num*25
    elif currentround in [2, 3, 4, 5]:
      moneywillingtobet = 50 + random.randint(1, 3)*25 + num*25
      if num > 1:
         betwillingness = 50 + num*15
      else:
         betwillingness = 20
    if randominteger < betwillingness:
      choice = 2
    else:
      choice = 1

  else:
    moneywillingtobet = 50 + random.randint(1, 3)*25 + num*50
    if callforplayer < moneywillingtobet:
      choice = 1
    else:
      if playerraised:
        callwillingness = 40 + sunkcost/20 + (50 - callforplayer/10 ) + num*10 + playerbluffrate*100
      else:
        callwillingness = 40 + sunkcost/20 + num*10 + (50 - callforplayer/10)
      if randominteger < callwillingness:
        choice = 1
      else:
        choice = 3
  if choice == 2 and playermoney <= 0:
    choice = 1
  if choice == 1:
      playermoneys[playernumpos] -= callforplayer
      if playermoneys[playernumpos] < 0 :
        playermoneys[playernumpos] = 0
      playercalls[playernumpos] = potstandard
      pot += callforplayer
      print(f"PLAYER {playernum}) CALLED {callforplayer}")
  elif choice == 2:
    betamount = moneywillingtobet - callforplayer
    playermoneys[playernumpos] -= moneywillingtobet
    if playermoneys[playernumpos] < 0:
      playermoneys[playernumpos] = 0
    playercalls[playernumpos] += betamount
    pot += betamount
    potstandard += betamount
    print(f"PLAYER {playernum}) RAISED BY {betamount}, CURRENT CALL = {potstandard - 50}")
    playerraised = False
  elif choice == 3:
    foldedplayers.append(playernum)
    print(f"PLAYER {playernum}) FOLDED")
  print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
  print("_____________________________________________")
  if len(foldedplayers) == len(allplayersingame) - 1:
    oneplayerleft = True
  return





def createplayercardswithcom(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  playercardswithcom = []
  playercards = []
  if playernum != 47:
    playercards = globals()[f"player{playernum}cards"]
    playercardswithcom.extend(playercards)
    playercardswithcom.extend(communitycards)
  else:
    playercardswithcom = communitycards
  return playercardswithcom




def royalflush(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards
  valuelists = [[] for _ in range(15)]
  returner = []
  #CDHS
  suitlists = [[] for _ in range(4)]
  straight = False
  royalflush = False
  for card in (playercardswithcom):
    number = int(cardsref[card][0])
    suit = cardsref[card][1]
    valuelists[int(number)].append(number)
    if suit == 'C':
      suitlists[0].append(number)
    elif suit == 'D':
      suitlists[1].append(number)
    elif suit == 'H':
      suitlists[2].append(number)
    elif suit == 'S':
      suitlists[3].append(number)
  for suitlist in suitlists:
    if len(suitlist) >= 5:
      suitlist.sort()
      if 10 in suitlist and 11 in suitlist and 12 in suitlist and 13 in suitlist and 14 in suitlist:
        royalflush = True
        returner.append(14)
        returner.append(13)
        returner.append(12)
        returner.append(11)
        returner.append(10)
        break
  if royalflush:
    print(returner)
    print(suitlists)
    pass
  else:
    return False
  returner.insert(0 , 10)
  return returner



def straightflush(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards
  valuelists = [[] for _ in range(15)]
  returner = []
  #CDHS
  suitlists = [[] for _ in range(4)]
  straight = False
  strflush = False
  for card in (playercardswithcom):
    number = int(cardsref[card][0])
    suit = cardsref[card][1]
    valuelists[int(number)].append(int(number))
    if number == 14:
      valuelists[1].append(1)
    if suit == 'C':
      suitlists[0].append(number)
      if number == 14:
        suitlists[0].append(1)
    elif suit == 'D':
      suitlists[1].append(number)
      if number == 14:
        suitlists[1].append(1)
    elif suit == 'H':
      suitlists[2].append(number)
      if number == 14:
        suitlists[2].append(1)
    elif suit == 'S':
      suitlists[3].append(number)
      if number == 14:
        suitlists[3].append(1)
  for suitlist in suitlists:
    if len(suitlist) >= 5:
      suitlist.sort()
      for i in range(len(suitlist) - 1,  3, -1 ):
        if suitlist[i] == suitlist[i - 1] + 1 and suitlist[i - 1] + 1 == suitlist[i - 2] + 2 and suitlist[i - 3] + 3  == suitlist[i - 4] + 4:
          returner.append(suitlist[i])
          returner.append(suitlist[i - 1])
          returner.append(suitlist[i - 2])
          returner.append(suitlist[i - 3])
          returner.append(suitlist[i - 4])
          strflush = True
          break
  if strflush:
    pass
  else:
    return False
  returner.insert(0, 9)
  return returner





def fourofakind(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom
  returner = []
  valuelists = [[] for _ in range(15)]
  fourofakind = False
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards

  for card in playercardswithcom:
    number = int(cardsref[card][0])
    valuelists[number].append(number)

  for valuelist in valuelists:
    if len(valuelist) == 4:
      fourofakind = True
      returner.extend(valuelist)
      valuelist.clear()
      break

  if not fourofakind:
    return False
  else:
    valuelists[1].clear()
    for i in range(len(valuelists) -1 , -1 , -1):
      if valuelists[i]:
        returner.append(valuelists[i][0])

  returner = returner[:5]
  returner.insert(0, 8)
  return returner

def fullhouse(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  quickleave = True
  returner = []
  valuelists = [[] for _ in range(15)]
  fullhouse = False
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards
  for card in playercardswithcom:
    number = int(cardsref[card][0])
    valuelists[number].append(number)
  for i in range(len(valuelists) -1, -1 , -1):
    if len(valuelists[i]) == 3:
      returner.extend(valuelists[i])
      valuelists[i].clear()
      quickleave = False
      break
  if quickleave:
    return False
  for i in range(len(valuelists) - 1, -1 , -1):
    if len(valuelists[i]) >= 2:
      returner.extend(valuelists[i][0:2])
      fullhouse = True
      break
  if fullhouse:
    pass
  else:
    return False
  returner.insert(0, 7)
  return returner

def flush(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom

  suitlists = [[] for _ in range(5)]
  valuelists = [[] for _ in range(15)]
  returner = []
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards

  flush = False


  for card in playercardswithcom:
    number = int(cardsref[card][0])
    suit = str(cardsref[card][1])
    valuelists[int(number)].append(int(number))

    if suit == 'C':
      suitlists[0].append(number)
    elif suit == 'D':
      suitlists[1].append(number)
    elif suit == 'H':
      suitlists[2].append(number)
    elif suit == 'S':
      suitlists[3].append(number)
  for suitlist in suitlists:
    if len(suitlist) >= 5:
      suitlist.sort(reverse=True)
      flush = True
      for i in range(5):
        returner.append(suitlist[i])
      returner.insert(0, 6)
      return returner

  return False

def straight(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom
  wheel = False
  returner = []
  valuelists = [[] for _ in range(15)]
  straight = False

  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards

  for card in playercardswithcom:
    number = str(cardsref[card][0])
    if number == '14':
      valuelists[1].append(1)
    valuelists[int(number)].append(int(number))

  for i in range(len(valuelists) - 1, -1 , -1):
    if valuelists[i] and valuelists[i-1] and valuelists[i-2] and valuelists[i-3] and valuelists[i-4]:
      returner.append(valuelists[i][0])
      returner.append(valuelists[i-1][0])
      returner.append(valuelists[i-2][0])
      returner.append(valuelists[i-3][0])
      returner.append(valuelists[i-4][0])
      straight = True
      returner.insert(0, 5)
      return returner
  return False



def threeofakind(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom
  valuelists = [[] for _ in range(15)]
  threeofakind = False
  returner = []
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards

  for card in playercardswithcom:
    number = int(cardsref[card][0])
    valuelists[number].append(number)
  for i in range(len(valuelists) -1, -1 , -1):
    if len(valuelists[i]) == 3:
      returner.extend(valuelists[i])
      valuelists[i].clear()
      threeofakind = True

  if threeofakind:
    for i in range(len(valuelists) -1, -1 , -1):
      if valuelists[i]:
        returner.extend(valuelists[i])
        returner = returner[:5]
    returner.insert(0, 4)
    return returner
  return False

def twopair(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom
  quickleave = True
  valuelists = [[] for _ in range(15)]
  returner = []
  firstpair = False
  twopair = False
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards

  for card in playercardswithcom:
    num = int(cardsref[card][0])
    valuelists[num].append(num)
  for i in range(len(valuelists) -1 , -1 , -1):
    if len(valuelists[i]) == 2:
      returner.extend(valuelists[i])
      valuelists[i].clear()
      firstpair = True
      break
  if not firstpair:
    return False
  for i in range(len(valuelists) -1 , -1 , -1):
    if len(valuelists[i]) == 2:
      returner.extend(valuelists[i])
      valuelists[i].clear()
      twopair = True
      break
  if twopair:
    for i in range(len(valuelists) -1 , -1 , -1):
      if valuelists[i]:
        returner.append(valuelists[i][0])
        returner = returner[:5]
    returner.insert(0, 3)
    return returner

  return False





def pair(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  pairbool = False
  returner = []
  valuelists = [[] for _ in range(15)]
  if playernum != 47:
    playercardswithcom = createplayercardswithcom(playernum)
  else:
    playercardswithcom = communitycards
  for card in playercardswithcom:
    number = str(cardsref[card][0])
    valuelists[int(number)].append(int(number))
  for i in range(len(valuelists) - 1, -1 , -1 ):
    if len(valuelists[i]) == 2:
      returner.extend(valuelists[i])
      valuelists[i].clear()
      pairbool = True
      break
  if pairbool:
    for i in range(len(valuelists) -1 , -1 , -1 ):
      if valuelists[i]:
        returner.extend(valuelists[i])
    returner = returner[:5]
    returner.insert(0, 2)
    return returner
  else:
    return False





def highcard(playernum):
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global createplayercardswithcom
  valuelists = [[] for _ in range(15)]
  returner = []
  playercardswithcom = createplayercardswithcom(playernum)
  for card in playercardswithcom:
    number = str(cardsref[card][0])
    valuelists[int(number)].append(int(number))
  for lists in range(len(valuelists) -1 , -1 ,-1):
    if valuelists[lists]:
      for item in range(len(valuelists[lists])):
        returner.append(valuelists[lists][item])

  returner = returner[:5]
  returner.insert(0, 1)
  return returner













def distribute(num, playernum):
  global cards
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  for i in range(num):
    cardgiven = random.choice(list(cards.keys()))
    if playernum == 1:
        player1cards.append(cardgiven)
    elif playernum == 2:
        player2cards.append(cardgiven)
    elif playernum == 3:
        player3cards.append(cardgiven)
    elif playernum == 4:
        player4cards.append(cardgiven)
    elif playernum == 5:
        player5cards.append(cardgiven)
    elif playernum == 6:
        player6cards.append(cardgiven)
    elif playernum == 7:
        player7cards.append(cardgiven)
    elif playernum == 8:
        player8cards.append(cardgiven)
    elif playernum == 9:
        player9cards.append(cardgiven)
    del cards[cardgiven]



def playerchoice(playernum):
  global playermoneys
  global playercalls
  global potstandard
  global pot
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards
  global currentround
  global foldedplayers
  global allinplayers
  global playerraised
  global oneplayerleft
  playernumpos = playernum - 1
  mustgoallin = False

  if playernum in foldedplayers:
    pass
  else:
    while True:
      playercard = eval(f"player{playernum}cards")
      thisplayercall = playercalls[playernumpos]
      callforplayer = potstandard - thisplayercall
      thisplayermoney = playermoneys[playernumpos]
      print(allplayersingame)
      if callforplayer >= thisplayermoney :
        mustgoallin = True
        askchoicestring = f"1. Call (All in ${thisplayermoney})\n2.Fold"
      else:
        askchoicestring = f"1. Call (${callforplayer})\n2.Raise\n3.Fold"
        if callforplayer == 0:
          askchoicestring = f"1. Check ($0)\n2.Raise\n3.Fold"

      print("--------------------------------")
      print("ALL PLAYER'S MONEY: ", playermoneys)
      print("POT: $", pot)
      print("____________________________________")
      print("PLAYER: ", playernum ,  "Money: " , thisplayermoney)
      print("")
      if currentround > 1:
        print("COMMUNITY CARDS: ",communitycards)
      print("YOUR CARDS:      ",playercard)
      print("")
      print("____________________________________")
      print(askchoicestring)
      choice = input("Input choice (1-3): ")
      print("-------------------------------")
      if choice == '1':
        playermoneys[playernumpos] -= callforplayer
        if playermoneys[playernumpos] < 0 :
          playermoneys[playernumpos] = 0
        playercalls[playernumpos] = potstandard
        pot += callforplayer
        break
      elif choice == '2':
        if mustgoallin:
          foldedplayers.append(playernum)
          allinplayers.append(playernum)
        else:
          betamount = isvaliddigitinput(f"Input amount to bet(increase from ${callforplayer}): ", 0 , thisplayermoney - callforplayer)
          playermoneys[playernumpos] -= callforplayer + betamount
          potstandard += betamount
          playercalls[playernumpos] = potstandard
          pot += callforplayer + betamount
          playerraised = True
          break


      elif choice == '3':
        foldedplayers.append(playernum)
        print(foldedplayers)
        if len(foldedplayers) == len(allplayersingame) - 1:
          oneplayerleft = True
        break
      elif choice == '4':
        playermoneys[playernumpos] = 0
        print("------------------------------")
        print("|Please input a  valid number|" )
        print("------------------------------")










def firstround():
  global currentround
  global pot
  global potstandard
  print("+++++++++++++++++++")
  print("ROUND : PREFLOP")
  print("+++++++++++++++++++")
  for i in allplayersingame:
    distribute(2, i)
  currentround = 1
  pot = len(allplayersingame) * 50
  potstandard = 50
  for i in allplayersingame:
    playercalls[i - 1] = 50
    playermoneys[i - 1] -= 50

  if singleplayer:
    for i in range(len(allplayersingame)):
      if allplayersingame[i] not in foldedplayers:
        if oneplayerleft:
          return endgame()
        if allplayersingame[i] == 1:
          playerchoice(1)
        else:
          botplayerchoice(allplayersingame[i])
    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            if i == 1:
              playerchoice(i)
            else:
              botplayerchoice(i)
      if allplayersareequaltostandard:
        break


  else:
    for i in range(len(allplayersingame)):
      playerchoice(allplayersingame[i])
      if oneplayerleft:
          return endgame()
    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            playerchoice(i)
      if allplayersareequaltostandard:
        break
  secondround()




def secondround():
  global cards
  global currentround
  global foldedplayers
  global communitycards
  print("+++++++++++++++++++")
  print("ROUND : FLOP")
  print("+++++++++++++++++++")
  currentround = 2

  for i in range(3):
    cardtogive = random.choice(list(cards.keys()))
    communitycards.append(cardtogive)
    del cards[cardtogive]

  if singleplayer:
    for i in range(len(allplayersingame)):
      if oneplayerleft:
        return endgame()
      if allplayersingame[i] not in foldedplayers:
        if allplayersingame[i] == 1:
          playerchoice(1)
        else:
          botplayerchoice(allplayersingame[i])
    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            if i == 1:
              playerchoice(i)
            else:
              botplayerchoice(i)
      if allplayersareequaltostandard:
        break

  else:
    for i in range(len(allplayersingame)):
      if oneplayerleft:
        return endgame()
      playerchoice(allplayersingame[i])

    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            playerchoice(i)
      if allplayersareequaltostandard:
        break

  thirdround()


def thirdround():
  global cards
  global currentround
  global foldedplayers
  global commuitycards
  print("+++++++++++++++++++")
  print("ROUND : TURN")
  print("+++++++++++++++++++")
  currentround = 3

  cardtogive = random.choice(list(cards.keys()))
  communitycards.append(cardtogive)
  del cards[cardtogive]
  if singleplayer:
    for i in range(len(allplayersingame)):
      if oneplayerleft:
        return endgame()
      if allplayersingame[i] not in foldedplayers:
        if allplayersingame[i] == 1:
          playerchoice(1)
        else:
          botplayerchoice(allplayersingame[i])
    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            if i == 1:
              playerchoice(i)
            else:
              botplayerchoice(i)
      if allplayersareequaltostandard:
        break
  else:
    for i in allplayersingame:
      if oneplayerleft:
        return endgame()
      playerchoice(i)

    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            playerchoice(i)
      if allplayersareequaltostandard:
        break
  fourthround()

def fourthround():
  global cards
  global currentround
  global endgame
  global pot
  global playermoneys
  global allplayersingame
  global foldedplayers
  global communitycards
  global timesbluffed
  global playerbluffrate
  print("+++++++++++++++++++")
  print("ROUND : RIVER")
  print("+++++++++++++++++++")
  currentround = 4

  cardtogive = random.choice(list(cards.keys()))
  communitycards.append(cardtogive)
  del cards[cardtogive]
  if singleplayer:
    for i in range(len(allplayersingame)):
      if oneplayerleft:
        return endgame()
      if allplayersingame[i] not in foldedplayers:
        if allplayersingame[i] == 1:
          playerchoice(1)
        else:
          botplayerchoice(allplayersingame[i])
    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            if i == 1:
              playerchoice(i)
            else:
              botplayerchoice(i)
      if allplayersareequaltostandard:
        break
  else:
    for i in allplayersingame:
      if oneplayerleft:
        return endgame()
      playerchoice(i)

    while True:
      allplayersareequaltostandard = True
      for i in allplayersingame:
        if oneplayerleft:
          return endgame()
        if i not in foldedplayers:
          if playercalls[i - 1] != potstandard:
            allplayersareequaltostandard = False
            playerchoice(i)
      if allplayersareequaltostandard:
        break
  for i in foldedplayers:
    allplayersingame.remove(i)
  print

  endgame()

def endgame():
  global currentround
  global endgame
  global pot
  global playermoneys
  global allplayersingame
  global foldedplayers
  global communitycards
  global timesbluffed
  global playerbluffrate
  for i in range(len(allplayersingamenochange)):
    cardsofcurrentplayer = globals()[f"player{allplayersingamenochange[i]}cards"]
    print(f"PLAYER {allplayersingamenochange[i]} CARDS: {cardsofcurrentplayer}")
  print("COMMUNITY CARDS: ", communitycards)
  if oneplayerleft:
    for i in foldedplayers:
      allplayersingame.remove(i)
    winner = ["solewinner", allplayersingame[0] , f"{allplayersingame[0]} WON (REST OF PLAYERS FOLDED)"]
  else:
    winner = cardscheck()
  if winner[0] == "solewinner":
    playermoneys[winner[1] - 1] += pot
    print(winner[2], f"(+${pot})")
  elif winner[0] == "morewinner":
    foreach = round(pot / len(winner[1]))
    print(winner[2], f"(+${foreach})")
    for i in winner[1]:
      playermoneys[i - 1] += foreach
  elif winner[0] == "comwinner":
    foreach = round(pot / len(allplayersingame))
    print(winner[2], f"(+${foreach})")
    for i in allplayersingame:
      playermoneys[i - 1] += foreach
  if singleplayer:
    if fastcardscheck(1) > playercalls[0] / 250:
      timesbluffed += 1
      playerbluffrate = round(timesbluffed / roundsplayed)
  pot = 0
  return 1



def psuedogame(cards1, cards2, cards3, cards4, cards5, cards6, cards7, cards8, cards9, comcards1):

  global cards
  global currentround
  global endgame
  global pot
  global playermoneys
  global allplayersingame
  global foldedplayers
  global player1cards
  global player2cards
  global player3cards
  global player4cards
  global player5cards
  global player6cards
  global player7cards
  global player8cards
  global player9cards
  global communitycards

  player1cards = cards1
  player2cards = cards2
  player3cards = cards3
  player4cards = cards4
  player5cards = cards5
  player6cards = cards6
  player7cards = cards7
  player8cards = cards8
  player9cards = cards9
  communitycards = comcards1
  allplayersingamenochange = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
  winner = cardscheck()
  if winner[0] == "solewinner":
    playermoneys[winner[1] - 1] += pot
  elif winner[0] == "morewinner":
    foreach = round(pot / len(winner[1]))
    for i in winner[1]:
      playermoneys[i - 1] += foreach
  elif winner[0] == "comwinner":
    foreach = round(pot / len(allplayersingame))
    for i in allplayersingame:
      playermoneys[i - 1] += foreach
  pot = 0
  print("DODNIEONDOINDOAENODNENDIONAODNOIAENDIANODNAOENDAINDOEANDOIANDOAENDONEADONAEIO", winner)




def isvaliddigitinput(question , min , max ):
  thequestion = str(f"{question} ({min} - {max}): ")
  while True:
    theinput = input(f"{question} ({min}-{max}): ")
    if theinput.isdigit():
      if int(theinput) <= max and int(theinput) >= min:
        return int(theinput)
      else:
        print("-----------------------------------")
        print(f"ERROR: INPUT MUST BE {min} - {max}")
        print("-----------------------------------")
    else:
      print("---------------------------")
      print("ERROR: INPUT MUST BE NUMBER")
      print("---------------------------")

#BEGIN VARIABLE INITIALISATION
player1cards = []
player2cards = []
player3cards = []
player4cards = []
player5cards = []
player6cards = []
player7cards = []
player8cards = []
player9cards = []
player1value = []
player2value = []
player3value = []
player4value = []
player5value = []
player6value = []
player7value = []
player8value = []
player9value = []
allplayersingame = []
allplayersingamenochange = []
foldedplayers = []
allplayersingame = []
allinplayers = []
communitycards = []
playermoneys = []
playercalls = []
bankruptplayers = []
timesbluffed = 0
roundsplayed = 1
currentround = 0
playerbluffrate = 0
pot = 0
potstandard = 0
playerraised = False
singleplayer = False
oneplayerleft = False
wonwithwhatdict = {
    1: "HIGH CARD",
    2: "PAIR",
    3: "TWO PAIR",
    4: "THREE OF A KIND",
    5: "STRAIGHT",
    6: "FLUSH",
    7: "FULL HOUSE",
    8: "FOUR OF A KIND",
    9: "STRAIGHT FLUSH",
    10: "ROYAL FLUSH"
}
#END VARIABLE INITIALISATION
input1 = isvaliddigitinput("Singleplayer?\n1.Yes\n2.No\n", 1, 2)
if input1 == 1:
  singleplayer = True
else:
  singleplayer = False
if singleplayer:
  for i in range(4):
    allplayersingamenochange.append(i + 1)
    playermoneys.append(1000)
    playercalls.append(0)
else:
  input2 = isvaliddigitinput("How many players?", 2, 9)
  for i in range(input2):
    allplayersingamenochange.append(i + 1)
    playermoneys.append(1000)
    playercalls.append(0)




while True:

  allplayersingame = allplayersingamenochange.copy()
  player1cards = []
  player2cards = []
  player3cards = []
  player4cards = []
  player5cards = []
  player6cards = []
  player7cards = []
  player8cards = []
  player9cards = []
  player1value = []
  player2value = []
  player3value = []
  player4value = []
  player5value = []
  player6value = []
  player7value = []
  player8value = []
  player9value = []
  communitycards = []
  foldedplayers = []
  allinplayers = []
  currentround = 0
  oneplayerleft = False
  playerraised = False
  value = 0
  pot = 0
  potstandard = 0
  for i in range(len(allplayersingamenochange)):
    playercalls[i] = 0



  cards = {
      '[Ace/Hearts]': (14, 'H'), '[Ace/Diamonds]': (14, 'D'), '[Ace/Clubs]': (14, 'C'), '[Ace/Spades]': (14, 'S'),
      '[Two/Hearts]': (2, 'H'), '[Two/Diamonds]': (2, 'D'), '[Two/Clubs]': (2, 'C'), '[Two/Spades]': (2, 'S'),
      '[Three/Hearts]': (3, 'H'), '[Three/Diamonds]': (3, 'D'), '[Three/Clubs]': (3, 'C'), '[Three/Spades]': (3, 'S'),
      '[Four/Hearts]': (4, 'H'), '[Four/Diamonds]': (4, 'D'), '[Four/Clubs]': (4, 'C'), '[Four/Spades]': (4, 'S'),
      '[Five/Hearts]': (5, 'H'), '[Five/Diamonds]': (5, 'D'), '[Five/Clubs]': (5, 'C'), '[Five/Spades]': (5, 'S'),
      '[Six/Hearts]': (6, 'H'), '[Six/Diamonds]': (6, 'D'), '[Six/Clubs]': (6, 'C'), '[Six/Spades]': (6, 'S'),
      '[Seven/Hearts]': (7, 'H'), '[Seven/Diamonds]': (7, 'D'), '[Seven/Clubs]': (7, 'C'), '[Seven/Spades]': (7, 'S'),
      '[Eight/Hearts]': (8, 'H'), '[Eight/Diamonds]': (8, 'D'), '[Eight/Clubs]': (8, 'C'), '[Eight/Spades]': (8, 'S'),
      '[Nine/Hearts]': (9, 'H'), '[Nine/Diamonds]': (9, 'D'), '[Nine/Clubs]': (9, 'C'), '[Nine/Spades]': (9, 'S'),
      '[Ten/Hearts]': (10, 'H'), '[Ten/Diamonds]': (10, 'D'), '[Ten/Clubs]': (10, 'C'), '[Ten/Spades]': (10, 'S'),
      '[Jack/Hearts]': (11, 'H'), '[Jack/Diamonds]': (11, 'D'), '[Jack/Clubs]': (11, 'C'), '[Jack/Spades]': (11, 'S'),
      '[Queen/Hearts]': (12, 'H'), '[Queen/Diamonds]': (12, 'D'), '[Queen/Clubs]': (12, 'C'), '[Queen/Spades]': (12, 'S'),
      '[King/Hearts]': (13, 'H'), '[King/Diamonds]': (13, 'D'), '[King/Clubs]': (13, 'C'), '[King/Spades]': (13, 'S')
  }
  cardsref = {
      '[Ace/Hearts]': (14, 'H'), '[Ace/Diamonds]': (14, 'D'), '[Ace/Clubs]': (14, 'C'), '[Ace/Spades]': (14, 'S'),
      '[Two/Hearts]': (2, 'H'), '[Two/Diamonds]': (2, 'D'), '[Two/Clubs]': (2, 'C'), '[Two/Spades]': (2, 'S'),
      '[Three/Hearts]': (3, 'H'), '[Three/Diamonds]': (3, 'D'), '[Three/Clubs]': (3, 'C'), '[Three/Spades]': (3, 'S'),
      '[Four/Hearts]': (4, 'H'), '[Four/Diamonds]': (4, 'D'), '[Four/Clubs]': (4, 'C'), '[Four/Spades]': (4, 'S'),
      '[Five/Hearts]': (5, 'H'), '[Five/Diamonds]': (5, 'D'), '[Five/Clubs]': (5, 'C'), '[Five/Spades]': (5, 'S'),
      '[Six/Hearts]': (6, 'H'), '[Six/Diamonds]': (6, 'D'), '[Six/Clubs]': (6, 'C'), '[Six/Spades]': (6, 'S'),
      '[Seven/Hearts]': (7, 'H'), '[Seven/Diamonds]': (7, 'D'), '[Seven/Clubs]': (7, 'C'), '[Seven/Spades]': (7, 'S'),
      '[Eight/Hearts]': (8, 'H'), '[Eight/Diamonds]': (8, 'D'), '[Eight/Clubs]': (8, 'C'), '[Eight/Spades]': (8, 'S'),
      '[Nine/Hearts]': (9, 'H'), '[Nine/Diamonds]': (9, 'D'), '[Nine/Clubs]': (9, 'C'), '[Nine/Spades]': (9, 'S'),
      '[Ten/Hearts]': (10, 'H'), '[Ten/Diamonds]': (10, 'D'), '[Ten/Clubs]': (10, 'C'), '[Ten/Spades]': (10, 'S'),
      '[Jack/Hearts]': (11, 'H'), '[Jack/Diamonds]': (11, 'D'), '[Jack/Clubs]': (11, 'C'), '[Jack/Spades]': (11, 'S'),
      '[Queen/Hearts]': (12, 'H'), '[Queen/Diamonds]': (12, 'D'), '[Queen/Clubs]': (12, 'C'), '[Queen/Spades]': (12, 'S'),
      '[King/Hearts]': (13, 'H'), '[King/Diamonds]': (13, 'D'), '[King/Clubs]': (13, 'C'), '[King/Spades]': (13, 'S')
  }

  firstround()
  roundsplayed += 1

  for i in range(len(playermoneys)):
    if playermoneys[i] <= 0 and i+1 not in bankruptplayers:
      allplayersingamenochange.remove(i + 1)
      print("PLAYER " , str(i + 1) , "IS BANKRUPT (REMOVED FROM THE GAME)")
      bankruptplayers.append(i + 1)

  if singleplayer and playermoneys[0] <= 0:
    print("YOU ARE BANKRUPT : GAME OVER")
    break
  while True:
    choice = input("CONTINUE TO NEXT ROUND? (Y/N): ")
    if choice == 'Y' or choice == 'y':
      break
    elif choice == 'N' or choice == 'n':
      break
    else:
      print("INPUT MUST BE 'Y' OR 'N'")
  if choice == 'N' or choice == 'n':
    break
  print("NEXT ROUND")
print("THANK YOU FOR PLAYING!")








