"""
Poker Playing Agent
By: Team 18, I think.

"""
import agent
import player
import dealer
import util
from time import sleep

#Test

#Clear user screen, we want their full attention
util.clear()

#Will be used to break loop in case of infinite loop
safetyCount = 0

#Automated player flag
automated = False

#Will display menu and ask player if ready to play
#Will not move forward until the player answers 'yes'
#Will display hint menu if answer != yes (or variant) 
while (True):
  #Shows main menu, gets answer to "Ready to play" from user
  util.printMenu()
  answer = input("--> ")

  #If player answers 'demo' then the automated player is activated
  if answer == 'demo':
    automated = True


  #If player answers 'yes' (or variant)
  if answer in util.yes:
    break
 
  #Otherwise we print hint menu, and then main menu again
  util.clear()
  util.printInputHint()
  sleep(5)
  util.clear() 
 
  #Will break loop in case of infinite loop
  safetyCount += 1
  if safetyCount > 50:
    print("Error: Possible infinite loop?")
    break
  
#Ceate players, everyone starts with $100
agent = util.Player("agent", 100)
human = util.Player("human", 100)
pot = 0
  
#This loop represents one entire playing hand
while(True):
  #Shows starting new hand screen
  util.clear()
  util.printStartingNewHand()
  sleep(2)
  
  #Game starts
  util.clear()
  comCards = ["", "", "", "", ""]
  playerFolded = False
  agentFolded = False
 
  #Create fresh deck for this hand
  deck = util.createDeck()
  
  #Initial bets
  pot = 10
  human.money -= 5 
  agent.money -= 5

  #Deal intitial two cards, display only players cards
  util.printDealingCards()
  sleep(1)
  util.clear()
  dealer.deal(human, agent, deck)
  util.printDealtCards(human, agent, pot)
  
  if(automated):
    answer = player.action(human.money)
  else:
    #Prompt the user to make a move
    answer = input(">>> ")
    
  #Players decission  //This may need to be within a while loop 
  if answer in util.fold:
    playerFolded = True
  elif answer in util.check:
    playerCheck = True
  elif answer in util.call:
    playerCheck = True
  elif answer in util.bet:
    playerBet = True
  else:
   print("Unidentified val, prompt hints screen, display dealtCards screen.")

  #Agent decission
  #Need to call agent card analysis here
  ######################################
  
  #I folded, means agent wins 
  if playerFolded == True:
    winner = "Agent"
    agent.money = agent.money + pot
    util.clear()
    util.printWinner(human, agent, pot, winner)
    sleep(3)

  #Agent folded, means I win
  elif agentFolded == True:
    winner = "Player"
    player.money = player.money + pot
    util.clear()
    util.printWinner(human, agent, pot, winner)
    sleep(3)
 
  #If neither player folded, game continues
  else:
    if (playerCheck == True): #We need to add agent's check here too 
      
      #Both checked, we deal community cards
      util.clear()
      dealer.dealThreeCards(comCards, deck)
      util.printThreeCards(human, agent, pot, comCards)
      nothing = input("TEST: ")
  
  
  #Game has ended, ask if payer wants to play another hand
  util.clear()
  util.printPlayAgain()
  answer = input("--> ")
  
  #If they dont want to play another hand, display stats
  if answer == 'no':
    break 

