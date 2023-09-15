
def Hit():
  while True:
    try:
      Hit = input("\rHit or stick? (H) or (S): ")
    except ValueError:
      print("Make sure you only type H or S ")
      continue
    if Hit.lower() == "h" or Hit.lower() == "s":
      break
    else:
      print("please only type H or S ")
      continue
  
  return Hit.lower()


def HandCalc(Hand):

  # variable to stop the loop exceeding the list length
  Loop = 0
  # variable for the total value of the hand
  HandTotal = 0

  AceTotal = 0

  #Loop that keeps going aslong as there are items in the list
  while Loop < len(Hand):

    #Try function so it can differ from integer and string
    try:
      HandTotal = HandTotal + int((Hand[Loop])[1])

      #If the number is 10 then this line of code deals with that and adds the apropriate value
      if int((Hand[Loop])[1]) == 1:
        if len(Hand[Loop]) == 3:
          HandTotal = HandTotal + 9
      
    #Deals with the letters within the deck and gives them value
    except ValueError:
      if ((Hand[Loop])[1]) == "A":
        HandTotal = HandTotal + 11
        AceTotal = AceTotal + 1

      if ((Hand[Loop])[1]) == "J":
        HandTotal = HandTotal + 10

      if ((Hand[Loop])[1]) == "Q":
        HandTotal = HandTotal + 10

      if ((Hand[Loop])[1]) == "K":
        HandTotal = HandTotal + 10

    Loop = Loop + 1


  while AceTotal > 0 and HandTotal > 21:
    HandTotal = HandTotal - 10
    AceTotal = AceTotal - 1

    
  return(HandTotal)