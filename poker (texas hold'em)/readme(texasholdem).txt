this is definitely my favourite coding project. i worked on this project during late sec3 to early sec4 at school, usually in between classes and in the morning. the whole program took me about 4 months 

i learnt the most from this out of all my projects (with chatgpt as my teacher haha), but i still wanted the project to be 'mine', so i never copied and paste any code. i was still only knew beginner-level python, so i needed chatgpt to learn how to iterate backwards and stuff like that.

obviously the code isnt very efficient, and its quite messsy and unreadable (i didn't write any comments), but all the ideas for the player's hand evaluation are mine and im pround of them :)


here's an explanation of how the code works so i wont subject you to the pain of reading through it:

    the game begins with randomly distributing the cards to each player from a dictionary.
    
    firstround(), secondround(), thirdround(), and  fourthround() are all basically the same, adding community cards according to poker rules and then allowing players to call, raise and fold. They all call the next round's function.

    playerchoice() displays the users cards and community cards then asks for their choice to call, raise or fold.

    fourthround() calls endgame(). endgame() first calls cardscheck(if more than 1 players left)

    cardscheck(), comparecards(), endgame() and all the functions called in cardscheck() are part of the poker-hand evaluation

    now i will explain the most time-consming and challenging part of the code for me; all the functions called in cardscheck():

--------------------------------------------------------

    all the functions return the 'returner' variable e.g  [2, 4, 14, 14, 14, 13, 10]
    
    the first int is the players number, in this case player 2
    the second int is the players poker-hand value, in this case 4 (corresponding to three of a kind)
    the rest of the integers are the cards and kickers, in this case 14, 14, 14, 13, 10 (Ace, Ace, Ace, King (kicker) ,10 (second kicker))


    all of the functions also follow similar steps:
        1.initialise valuelists, a list of 15 lists
        2.arrange the card in the lists according to their values (e.g 10 goes in valuelists[10] and queen goes in valuelist[12])
        3.iterate through them backwards until it satisfies a certain condition for the respective card combination
         (iterating backwards finds the highest combination first   ,e.g if a player has cards 3 - 10 it will return 10-5 as the straight)
        4. pop and append the combination to returner in descending order, if the card combination <5 cards (eg three of a kind) iterate backwards again and append until 5 cards to get highest kickers.
        
    ill start from the simplest:

        highcard():
            iterates backwards and appends to returner

        pair():
            iterates backwards through valuelists until len(valuelists[i]) == 2, append and clear valuelists[i]
            then iterate backwards and appends 3 kicker cards

        twopair():
            iterates backwards through valuelists until len(valuelists[i]) == 2, append and clear valuelists[i]
            then repeat ^
            then iterate backwards and appends 1 kicker card

        threeofakind():
            iterates backwards through valuelists until len(valuelists[i]) == 3, append and clear valuelists[i]
            then iterate backwards and appends 2 kicker cards

        straight():
            when sorting cards into valuelists, if the current number is 14 (Ace), append 1 to valuelists[1], this is for a 'wheel straight', which is: Ace, 2 , 3 , 4, 5
            iterates backwards through valuelists until valuelist[i], valuelists[i-1]...,valuelists[i-4] have atleast one card, append to returner and clear the 5 lists

        flush():
            initialises suitlists (list of 4 lists) variable, and sorts cards according to their suit
            iterates through suitlists until len(suitlists[i]) == 5, appends to returner 

        fullhouse():
            iterates backwards through valuelists until len(valuelists[i]) == 3, append and clear valuelists[i]
            then iterates backwards until through valuelists until len(valuelists[i]) == 2, append and clear valuelists[i]

        fourakind():
            iterates backwards through valuelists until len(valuelists[i]) == 4, append and clear valuelists[i]
            then iterate backwards and appends 1 kicker card

        straightflush():
           uses suitlists and appends card values based on their suit,  same sorting exception as straight() for aces.
           for suitlist in suitlist:
                sorts suitlist and then iterates backwards until next 5 numbers are one after the other, then appends to returner
            
        royalflush():
            same as straightflush(), except when iterating through suitlists, check if the 5 highest cards are present (ace - 10)
           
   now for cardscheck():
        cardscheck calls all of these functions in descending order (royalflush to highcards), and then sets playerxvalue to the returned value
        i noticed i made a comcardstocompare variable, but i dont think i ever used it everywhere as i found a more effecient way to find if the community cards have the highest hand, so pay no mind to it

	
        after this, cardscheck() calls comparecards()
        comparecards() first compares the second number of all the playerxvalues (starting at i=1 to skip the first as that is the player number) and adds the players who arent equal to the highest num to playersnotincompare
        player numbers inside playersnotincompare will be skipped in the comparing process and will be removed at the end
        if there is still >1 players left in the compare process, it will repeat the for the next numbers until it reaches the end

        iterates through playersnotincompare and removes them from currentwinner (just a list of all the players in the game)
        if there are still >1 players left in currentwinner once it reaches to end (i=6), the pot will be split according to official poker rules

        >>
        heres an example situation:

        player one has a pair and three kickers       - [1, 2, 5, 5, 13, 3]
        player two has a threeofakind and two kickers - [2, 4, 5, 5, 5, 13, 10]
        player three has a threeofakind and two kickers - [2, 4, 5, 5, 5, 13, 12]
        
        compare all playervalues[i=1]:
            player one is removed as his hand value is 2 which is less that 4
        compare all playervalues[i=2 to 5]:
            no change as all numbers are the same
        compare all playervalues[i=6]:
            playertwo is removed as 10 is less that 12

        after removing all losers, len(currentwinners) == 1 ,so sole winner is player three
 

-------------------------------

    now the bot players. i wanted the bot players to be intelligent and actually respond to whats happening in the game, and not randomly make decisions, so i came up with this idea:

    the bots would take in some factors of the game (like the amount it has to call, and the value of its current hand) and add that to a number which will serve as a probability percentage.
    the bot then takes a random integer and compares it to the probability value. if randint > probabilityvalue, the bot will call a players bet/make a bet , or  fold/dont bet anything

    i chose this probability system also so that the players will be unable to tell what the bot has in its hand, (e.g with only mathematical calculations choosing the amount to bet, like handvalue*50, the player can get a good idea on what the bot has when looking at the amount it bets.)

    heres a few lines from botplayerchoice():
    -
      if playerraised:
        callwillingness = 40 + sunkcost/20 + (50 - callforplayer/10 ) + num*10 + playerbluffrate*100
      else:
        callwillingness = 40 + sunkcost/20 + num*10 + (50 - callforplayer/10)
    -
            
    the playerraised bool (only used in singleplayer) just represents whether the current bet raise was made by the player, and if it is True the callwillingness (probability value) will include playerbluffrate - explained later

    sunkcost/20 		-- sunkcost is the amount that the bot player has played already in the game, the divisor is just a number i thought would work well

    (50 - callforplayer/10)  -- callforplayer is how much it has to pay to call. both numbers are also arbitrary ones that i chose because i thought would work well
			    the reason for the '50 -' is for example: callforplayer is 150 , then callforplayer/10 would be 15, and then 50-15 = 35. so because 150 is a relatively small bet, 35 is added to the probability
			    my idea also works with extremly large bets, like when callforplayer = 600. the result would be 50-600/10 = -10, so 10 is subtracted to the probability, which is fitting

    num*10                   -- num is returned from fastcardscheck(), which gives the players current hand value , e.g 2 if player has a pair so 20 is added to the probability

    playerbluffrate*100      -- this is the variable that is how the bots adapt to how the player plays
   
    heres how its calculated at the end of each round:
    -
          if fastcardscheck(1) < playercalls[0] / 200:
            timesbluffed += 1
            playerbluffrate = round(timesbluffed / roundsplayed, 2) 
    -

    (playercalls[0] is how much the singleplayer has bet)
    so if the player bets a disproportionate amount of money (e.g. 600 hundred when the player only has a pair) , and the player has played three rounds before, playerbluffrate is calculated to 0.33 
    this means that when player raises in the next round, 0.33*100 = 33 will be added to the bots call probability. this is how the bot adapts to how the player plays, and becomes more likely to call out a bluff from a player who bluffs very often	

my father was happy to play-test it (singleplayer mode) and he hasnt come across any bugs so far in the final version

hopefully this text file is enough to explain the thought process behind my code 


				
	

    
    
    

        
        
            
            
            
            

        
            
            
            
        
        
            
            

        
    
    
    
    






