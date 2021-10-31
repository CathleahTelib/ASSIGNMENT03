def askName():
    name = input("What is your name?:")
    return name

def askAge():
    age = int(input("How old are you?:"))
    return age

def askAddress():
    address = input("Where do you live?:")
    return address

def personalDetails():
   print("Hi, my name is {}. I am {} years old and I live in {}.".format(nameQ, ageQ, addressQ))

   


#steps
# 1. ask for name 
nameQ = askName()
# 2. ask for age 
ageQ = askAge()
# 3. ask for address 
addressQ = askAddress()
# 4. display output in the ff. format: Hi, my name is _______. I am ______ years old and I live in _______ .
outputQ = personalDetails()