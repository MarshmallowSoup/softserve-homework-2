import random

day = 0

videocard = {
    'rtx1080': [30000, 1],
    'rtx2080': [45000, 2]
}


users_videocard = {}

def goods():
    btc = random.randint(300, 3000)
    price = str(btc)
    return price


def start():
    print("Bitcoin costs " + prce + " dollars")
    print("You have " + str(money) + " dollars")
    print('You have {0} btc'.format(quantity))


def ask_buying():
    buy = input("Will you buy some?(y/n) ")
    if buy != "y":
        print("Bye")
        return False
    else:
        qty = input("Choose quantity ")
        return int(qty)


def buying():
    global quantity
    if quantity == False:
        quantity = 0
    print("You have " + str(balance) + " dollars")
    print("You have " + str(quantity) + " BTC")


def money_b():
    global quantity
    money_af = money - int(quantity) * int(prce)
    return money_af


def trade():
    global balance
    global quantity
    print("You have " + str(quantity) + " BTC")
    bs = input('Wanna buy or sell?(b/s)')
    if bs == 'b':
        qty = int(input("Choose quantity "))
        balance = money - int(qty) * int(prce)
        quantity = quantity + qty
        print("You have " + str(balance) + " dollars")
        print("You have " + str(quantity) + " BTC" + "\n")
        return balance
    elif bs == 's':
        qty = input("Choose quantity ")
        quanty = int(qty)
        if quanty<=quantity:
            balance = money + int(quantity) * int(prce)
            quantity = quantity - quanty
            print("You have " + str(balance) + " dollars")
            print("You have " + str(quantity) + " BTC")
            return balance
        else:
            print('Not enough')
            print("Bye")
            return
    else:
        print("Bye")
        return

    

def shop():
    print('Welcome to shop, here you can buy a videocard')
    for name, value in videocard.items():
        print('Videocard {0} costs {1} dollars and produces {2} btc per day'.format(name, value[0], value[1]))
    print('Which one do you want to buy?')
    global choice
    global balance
    choice = input('(input here full name) ')
    for name, value in videocard.items():
        if name == choice:
            print('Videocard {0} will be cost {1} bucks'.format(name, value[0]))
            balance = money - value[0]
            print('You have {0} dollars'.format(balance))
            global users_videocard
            users_videocard[choice] = videocard[choice]
            return balance
        else:
            print('choose something else')

    

def game():
    global money
    choice = input('Wanna trade(t) or buy a videocard(s)? (t/s)')
    if choice == 't':
        trade()
    elif choice == 's':
       shop() 
       money = balance
       
def checker():
    global quantity
    for name, value in users_videocard.items():
        quantity = quantity + value[1] 
        return quantity


        



while True:
    quantity = 0
    money = 10000
    prce = goods()
    start()

    quantity = ask_buying()
    
    balance = money_b()
    buying()
    money = balance

    while money >= 0:
        day += 1
        print('Day ' + str(day))
        prce = goods()
        money = balance
        start()
        game()
        checker()
        money = balance
    else:
        print("You lose" + "\n")
