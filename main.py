import art
import os

bid_dic = {}
bid_condition = True

print(art.logo_auction) 
print(art.logo_gavel)

def highest_bidder(bid_dictionary):
    highest_value = 0
    for key in bid_dictionary:
        if highest_value < bid_dic[key]:
            highest_value = bid_dic[key]
    return key,highest_value
    
    

while bid_condition:
    name_key = input("Enter the name of the bidder.\n")
    bid_value = int(input("Enter the bid value in $\n"))
    bid_dic[name_key] = bid_value
    bid_winner,winner_value = highest_bidder(bid_dic)
    print('\n'*100)
    condition_check = input("Enter 'Yes' if you want to continue bidding else enter 'No'\n").lower()
    
    if condition_check != 'yes':
        bid_condition = False

print(f"Winner is {bid_winner} with bid amount {winner_value}.")
os.system("pause")