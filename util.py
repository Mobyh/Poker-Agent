from os import system, name 

#Player class to hold players attributes
class Player:
  def __init__(self, name, money):
    self.name = name
    self.money = money
    self.cards = ["", ""]

# Variables
yes = ['Yes', 'yes', 'YES', 'Si'] #the more we add, the more out dealer will "understand"
fold = ['fold', 'FOLD', 'Fold']
call = ['call', 'CALL', 'Call']
check = ['check', 'CHECK', 'Check']
bet = ['raise', 'RAISE', 'Raise']

# Creates a deck of cards
def createDeck():
  deck = [[0 for x in range(13)] for y in range(4)]
  #Ace
  deck[0][0] = 'A' + ' S '
  deck[1][0] = 'A' + ' C '
  deck[2][0] = 'A' + ' H '
  deck[3][0] = 'A' + ' D '
  #2-9
  for x in range(1,9):
    deck[0][x] = str(x+1) + ' S '
    deck[1][x] = str(x+1) + ' C '
    deck[2][x] = str(x+1) + ' H '
    deck[3][x] = str(x+1) + ' D '
  #10 done separately for formatting purposes  
  deck[0][9] = '10' + ' S'  
  deck[1][9] = '10' + ' C' 
  deck[2][9] = '10' + ' H'  
  deck[3][9] = '10' + ' D' 
 
  #KJQ
  deck[0][10] = 'J' + ' S '
  deck[0][11] = 'Q' + ' S '
  deck[0][12] = 'K' + ' S '
  deck[1][10] = 'J' + ' C '
  deck[1][11] = 'Q' + ' C '
  deck[1][12] = 'K' + ' C '
  deck[2][10] = 'J' + ' H '
  deck[2][11] = 'Q' + ' H '
  deck[2][12] = 'K' + ' H '
  deck[3][10] = 'J' + ' D '
  deck[3][11] = 'Q' + ' D '
  deck[3][12] = 'K' + ' D '
  #Returns new deck
  return deck

# Clears the screen 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

# This will print out the main menu
def printMenu():
  print("*************************************************************************************")
  print("*                                                                                   *")
  print("*    Welcome! Have a sit while we wait for Agent. Here's some useful information:   *")
  print("*     - The game is Texas Hold'em.                                                  *")
  print("*     - You will play against our poker playing agent.                              *")
  print("*     - You will see --> when you need to type an answer.                           *")
  print("*     - Please do not type unless prompted to do so. :)                             *")  
  print("*     - When prompted to, use simple words such as:                                 *")
  print('*        - "Check"                                                                  *')
  print('*        - "Raise"                                                                  *')
  print('*        - "Fold"                                                                   *')
  print('*        - "Yes"                                                                    *')
  print('*        - "No"                                                                     *')
  print("*     - If the dealer fails to understand you, hints will be prompted.              *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                    Good luck!!                                    *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                        Are you ready to play? (Enter 'yes')                       *")
  print("*                                                                                   *") 
  print("*************************************************************************************")  

#This will print input hints
def printInputHint():
  print("*************************************************************************************")
  print("*                                                                                   *")
  print("*                                   USEFUL HINTS                                    *")
  print("*     - You will see --> when you need to type an answer.                           *")
  print("*     - Please do not type unless prompted to do so. :)                             *")
  print("*     - When prompted to, use simple words such as:                                 *")
  print('*        - "Check"                                                                  *')
  print('*        - "Raise"                                                                  *')
  print('*        - "Raise"                                                                  *')
  print('*        - "Demo"                                                                   *')
  print('*        - "Fold"                                                                   *')
  print('*        - "Yes"                                                                    *')
  print('*        - "No"                                                                     *')
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                        This window will close automatically...                    *")
  print("*                                                                                   *")
  print("*************************************************************************************")

#This will print new 'Starting new hand' window
def printStartingNewHand():
  print("*************************************************************************************")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                STARTING NEW HAND!                                 *") 
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")  
  print("*                        This window will close automatically...                    *") 
  print("*                                                                                   *")
  print("*************************************************************************************")

#This will print the 'Wanna play again?' window
def printPlayAgain():
  print("*************************************************************************************")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                               Play another hand??                                 *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*************************************************************************************")

#This will print the dealer dealing cards screen
def printDealingCards():
  print("*************************************************************************************")
  print("*                                                                                   *")
  print("*                                 Dealing Cards...                                  *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*    Your Cards:                                                 Agents Cards:      *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*************************************************************************************")

#This will print the dealer dealing the cards once dealt
def printDealtCards(human, agent, pot):
  print("*************************************************************************************")
  print("*                                                                                   *")
  print("*                                 Make Your Bets                                    *")
  print("*                    |   Check   |  Raise |  Call  |  Fold  |                       *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *") 
  print("*    Your Cards:                                                Agents Cards:       *")
  print("*   _____   _____                                               _____   _____       *")
  print("*  |     | |     |                                             |     | |     |      *")
  print('*  | {}| | {}|                                             | X X | | X X |      *'.format(human.cards[0], human.cards[1]))
  print("*  |     | |     |                                             |     | |     |      *")
  print("*  |_____| |_____|                                             |_____| |_____|      *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*************************************************************************************")
  print("            Your Balance: ${}                        Agent's Balance: ${}             ".format(human.money, agent.money)) 
  print('                                Current Pot:  ${}'.format(pot))

#will print winner screen
def printWinner(human, agent, pot, winner):
  print("*************************************************************************************")
  print("*                                                                                   *")
  print("*                                 Make Your Bets                                    *")
  print("*                    |   Check   |  Raise |  Call  |  Fold  |                       *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  if winner == 'Agent':
    print("*                            {} wins this hand!                                  *".format(winner))
  else: 
    print("*                            {} wins this hand!                                    *".format(winner))
  print("*                                                                                   *")
  print("*    Your Cards:                                                Agents Cards:       *")
  print("*   _____   _____                                               _____   _____       *")
  print("*  |     | |     |                                             |     | |     |      *")
  print('*  | {}| | {}|                                             | X X | | X X |      *'.format(human.cards[0], human.cards[1]))
  print("*  |     | |     |                                             |     | |     |      *")
  print("*  |_____| |_____|                                             |_____| |_____|      *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*************************************************************************************")
  print("            Your Balance: ${}                        Agent's Balance: ${}             ".format(human.money, agent.money))
  print("                                    Pot: ${}".format(pot)) 

#will show the new dealth cards (3)
def printThreeCards(human, agent, pot, comCards):
  print("*************************************************************************************") 
  print("*                                                                                   *")
  print("*                                 Make Your Bets                                    *")
  print("*                    |   Check   |  Raise |  Call  |  Fold  |                       *")
  print("*                                                                                   *")
  print("*                   _____    _____    _____                                         *")
  print("*                  |     |  |     |  |     |                                        *")
  print('*                  | {}|  | {}|  | {}|                                        *'.format(comCards[0], comCards[1], comCards[2]))
  print("*                  |     |  |     |  |     |                                        *")
  print("*                  |_____|  |_____|  |_____|                                        *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*    Your Cards:                                                Agents Cards:       *")
  print("*   _____   _____                                               _____   _____       *")
  print("*  |     | |     |                                             |     | |     |      *")
  print('*  | {}| | {}|                                             | X X | | X X |      *'.format(human.cards[0], human.cards[1]))
  print("*  |     | |     |                                             |     | |     |      *")
  print("*  |_____| |_____|                                             |_____| |_____|      *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*                                                                                   *")
  print("*************************************************************************************")
  print("            Your Balance: ${}                        Agent's Balance: ${}             ".format(human.money, agent.money))
  print("                                    Pot: ${}".format(pot))
  
