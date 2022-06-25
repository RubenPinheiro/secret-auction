import clearConsole
import auction_art

print(auction_art.logo)

#name = input('What is your name? ' )
#bid = int(input('What is your bid? €'))

should_continue = True
offers = {}
#offers[name] = bid

def highest_bidder(offers):
    winner_bid = 0
    for name in offers:
        if offers[name] >= winner_bid:
            winner_bid = offers[name]
            winner_name = name
    print(f'The winner is {winner_name} with the highest bid of {winner_bid}€')

while should_continue == True:
    #LEARN PYCHARM
    clearConsole.clearConsole()
    name = input('What is your name? ' )
    bid = int(input('What is your bid? €'))

    offers[name] = bid
    others = input('Are there any other bidders? Type "yes" or "no"\n')
    
    if others == 'no':
        should_continue = False
        highest_bidder(offers)