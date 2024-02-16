from replit import clear
#HINT: You can call clear() to clear the output in the console.

import art

#Print logo
print (art.logo)
#Print welcome line
print ("Welcome to the silent auction program")

#Create empty dictionary
bids = {}
#Create boolean to be used in while loop
bidding_finished = False

#define the function for the highest bidder
def find_highest_bidder(bidding_record):
  #set the highest bid to 0 
  highest_bid = 0
  #set the winner to an empty string
  winner = ""
  #for evey bidder in the list of bidders
  for bidder in bidding_record:
    #make their amount = to the name of the bidder
    bid_amount = bidding_record[bidder]
    #if the bid amount is higher than the current highest bid, then reassign to make highest bid = this value
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      #the winner is = to the bidder of the highest bid
      winner = bidder
      #print the winning statement
  print (f"The winner is {winner} with a bid of ${highest_bid}")
      

#While bidding_finished is not = to True

while not bidding_finished: 
  #ask for name and bid
  name = input("What is your name? ")
  price = int(input("What is your bid? "))
  #record the name and price in the bids dictionary
  bids[name] = price
  #see if more bidders need to input their information
  should_continue = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
  #if no, then change boolean value and carry out the find_highest_bidder function
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    #else clear the screen and ask the questions again
    clear()