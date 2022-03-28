
# Name : Zachary Hopps 
# this is the beginning of my integration project
# this project is going to act as a Magic Eden NFT sniping bot
# ME (short for Magic Eden) is the largest, most popular NFT marketplace for
# NFTs on the Solana blockchain
# the purpose of a sniping bot is to quickly purchase NFTs listed far below the
# general floor price, on purpose or by accident, and allow the user of the bot
# to only buy into a project when they get the deal that they want, and is
# useful to potentially make someone a lot of money daytrading using a bot like this
# this bot will double as its own NFT, and the rights of using it will be sold and traded
# on magic eden one day after finalization
def main():
    
    print("LOADING........ \n")

#loading screen to satisfy requirements

    print(1 ** 2)   
    print(int(10 / 5))
    print(1 + 2)
    print(4 % 100 )
    print(35 // 6)
    print(3 * 2)
    print(10 - 3)

    print("Welcome to TH NFT BOT --- " * 3)

    print("HURRY!\n")

    print("Select a Sol Wallet to Connect")

    One = "Phantom"
    Two = "MetaMask"
    Three = "SolFlare"
    Four = "Sollet"
    Five = "Ledger"

    print("One - Phantom")
    print("Two - MetaMask")
    print("Three - SolFlare")
    print("Four - Sollet")
    print("Five - Ledger Wallet\n")

    a = input("Enter Solana Wallet Type (example, One = Phantom Wallet): ")
    if One:
        input("Phantom Wallet Password: ")
    elif Two:
        input("MetaMask Wallet Password: ")
    elif Three:
        input("SolFlare Wallet Password: ")
    elif Four:
        input("Sollet Wallet Password: ")
    elif Five:
        input("Ledger Password: ")
    else:
        print("Invalid input, try again")
    
# this will let the bot know which wallet to prompt the user to authenticate and connect
# so that there is money to use to buy the NFTs with.

    print("WALLET CONNECTED...LOADING")

    while a == a:
        print("Phantom Wallets are the most widely accepted of all cryptocurrency wallets,\n consider switching to one!")
        break

#entering the max price of the NFT item for the bot to purchase  (usually far under floor price)

    max_price = (int(input("Enter Max Value to Purchase Here (must be a whole number) : ")))
    if max_price > 100.00:
        print("WHALE ALERT!!!")
    else:
        print("Time to Sweep!\n")

    for i in range(max_price):
        if not max_price % 1 == 0:
            print("Okay! not very specific\n")
        else:
            print("Okay!! Lets snipe!\n")

    if not max_price > 1 and max_price > 0:
        print("Might have to stick to your day job but okay..\n")

    if max_price == 0 or max_price == 10000:
        print("???")
    else:
        print("Okay, now the important part\n")
            
    NFT_Collection = input("Enter NFT Collection Name Here: ")
    Collection_URL = input("Enter Collection Magic Eden URL: ")

    if Collection_URL != "www.MagicEden.io/":
        print("Error Invalid Website")
    else:
        print("CONNECTED\n")
        
#this is so that the bot can monitor the data on the website and see when a item is listed
#lower than the price input above.

main()
#this is the call to the program
#many people only use bots like these to be quick to buy NFTs when people mistakingly list them for lower than
#they should have, and therefore make money on them.




