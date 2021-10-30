def amount_of_money():
    moneyQuantity = int(input("Enter amount of money you have:"))
    return moneyQuantity

def price_of_apple():
    applePrice = float(input("Price of apple:"))
    return applePrice

def display_apple_quantity_and_money_change():
    canPurchase = moneyQ // appleP
    moneyChange = moneyQ % appleP
    print(f"You can buy {canPurchase} apples and your change is {moneyChange:.2f} pesos.") 

# steps
# 1. ask money that you have and save to variable
moneyQ = amount_of_money()
# 2. ask for the price of apple
appleP = price_of_apple() 
# 3. Display the amount of apples that you can buy and amount of your change in the ff. format: You can buy _____ apples and your change is _____ pesos.
displayOutput = display_apple_quantity_and_money_change()