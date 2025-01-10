import art
import os
bid_dic = {}
bid_condition = True
highest_value = 0
bid_winner = ''
print(art.logo_auction) 
print(art.logo_gavel)
while bid_condition:
    name_key = input("Enter the name of the bidder.\n")
    bid_value = int(input("Enter the bid value in $\n"))
    bid_dic[name_key] = bid_value
    print('\n'*100)
    condition_check = input("Enter 'Yes' if you want to continue bidding else enter 'No'\n").lower()
    if condition_check != 'yes':
        bid_condition = False


for key in bid_dic:
    if highest_value < bid_dic[key]:
        highest_value = bid_dic[key]
        bid_winner = key

print(f"Winner is {bid_winner} with bid amount {highest_value}.")
os.system("pause")