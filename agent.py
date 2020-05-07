def startingHand(agent):
  # Agent determines the value of the hand, based on Only the two cards in hand for now
    handValue = 0
    card1 = agent.cards[0][0]
    card2 = agent.cards[1][0]

  # Determine hand value - take values of hand and total up what you have.
  # Basing information on https://www.cardschat.com/poker-starting-hands.php , with no regards to suits currently

    cardRevalue = {'A' : 0, '2' : 12, '3' : 11, '4' : 10, '5' : 9, '6' : 8, '7' : 7, '8' : 6, '9' : 5, '10' : 4, 'J' : 3, 'Q' : 2, 'K' : 1}
    
    print(card1, card2)
        
  # Values in A, K, Q, J, 10, 9, ect order. Reorderer above makes it so the right combinations will be picked
    values = ( [85, 68, 67, 66, 66, 64, 63, 63, 62, 62, 61, 60, 59], [66, 83, 64, 64, 63, 61, 60, 59, 58, 58, 57, 56, 55],
               [65, 62, 80, 61, 61, 59, 58, 56, 55, 55, 54, 53, 52], [65, 62, 59, 78, 59, 57, 56, 54, 53, 52, 51, 50, 50],
               [64, 61, 59, 57, 75, 56, 54, 53, 51, 49, 49, 48, 47], [62, 59, 57, 55, 53, 72, 53, 51, 50, 48, 46, 46, 45],
               [61, 58, 55, 53, 52, 50, 69, 50, 49, 47, 45, 43, 43], [60, 57, 54, 52, 50, 48, 47, 67, 48, 46, 45, 43, 41],
               [59, 56, 53, 50, 48, 47, 46, 45, 64, 46, 44, 42, 40], [60, 55, 52, 49, 47, 45, 44, 43, 43, 61, 44, 43, 41],
               [59, 54, 51, 48, 46, 43, 42, 41, 41, 41, 58, 42, 40], [58, 54, 50, 48, 45, 43, 40, 39, 39, 39, 38, 55, 39],
               [57, 53, 49, 47, 44, 42, 40, 37, 37, 37, 36, 35, 51] )
    
  # Depending on value found choose what to do and what to return.
    val1 = cardRevalue[card1]
    val2 = cardRevalue[card2]
    handValue = values[val1][val2]

  # Choose to raise return 1
    if handValue >= 60:
        return 1

  # Choose to call  return 2
    if handValue >= 40 and handValue < 60:
        return 2

  # Choose to fold  return 3
    if handValue < 40:
        return 3
  
  # nothing should return here
    return 0