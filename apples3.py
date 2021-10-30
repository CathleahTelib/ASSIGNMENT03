def ask_quantity_of_apple():
    applesQuantity = int(input("How many apples you want to buy?: "))
    return applesQuantity

def ask_quantity_of_orange():
    orangeQuantity =int(input("How many oranges you want to buy?: "))
    return orangeQuantity

def compute_total_amount():
    apples = 20
    oranges = 25
    applesAmount = apples * applesQ
    orangeAmount = oranges * orangesQ
    amount= applesAmount + orangeAmount
    print(f"The total amount is {amount}.")
    return amount

#steps

# 1. ask for apples you want to buy and save to variable
applesQ = ask_quantity_of_apple()
# 2. ask for oranges you want to buy and save to variable
orangesQ = ask_quantity_of_orange()
# 3. display prices of apple and orange
print("The price of apples is 20 php")
apples = 20
print("The price of oranges is 25 php")
oranges = 25
# 4. display the total amount in the ff. format : The total amount is ________.
amount = compute_total_amount()