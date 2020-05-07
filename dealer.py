import random

#Deals initial 2 cards to the players
def deal(human, agent, deck):
  symbols = [0, 1, 2, 3]
  card = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  #Deal first card
  v1 = random.choice(symbols)
  v2 = random.choice(card)
  human.cards[0] = deck[v1][v2]
  deck[v1][v2] = '-'
  #Deal second card, avoid dealing an already dealt card
  while True:
    v1 = random.choice(symbols) 
    v2 = random.choice(card) 
    if deck[v1][v2] != '-':
      human.cards[1] = deck[v1][v2]
      break
  #Deals agents cards with the same logic
  while True:
    v1 = random.choice(symbols)
    v2 = random.choice(card)
    if deck[v1][v2] != '-':
      agent.cards[0] = deck[v1][v2]
      break
  while True:
    v1 = random.choice(symbols)
    v22 = random.choice(card)
    if deck[v1][v2] != '-':
      agent.cards[1] = deck[v1][v2]
      break

def dealThreeCards(comCards, deck):
  #placeholder, this needs to actually deal from the deck
  comCards[0] = '7 S '
  comCards[1] = 'A S '
  comCards[2] = '2 H '
  
  
