resources = {"Water":600,"Milk":650,"Coffee":700,"Money":3.5}

espresso = {"Water":120,"Milk":120,"Coffee":60,"Money":1.09}
latte = {"Water":100,"Milk":50,"Coffee":76,"Money":5.32}
cappuccino = {"Water":150,"Milk":100,"Coffee":67,"Money":10.46}

def report():
    print("Water: {0}ml\nMilk: {1}ml\nCoffee: {2}g\nMoney: {3}$\n".format(resources["Water"],resources["Milk"],resources["Coffee"],resources["Money"]))
    return
          
def resources_suffient(drinks):
    if drinks == "espresso":
        for i in resources:
            if resources[i] < espresso[i]:
                if i == "Money":
                    continue
                print("Sorry there is not enough {}.".format(i))
                menu()
                break
        insert_coins(drinks)
        
    elif drinks == "latte":
        for i in resources:
            if resources[i] < latte[i]:
                if i == "Money":
                    continue
                print("Sorry there is not enough {}.".format(i))
                menu()
                break       
        insert_coins(drinks)
    elif drinks == "cappuccino":
        for i in resources:
            if resources[i] < cappuccino[i]:
                if i == "Money":
                    continue
                print("Sorry there is not enough {}.".format(i))
                menu()   
                break
        insert_coins(drinks)
    
    return

def insert_coins(drinks):
    print("Please insert coins")
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total_coins = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    
    if drinks == "espresso":
        if total_coins > espresso["Money"]:
            diff = total_coins - espresso['Money']
            print("Here is your $%.2f" % diff,"in change")
            print("Here is your Espresso.Enjoy!")
            water_diff = resources["Water"] - espresso["Water"]
            milk_diff = resources["Milk"] - espresso["Milk"]
            coffee_diff = resources["Coffee"] - espresso["Coffee"]
            money_diff = resources["Money"] + espresso["Money"]
            resources["Water"] = water_diff
            resources["Milk"] = milk_diff
            resources["Coffee"] = coffee_diff
            resources["Money"] = money_diff
        else:
            print("Sorry that's not enough money. Money Refunded.")
    elif drinks == "latte":
        if total_coins > latte["Money"]:
            diff = total_coins - latte['Money']
            print("Here is your $%.2f" % diff,"in change")
            print("Here is your Latte.Enjoy!")
            water_diff = resources["Water"] - latte["Water"]
            milk_diff = resources["Milk"] - latte["Milk"]
            coffee_diff = resources["Coffee"] - latte["Coffee"]
            money_diff = resources["Money"] + latte["Money"]
            resources["Water"] = water_diff
            resources["Milk"] = milk_diff
            resources["Coffee"] = coffee_diff
            resources["Money"] = money_diff
        else:
            print("Sorry that's not enough money. Money Refunded.")
            
    else:
        if total_coins > cappuccino["Money"]:
            diff = total_coins - cappuccino['Money']
            print("Here is your $%.2f" % diff,"in change")
            print("Here is your Cappuccino.Enjoy!")
            water_diff = resources["Water"] - cappuccino["Water"]
            milk_diff = resources["Milk"] - cappuccino["Milk"]
            coffee_diff = resources["Coffee"] - cappuccino["Coffee"]
            money_diff = resources["Money"] + cappuccino["Money"]
            resources["Water"] = water_diff
            resources["Milk"] = milk_diff
            resources["Coffee"] = coffee_diff
            resources["Money"] = money_diff
        else:
            print("Sorry that's not enough money. Money Refunded.")
    
    return

def menu():
    while True:
        answer = input("What would you like? (espresso/latte/cappuccino):")
        if answer == "report":
            report()
        elif answer == "espresso":
            resources_suffient(answer)     
        elif answer == "latte":
            resources_suffient(answer)   
        elif answer == "cappuccino":
            resources_suffient(answer)   
        elif answer == "off":
            break
        else:
            print("Please enter correct choice")

menu()
