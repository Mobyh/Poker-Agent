"""
Poker Playing Agent
By: Team 18, I think.

"""
import agentScript
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

#Raised player flag
raised = False

#Will display menu and ask player if ready to play
#Will not move forward until the player answers 'yes'
#Will display hint menu if answer != yes (or variant) 
while (True):
  #Shows main menu, gets answer to "Ready to play" from user
  util.printMenu()
  answer = input("--> ")

  #If player answers 'demo' then the automated player is activated
  if answer == 'demo' or answer == 'Demo':
    automated = True
    break


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
  playerCheck = False
  playerBet = False

  agentFolded = False
  agentCheck = False
  agentBet = False
 
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
    answer = player.action(human.money,raised)
    print(">>> " + str(answer))
    sleep(3)
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
  agent_action = agentScript.startingHand(agent)

  #Agent is raising
  if agent_action == 1:
    agentBet = True

  #Agent is calling
  if agent_action == 2:
    agentCheck = True

  #Agent is folding
  if agent_action == 3:
    agentFolded = True

  
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
  elif playerCheck == True or agentCheck == True:      
      #Both checked, we deal community cards
      util.clear()
      dealer.dealThreeCards(comCards, deck)
      util.printThreeCards(human, agent, pot, comCards)
      if(automated):
        nothing = player.action(human.money,raised)
        print(">>> " + str(answer))
        sleep(3)
      else:
        #Prompt the user to make a move
        nothing = input(">>> ")
  
  
  #Game has ended, ask if payer wants to play another hand
  util.clear()
  util.printPlayAgain()
  if(automated):
    answer = player.action(human.money,raised)
    print(">>> " + str(answer))
    sleep(3)
  else:
    #Prompt the user to make a move
    answer = input(">>> ")
  
  #If they dont want to play another hand, display stats
  if answer == 'no':
    break 

