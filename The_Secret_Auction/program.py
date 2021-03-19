import art
print(art.logo)

bits = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bit = 0
    winner = ""
    for i in bidding_record:
        bid_amount = bidding_record[i]
        if bid_amount > highest_bit:
            highest_bit = bid_amount
            winner = i
    print(f"The winner is {i} with the bit of ${highest_bit}")

while not bidding_finished:
    name = input("What is your name ? ")
    price = int(input("What is your bit ? $"))
    bits[name] = price
    x = input("Are there any other bidders? Type 'Yes' or 'No'. \n").lower()
    if x == "no":
        bidding_finished = True
        find_highest_bidder(bits)