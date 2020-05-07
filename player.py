import random

def action(money, raised):
    if raised:
        return 'CALL'
    action = random.randint(1,3)
    if action == 1:
        return check()
    elif action == 2:
        return fold()
    elif action == 3:
        return raiseBet(random.randint(money))

def check():
    return 'CHECK'

def fold():
    return 'FOLD'

def raiseBet(amount):
    