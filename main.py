
#Imports random
import random, Blackfunctions, time 

#Sets the card deck
CardDeck = ["♥A","♥2","♥3","♥4","♥5","♥6","♥7","♥8","♥9","♥10","♥J","♥Q","♥K","♦A","♦2","♦3","♦4","♦5","♦6","♦7","♦8","♦9","♦10","♦J","♦Q","♦K","♠A","♠2","♠3","♠4","♠5","♠6","♠7","♠8","♠9","♠10","♠J","♠Q","♠K","♣A","♣2","♣3","♣4","♣5","♣6","♣7","♣8","♣9","♣10","♣J","♣Q","♣K"]

#Sets up the hands
DealerHand = []
YourHand = []

MaxRandomNumber = 51

#deals the First card
RandomListNumber = random.randint(0,MaxRandomNumber)
MaxRandomNumber = MaxRandomNumber - 1
YourHand.append(CardDeck[RandomListNumber])
del CardDeck[RandomListNumber]

#Dealers first card
RandomListNumber = random.randint(0,MaxRandomNumber)
MaxRandomNumber = MaxRandomNumber - 1
DealerHand.append(CardDeck[RandomListNumber])
del CardDeck[RandomListNumber]

#deals the second card
RandomListNumber = random.randint(0,MaxRandomNumber)
MaxRandomNumber = MaxRandomNumber - 1
YourHand.append(CardDeck[RandomListNumber])
del CardDeck[RandomListNumber]

#Dealers second card
RandomListNumber = random.randint(0,MaxRandomNumber)
MaxRandomNumber = MaxRandomNumber - 1
DealerHand.append(CardDeck[RandomListNumber])
del CardDeck[RandomListNumber]

#prints your hand to show what it is before you hit or stick
HandTotal = Blackfunctions.HandCalc(YourHand)
print("Your Hand is: ",YourHand, HandTotal)
print("Dealers hand is: [ XX," ,DealerHand[1],"]")
#Runs a loop that deals with the dealing
while True:
  time.sleep(0.5)
  Hit = Blackfunctions.Hit()
  if Hit == "h":
    RandomListNumber = random.randint(0,MaxRandomNumber)
    MaxRandomNumber = MaxRandomNumber - 1
    YourHand.append(CardDeck[RandomListNumber])
    del CardDeck[RandomListNumber]
    HandTotal = Blackfunctions.HandCalc(YourHand)
    print("Your Hand is: ",YourHand, HandTotal)
    if HandTotal > 21:
      GameResult = "You have lost, You went bust"
      break
    continue
  else:
    break

#Dealers hand calculation
DHandTotal = Blackfunctions.HandCalc(DealerHand)
print("Dealers hand is: ",DealerHand,DHandTotal)
while HandTotal < 22 and DHandTotal < 16:
  time.sleep(0.5)
  RandomListNumber = random.randint(0,MaxRandomNumber)
  MaxRandomNumber = MaxRandomNumber - 1
  DealerHand.append(CardDeck[RandomListNumber])
  DHandTotal = Blackfunctions.HandCalc(DealerHand) 
  print("Dealers hand is: ",DealerHand,DHandTotal)
  if DHandTotal > 21:
    GameResult = "You have won, Dealer went bust"
  if DHandTotal == HandTotal:
    GameResult = "You have lost, You went even agianst the dealer"

#Prints hands
time.sleep(0.5)
print("\n\n")
print("Your Hand is: ",YourHand, HandTotal)
print("Dealers hand is: ",DealerHand,DHandTotal)
time.sleep(0.5)

#Compares the two hands
if DHandTotal < 22 and HandTotal < 22:
  if DHandTotal > HandTotal:
    GameResult = "You have lost, Dealers hand is worth more"
  else:
    GameResult = "You have won, Your hand is worth more"

#Prints the game result
print(GameResult)