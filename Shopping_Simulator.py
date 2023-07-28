# Description: This program will run the user through a store in which they are able to add or delete items to a cart, view the items in the cart,
#              and proceed to checkout. The user may pay with card or cash. If they pay with card, a receipt of the purchase will be displayed. 
#              If they pay with cash, it will count the denominations that are due to the customer and then display a receipt for their order.

# Function that will determine the donominations of the change given to the customer
def denominations(change):
    # Variables that count the number of each bill or coin
    hundreds = 0
    fifties = 0
    twenties = 0
    tens = 0
    fives = 0
    toonies = 0
    loonies = 0
    quarters = 0
    dimes = 0
    nickels = 0

    # PROCESS: The change is rounded to the nearest 0.05 since pennies are not used as a form of payment
    change = float(round(change / 0.05) * 0.05)
    change = round(change, 2)
    rounded_change = change
    
    # While statement that will keep running as long as the change is greater than 0. Each if statement substracts a number from
    # the remaining change to see if that bill or coin is needed until the remaining change is 0.
    while change > 0:
        if change - 100 >= 0:
            hundreds += 1
            change -= 100
            change = round(change, 2)
            continue
        elif change - 50 >= 0:
            fifties += 1
            change -= 50
            change = round(change, 2)
            continue
        elif change - 20 >= 0:
            twenties += 1
            change -= 20
            change = round(change, 2)
            continue
        elif change - 10 >= 0:
            tens += 1
            change -= 10
            change = round(change, 2)
            continue
        elif change - 5 >= 0:
            fives += 1
            change -= 5
            change = round(change, 2)
            continue
        elif change - 2 >= 0:
            toonies += 1
            change -= 2
            change = round(change, 2)
            continue
        elif change - 1 >= 0:
            loonies += 1
            change -= 1
            change = round(change, 2)
            continue
        elif change - 0.25 >= 0:
            quarters += 1
            change -= 0.25
            change = round(change, 2)
            continue
        elif change - 0.1 >= 0:
            dimes += 1
            change -= 0.1
            change = round(change, 2)
            continue
        elif change - 0.05 >= 0:
            nickels += 1
            change -= 0.05
            change = round(change, 2)
            continue
    
    # Returns the rounded_change as well as the number of each bill/coin due to the customer
    return rounded_change, hundreds, fifties, twenties, tens, fives, toonies, loonies, quarters, dimes, nickels

shop_again = True

while shop_again == True:
    # Array that stores the different items available for purchase
    items = ["Apples", "Bananas", "Oranges", "Peaches", "Kiwis"]
    # Array that stores the corresponding prices of each item
    price = [2, 0.50, 1.50, 0.75, 1]
    # Empty arrays that will store the items in the cart and their respective quantities
    cart_items = [ ]
    cart_quantity = [ ]
    # Variable that stores the total cost of the purchase
    total_cost = 0
    # Variable that store the quantity of each fruit
    apples_quantity, bananas_quantity, oranges_quantity, peaches_quantity, kiwis_quantity = 0, 0, 0, 0, 0

    # OUTPUT: Displays a welcome message to the user
    print("*" * 30)
    print("Welcome to Aarav's Fruit Shop!\n" + "*" * 30 + "\nHere are the items you can buy with their price: ")

    # OUTPUT: Displays all 5 items in the store and their respective prices
    for i in range(5):
        print(items[i] + " (${:.2f}".format(price[i]) + " each)")
    print("*" * 30)

    repeat = True

    # While statement that will keep running as long as the user wants to add, delete, or view their cart
    while repeat == True:
        # OUTPUT: Displays a list of options/actions that the user can perform
        print("Menu:\n1 -> Add an Item to Cart\n2 -> Delete an Item from Cart\n3 -> View Your Cart\n4 -> Proceed to Checkout")
        # INPUT: Prompts the user for an action
        action = input("What would you like to do?: ")

        # If the user inputs, "add", then it will run this piece of code
        if action == "1":
            invalid_add_item = True

            # While loop that makes sure any invalid input prompts the user to try again
            while invalid_add_item == True:
                # OUTPUT: Displays a menu with the fruits and their corresponding letters so the user can enter a fruit
                print("Menu for Purchasing:\nA -> Apples\nB -> Bananas\nC -> Oranges\nD -> Peaches\nE -> Kiwis")
                # INPUT: Prompts user to input which item they would like to purchase
                add_item = input("Which item would you like to purchase?: ")
                
                # If the item is apples, it will run this piece of code
                if add_item == "A":
                    # Checks to see if apples are already in the cart and this code will run if it isn't
                    if "Apples" not in cart_items:
                        invalid_apples = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_apples == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of apples they would like to purchase
                                apples_quantity = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if apples_quantity > 0:
                                    invalid_apples = False
                                elif apples_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif apples_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")
                        
                        # PROCESS: The cost of the apples are calculated, then added to the total cost
                        apples_cost = apples_quantity * 2
                        total_cost += apples_cost
                        # PROCESS: Apples are added to the cart since they are not on it already and its quantity is added to the quantity list
                        cart_items.append("Apples")
                        cart_quantity.append(apples_quantity)
                        # OUTPUT: The program will output the cost of these apples and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(apples_cost) + ". It has been added to the cart.")
                    
                    # This will run if apples are already in the cart
                    else:
                        invalid_apples = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_apples == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of apples they would like to purchase
                                added_apples = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if added_apples > 0:
                                    invalid_apples = False
                                elif added_apples < 0:
                                    print("Number must be positive. Please try again.")
                                elif added_apples == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")
                        
                        # PROCESS: The cost of the apples are calculated, then added to the total cost
                        added_apples_cost = added_apples * 2
                        apples_cost += added_apples_cost
                        total_cost += added_apples_cost
                        apples_quantity += added_apples
                        # PROCESS: The added quantity is added to the previous number of apples 
                        cart_quantity[cart_items.index("Apples")] = apples_quantity
                        # OUTPUT: The program will output the cost of these apples and a confirmation they have been added to the cart 
                        print("This will cost ${:.2f}".format(added_apples_cost) + ". It has been added to the cart.")
                    invalid_add_item = False
                
                # If the item is bananas, it will run this piece of code 
                elif add_item == "B":
                    # Checks to see if bananas are already in the cart and this code will run if it isn't
                    if "Bananas" not in cart_items:
                        invalid_bananas = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_bananas == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of bananas they would like to purchase
                                bananas_quantity = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if bananas_quantity > 0:
                                    invalid_bananas = False
                                elif bananas_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif bananas_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: The cost of the bananas are calculated, then added to the total cost
                        bananas_cost = bananas_quantity * 0.5
                        total_cost += bananas_cost
                        # PROCESS: Bananas are added to the cart since they are not on it already and its quantity is added to the quantity list
                        cart_items.append("Bananas")
                        cart_quantity.append(bananas_quantity)
                        # OUTPUT: The program will output the cost of these bananas and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(bananas_cost) + ". It has been added to the cart.")
                    
                    # This will run if bananas are already in the cart
                    else:
                        invalid_bananas = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_bananas == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of bananas they would like to purchase
                                added_bananas = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if added_bananas > 0:
                                    invalid_bananas = False
                                elif added_bananas < 0:
                                    print("Number must be positive. Please try again.")
                                elif added_bananas == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")
                        
                        # PROCESS: The cost of the bananas are calculated, then added to the total cost
                        added_bananas_cost = added_bananas * 0.5
                        bananas_cost += added_bananas_cost
                        total_cost += added_bananas_cost
                        bananas_quantity += added_bananas
                        # PROCESS: The added quantity is added to the previous number of bananas 
                        cart_quantity[cart_items.index("Bananas")] = bananas_quantity
                        # OUTPUT: The program will output the cost of these bananas and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(added_bananas_cost) + ". It has been added to the cart.")
                    invalid_add_item = False
                
                # If the item is oranges, it will run this piece of code 
                elif add_item == "C":
                    # Checks to see if oranges are already in the cart and this code will run if it isn't
                    if "Oranges" not in cart_items:
                        invalid_oranges = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_oranges == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of oranges they would like to purchase
                                oranges_quantity = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if oranges_quantity > 0:
                                    invalid_oranges = False
                                elif oranges_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif oranges_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: The cost of the oranges are calculated, then added to the total cost
                        oranges_cost = oranges_quantity * 1.5
                        total_cost += oranges_cost
                        # PROCESS: Oranges are added to the cart since they are not on it already and its quantity is added to the quantity list
                        cart_items.append("Oranges")
                        cart_quantity.append(oranges_quantity)
                        # OUTPUT: The program will output the cost of these oranges and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(oranges_cost) + ". It has been added to the cart.")
                        
                    # This will run if oranges are already in the cart    
                    else:
                        invalid_oranges = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_oranges == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of oranges they would like to purchase
                                added_oranges = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if added_oranges > 0:
                                    invalid_oranges = False
                                elif added_oranges < 0:
                                    print("Number must be positive. Please try again.")
                                elif added_oranges == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: The cost of the oranges are calculated, then added to the total cost
                        added_oranges_cost = added_oranges * 1.5
                        oranges_cost += added_oranges_cost
                        total_cost += added_oranges_cost
                        # PROCESS: The added quantity is added to the previous number of oranges
                        oranges_quantity += added_oranges
                        cart_quantity[cart_items.index("Oranges")] = oranges_quantity
                        # OUTPUT: The program will output the cost of these oranges and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(added_oranges_cost) + ". It has been added to the cart.")
                    invalid_add_item = False
                
                # If the item is peaches, it will run this piece of code 
                elif add_item == "D":
                    # Checks to see if peaches are already in the cart and this code runs if it isn't
                    if "Peaches" not in cart_items:
                        invalid_peaches = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_peaches == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of peaches they would like to purchase
                                peaches_quantity = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if peaches_quantity > 0:
                                    invalid_peaches = False
                                elif peaches_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif peaches_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: The cost of the peaches are calculated, then added to the total cost
                        peaches_cost = peaches_quantity * 0.75
                        total_cost += peaches_cost
                        # PROCESS: Peaches are added to the cart since they are not on it already and its quantity is added to the quantity list
                        cart_items.append("Peaches")
                        cart_quantity.append(peaches_quantity)
                        # OUTPUT: The program will output the cost of these peaches and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(peaches_cost) + ". It has been added to the cart.")
                    
                    # This will run if peaches are already in the cart 
                    else:
                        invalid_peaches = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_peaches == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of peaches they would like to purchase
                                added_peaches = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if added_peaches > 0:
                                    invalid_peaches = False
                                elif added_peaches < 0:
                                    print("Number must be positive. Please try again.")
                                elif added_peaches == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: The cost of the peaches are calculated, then added to the total cost
                        added_peaches_cost = added_peaches * 0.75
                        peaches_cost += added_peaches_cost
                        total_cost += added_peaches_cost
                        # PROCESS: The added quantity is added to the previous number of peaches
                        peaches_quantity += added_peaches
                        cart_quantity[cart_items.index("Peaches")] = peaches_quantity
                        # OUTPUT: The program will output the cost of these peaches and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(added_peaches_cost) + ". It has been added to the cart.")
                    invalid_add_item = False
                
                # If the item is kiwis, it will run this piece of code 
                elif add_item == "E":
                    # Checks to see if kiwis are already in the cart and this code runs if it isn't
                    if "Kiwis" not in cart_items:
                        invalid_kiwis = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_kiwis == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of kiwis they would like to purchase
                                kiwis_quantity = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if kiwis_quantity > 0:
                                    invalid_kiwis = False
                                elif kiwis_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif kiwis_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: The cost of the kiwis are calculated, then added to the total cost
                        kiwis_cost = kiwis_quantity * 1
                        total_cost += kiwis_cost
                        # PROCESS: Kiwis are added to the cart since they are not on it already and its quantity is added to the quantity list
                        cart_items.append("Kiwis")
                        cart_quantity.append(kiwis_quantity)
                        # OUTPUT: The program will output the cost of these kiwis and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(kiwis_cost) + ". It has been added to the cart.")
                    
                    # This will run if kiwis are already in the cart
                    else:
                        invalid_kiwis = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_kiwis == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of kiwis they would like to purchase
                                added_kiwis = int(input("How many would you like to add to the cart?: "))
                                # if statement to check if user inputs a positive and non-zero number so they can try again
                                if added_kiwis > 0:
                                    invalid_kiwis = False
                                elif added_kiwis < 0:
                                    print("Number must be positive. Please try again.")
                                elif added_kiwis == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: The cost of the kiwis are calculated, then added to the total cost
                        added_kiwis_cost = added_kiwis * 1
                        kiwis_cost += added_kiwis_cost
                        total_cost += added_kiwis_cost
                        # PROCESS: The added quantity is added to the previous number of kiwis
                        kiwis_quantity += added_kiwis
                        cart_quantity[cart_items.index("Kiwis")] = kiwis_quantity
                        # OUTPUT: The program will output the cost of these kiwis and a confirmation they have been added to the cart
                        print("This will cost ${:.2f}".format(added_kiwis_cost) + ". It has been added to the cart.")
                    invalid_add_item = False
                # If the user enters an item not on the list, it will print an invalid statement and prompt them to choose an item from the list
                else:
                    print("Invalid Input. Please enter an item from the list provided.")

        # This will run if the user wants to delete an item from their cart
        elif action == "2":
            invalid_delete_item = True
            
            # While loop that will loop if the user inputs an invalid input
            while invalid_delete_item == True:
                # If the cart has no items, it will display a message saying the cart is empty
                if len(cart_items) == 0:
                    print("Your cart is empty, you cannot delete anything.")
                    break
                
                print("Here is your cart:")
                for i in range(len(cart_items)):
                    print(cart_quantity[i], cart_items[i])
                    
                # INPUT: Prompts the user to input the item they would like to delete from their cart
                delete_item = input("Which item would you like to delete from the cart?: ")

                # If the user wants to delete apples, it will run this code
                if delete_item == "Apples":
                    # Checks to see if apples are in the cart and this will run if it is 
                    if "Apples" in cart_items:
                        invalid_delete_quant = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_delete_quant == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of apples they would like to delete 
                                delete_quantity = int(input("How many would you like to delete?: "))
                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                if delete_quantity <= apples_quantity and delete_quantity > 0:
                                    invalid_delete_quant = False
                                elif delete_quantity > apples_quantity:
                                    print("You cannot delete more than what is in your cart. Please try again.")
                                elif delete_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif delete_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: Removes apples from the cart and their respective quantity
                        if apples_quantity == delete_quantity:
                            del cart_quantity[cart_items.index("Apples")]
                            cart_items.remove("Apples")
                        else:
                            cart_quantity[cart_items.index("Apples")] = apples_quantity - delete_quantity
                        
                        apples_quantity -= delete_quantity
                        # PROCESS: Subtracts the cost of the apples frocm the total cost
                        total_cost -= delete_quantity * 2
                        # OUTPUT: Displays a confirmation message that the apples have been removed from the cart
                        print(str(delete_quantity) + " apples have been removed from the cart.")
                    # If apples are not in the cart, it will run this piece of code
                    else:
                        # OUTPUT: Displays a message showing that apples are not in the cart and cannot be deleted
                        print("This item is not in your cart.")
                    invalid_delete_item = False
                
                # If the user wants to delete bananas, it will run this code
                elif delete_item == "Bananas":
                    # Checks to see if bananas are in the cart and this will run if it is 
                    if "Bananas" in cart_items:
                        invalid_delete_quant = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_delete_quant == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of bananas they would like to delete 
                                delete_quantity = int(input("How many would you like to delete?: "))
                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                if delete_quantity <= bananas_quantity and delete_quantity > 0:
                                    invalid_delete_quant = False
                                elif delete_quantity > bananas_quantity:
                                    print("You cannot delete more than what is in your cart. Please try again.")
                                elif delete_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif delete_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")

                        # PROCESS: Removes bananas from the cart and their respective quantity
                        if bananas_quantity == delete_quantity:
                            del cart_quantity[cart_items.index("Bananas")]
                            cart_items.remove("Bananas")
                        else:
                            cart_quantity[cart_items.index("Bananas")] = bananas_quantity - delete_quantity
                        
                        bananas_quantity -= delete_quantity
                        # PROCESS: Subtracts the cost of the bananas from the total cost
                        total_cost -= delete_quantity * 0.5
                        # OUTPUT: Displays a confirmation message that the bananas have been removed from the cart
                        print(str(delete_quantity) + " bananas have been removed from the cart.")
                    # If bananas are not in the cart, it will run this piece of code
                    else:
                        # OUTPUT: Displays a message showing that bananas are not in the cart and cannot be deleted
                        print("This item is not in your cart.")
                    invalid_delete_item = False

                # If the user wants to delete oranges, it will run this code
                elif delete_item == "Oranges":
                    # Checks to see if oranges are in the cart and this will run if it is 
                    if "Oranges" in cart_items:
                        invalid_delete_quant = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_delete_quant == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of oranges they would like to delete 
                                delete_quantity = int(input("How many would you like to delete?: "))
                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                if delete_quantity <= oranges_quantity and delete_quantity > 0:
                                    invalid_delete_quant = False
                                elif delete_quantity > oranges_quantity:
                                    print("You cannot delete more than what is in your cart. Please try again.")
                                elif delete_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif delete_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")
                        # PROCESS: Removes oranges from the cart and their respective quantity
                        if oranges_quantity == delete_quantity:
                            del cart_quantity[cart_items.index("Oranges")]
                            cart_items.remove("Oranges")
                        else:
                            cart_quantity[cart_items.index("Oranges")] = oranges_quantity - delete_quantity
                        oranges_quantity -= delete_quantity
                        # PROCESS: Subtracts the cost of the oranges from the total cost
                        total_cost -= delete_quantity * 1.5
                        # OUTPUT: Displays a confirmation message that the oranges have been removed from the cart
                        print(str(delete_quantity) + " oranges have been removed from the cart.")
                    # If oranges are not in the cart, it will run this piece of code
                    else:
                        # OUTPUT: Displays a message showing that oranges are not in the cart and cannot be deleted
                        print("This item is not in your cart.")
                    invalid_delete_item = False

                # If the user wants to delete peaches, it will run this code
                elif delete_item == "Peaches":
                    # Checks to see if peaches are in the cart and this will run if it is 
                    if "Peaches" in cart_items:
                        invalid_delete_quant = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_delete_quant == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of peaches they would like to delete 
                                delete_quantity = int(input("How many would you like to delete?: "))
                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                if delete_quantity <= peaches_quantity and delete_quantity > 0:
                                    invalid_delete_quant = False
                                elif delete_quantity > peaches_quantity:
                                    print("You cannot delete more than what is in your cart. Please try again.")
                                elif delete_quantity > apples_quantity:
                                    print("You cannot delete more than what is in your cart. Please try again.")
                                elif delete_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif delete_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")
                        # PROCESS: Removes peaches from the cart and their respective quantity
                        if peaches_quantity == delete_quantity:
                            del cart_quantity[cart_items.index("Peaches")]
                            cart_items.remove("Peaches")
                        else:
                            cart_quantity[cart_items.index("Peaches")] = peaches_quantity - delete_quantity
                        peaches_quantity -= delete_quantity
                        # PROCESS: Subtracts the cost of the peaches from the total cost
                        total_cost -= delete_quantity * 0.75
                        # OUTPUT: Displays a confirmation message that the peaches have been removed from the cart
                        print("Peaches have been removed from the cart.")
                    # If peaches are not in the cart, it will run this piece of code
                    else:
                        # OUTPUT: Displays a message showing that peaches are not in the cart and cannot be deleted
                        print("This item is not in your cart.")
                    invalid_delete_item = False

                # If the user wants to delete kiwis, it will run this code
                elif delete_item == "Kiwis":
                    # Checks to see if kiwis are in the cart and this will run if it is 
                    if "Kiwis" in cart_items:
                        invalid_delete_quant = True

                        # While loop to make sure any invalid input prompts user to try again
                        while invalid_delete_quant == True:   
                            # Try and except statement to stop program from crashing if user inputs an invalid input
                            try:    
                                # INPUT: Prompts user to input the amount of kiwis they would like to delete 
                                delete_quantity = int(input("How many would you like to delete?: "))
                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                if delete_quantity <= kiwis_quantity and delete_quantity > 0:
                                    invalid_delete_quant = False
                                elif delete_quantity > kiwis_quantity:
                                    print("You cannot delete more than what is in your cart. Please try again.")
                                elif delete_quantity < 0:
                                    print("Number must be positive. Please try again.")
                                elif delete_quantity == 0:
                                    print("Number cannot be 0. Please try again.")
                            except:
                                print("Invalid Input. Input must be an integer. Please try again.")
                        # PROCESS: Removes kiwis from the cart and their respective quantity
                        if kiwis_quantity == delete_quantity:
                            del cart_quantity[cart_items.index("Kiwis")]
                            cart_items.remove("Kiwis")
                        else:
                            cart_quantity[cart_items.index("Kiwis")] = kiwis_quantity - delete_quantity
                        kiwis_quantity -= delete_quantity
                        # PROCESS: Subtracts the cost of the kiwis from the total cost
                        total_cost -= delete_quantity 
                        # OUTPUT: Displays a confirmation message that the kiwis have been removed from the cart
                        print(str(delete_quantity) + " kiwis have been removed from the cart.")
                    # If kiwis are not in the cart, it will run this piece of code
                    else:
                        # OUTPUT: Displays a message showing that kiwis are not in the cart and cannot be deleted
                        print("This item is not in your cart.")
                    invalid_delete_item = False

                # This will run if the user inputs an item not available in the store
                else:
                    # OUTPUT: Displays a message saying invalid input and prompts them to choose an item from the list
                    print("Invalid Input. Please enter an item from the list provided.")

        # If the user wants to view the cart, this piece of code will run
        elif action == "3":
            # If the length of the cart is 0, it is empty
            if len(cart_items) == 0:
                # OUTPUT: Displays a message saying their cart is empty
                print("Your cart is empty!")
            # If the cart is not empty, then it will run this piece of code
            else:
                print("-" * 20 + "\nHere is your cart:")
                # For loop that will display the quantity with the fruit in a list
                for i in range(len(cart_items)):
                    print(cart_quantity[i], cart_items[i])
                print("Subtotal: ${:.2f}".format(total_cost))
                print("-" * 20)

        # If the user wants to checkout, it will break out of the while loop and run this piece of code
        elif action == "4":
            if len(cart_items) == 0:
                print("You cannot checkout with 0 items in the cart.")
                continue
            invalid_action = True
            repeat = False
            # PROCESS: The tax is calculated by multiplying the total by 0.13 and rounding it to 2 decimal places
            tax = round((total_cost * 0.13), 2)
            # PROCESS: The final total is calculated by adding the tax and subtotal
            final_total = total_cost + tax
            # OUTPUT: Displays the total for this purchase
            print("-" * 20)
            print("Cost of Purchase: ")
            print("Subtotal: ${:.2f}".format(total_cost))
            print("Tax: ${:.2f}".format(tax))
            print("Total: ${:.2f}".format(final_total))
            print("-" * 20)

            # While loop that loops if the user input is not card or cash
            while invalid_action == True:
                # INPUT: Prompts the user to input if they will be paying with card or cash
                payment_method = input("Will you be paying with cash or card? (Card/Cash): ")

                # If they input card, then it will run this piece of code
                if payment_method == "Card":
                    # OUTPUT: The receipt will be displayed with their purchase order, subtotal, tax, grand total, and a goodbye message
                    print("Here is the receipt for your purchase:")
                    print("*" * 30 + "\nRECEIPT\n" + "*" * 30)
                    print("Items:")
                    for i in range(len(cart_items)):
                        print(cart_quantity[i], cart_items[i])
                    print("-" * 30)
                    print("Subtotal: ${:.2f}".format(total_cost))
                    print("Tax: ${:.2f}".format(tax))
                    print("Total: ${:.2f}".format(final_total))
                    print("Method of Transaction: Card")
                    print("Change: $0.00")
                    print("*" * 30)
                    invalid_action = False
                
                # If they want to pay in cash, it will run this piece of code
                elif payment_method == "Cash":
                    x = True
                    y = True
                    invalid_amount = True
                    
                    # While loop that will keep looping if the amount of cash is invalid
                    while invalid_amount == True and x == True and y == True:
                        # INPUT: Prompts the user to enter the amount of cash they give
                        amount_tendered = input("Enter the amount of cash that you will tender for this purchase in dollars: ")
                        # Try and except statement that checks if the user inputs a string
                        try:
                            float_amount = float(amount_tendered)
                        except:
                            # OUTPUT: Displays a message saying the amount must be a number
                            print("The amount must be a number. Please try again.")
                            continue
                        
                        # If statement that checks if there are only 2 decimal places in the amount of money given
                        if len(amount_tendered[amount_tendered.rfind('.') + 1:]) != 2:
                            # OUTPUT: Displays a message saying that the amount must only have 2 decimal places
                            print("The amount must only have 2 decimal places. Please try again.")
                            continue
                        
                        # If statement to check if the amount is a negative number
                        elif float(amount_tendered) < 0:
                            # OUTPUT: Displays a message saying that the number must be positive
                            print("The amount must be a positive number. Please try again.")
                            continue
                        
                        # If statement that checks if the amount given is greater than or equal to the final total
                        elif float(amount_tendered) < final_total:
                            # OUTPUT: Displays a message saying that the amount given cannot be lower than the final total
                            print("Cash must be greater or equal to the amount of the purchase. You do not have enough money.")
                            print("You must delete items to afford the purchase.")
                            
                            invalid_delete_item = True
            
                            # While loop that will loop if the user inputs an invalid input
                            while (invalid_delete_item == True or float(amount_tendered) < final_total) and x == True:
                                print("-" * 20 + "\nHere is your cart:")
                                # For loop that will display the quantity with the fruit in a list
                                for i in range(len(cart_items)):
                                    print(cart_quantity[i], cart_items[i])
                                print("Final Total: ${:.2f}".format(final_total))
                                print("-" * 20)
                                # INPUT: Prompts the user to input the item they would like to delete from their cart
                                delete_item = input("Which item would you like to delete from the cart?: ")

                                # If the user wants to delete apples, it will run this code
                                if delete_item == "Apples":
                                    # Checks to see if apples are in the cart and this will run if it is 
                                    if "Apples" in cart_items:
                                        invalid_delete_quant = True

                                        # While loop to make sure any invalid input prompts user to try again
                                        while invalid_delete_quant == True:   
                                            # Try and except statement to stop program from crashing if user inputs an invalid input
                                            try:    
                                                # INPUT: Prompts user to input the amount of apples they would like to delete 
                                                delete_quantity = int(input("How many would you like to delete?: "))
                                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                                if delete_quantity <= apples_quantity and delete_quantity > 0:
                                                    invalid_delete_quant = False
                                                elif delete_quantity > apples_quantity:
                                                    print("You cannot delete more than what is in your cart. Please try again.")
                                                elif delete_quantity < 0:
                                                    print("Number must be positive. Please try again.")
                                                elif delete_quantity == 0:
                                                    print("Number cannot be 0. Please try again.")
                                            except:
                                                print("Invalid Input. Input must be an integer. Please try again.")
                                        # PROCESS: Removes apples from the cart and their respective quantity
                                        if apples_quantity == delete_quantity:
                                            del cart_quantity[cart_items.index("Apples")]
                                            cart_items.remove("Apples")
                                        
                                        else:
                                            cart_quantity[cart_items.index("Apples")] = apples_quantity - delete_quantity
                                        apples_quantity -= delete_quantity
                                        
                                        # PROCESS: Subtracts the cost of the apples frocm the total cost
                                        total_cost -= delete_quantity * 2
                                        final_total = total_cost + round((total_cost * 0.13), 2)
                                        # OUTPUT: Displays a confirmation message that the apples have been removed from the cart
                                        print(str(delete_quantity) + " apples have been removed from the cart.")
                                    # If apples are not in the cart, it will run this piece of code
                                    else:
                                        # OUTPUT: Displays a message showing that apples are not in the cart and cannot be deleted
                                        print("This item is not in your cart. Please choose an item in your cart.")
                                    invalid_delete_item = False
                                
                                # If the user wants to delete bananas, it will run this code
                                elif delete_item == "Bananas":
                                    # Checks to see if bananas are in the cart and this will run if it is 
                                    if "Bananas" in cart_items:
                                        invalid_delete_quant = True

                                        # While loop to make sure any invalid input prompts user to try again
                                        while invalid_delete_quant == True:   
                                            # Try and except statement to stop program from crashing if user inputs an invalid input
                                            try:    
                                                # INPUT: Prompts user to input the amount of bananas they would like to delete 
                                                delete_quantity = int(input("How many would you like to delete?: "))
                                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                                if delete_quantity <= bananas_quantity and delete_quantity > 0:
                                                    invalid_delete_quant = False
                                                elif delete_quantity > bananas_quantity:
                                                    print("You cannot delete more than what is in your cart. Please try again.")
                                                elif delete_quantity < 0:
                                                    print("Number must be positive. Please try again.")
                                                elif delete_quantity == 0:
                                                    print("Number cannot be 0. Please try again.")
                                            except:
                                                print("Invalid Input. Input must be an integer. Please try again.")
                                        # PROCESS: Removes bananas from the cart and their respective quantity
                                        if bananas_quantity == delete_quantity:
                                            del cart_quantity[cart_items.index("Bananas")]
                                            cart_items.remove("Bananas")
                                        else:
                                            cart_quantity[cart_items.index("Bananas")] = bananas_quantity - delete_quantity
                                        bananas_quantity -= delete_quantity
                                        # PROCESS: Subtracts the cost of the bananas from the total cost
                                        total_cost -= delete_quantity * 0.5
                                        final_total = total_cost + round((total_cost * 0.13), 2)
                                        # OUTPUT: Displays a confirmation message that the bananas have been removed from the cart
                                        print(str(delete_quantity) + " bananas have been removed from the cart.")
                                    # If bananas are not in the cart, it will run this piece of code
                                    else:
                                        # OUTPUT: Displays a message showing that bananas are not in the cart and cannot be deleted
                                        print("This item is not in your cart. Please choose an item in your cart.")
                                    invalid_delete_item = False

                                # If the user wants to delete oranges, it will run this code
                                elif delete_item == "Oranges":
                                    # Checks to see if oranges are in the cart and this will run if it is 
                                    if "Oranges" in cart_items:
                                        invalid_delete_quant = True

                                        # While loop to make sure any invalid input prompts user to try again
                                        while invalid_delete_quant == True:   
                                            # Try and except statement to stop program from crashing if user inputs an invalid input
                                            try:    
                                                # INPUT: Prompts user to input the amount of oranges they would like to delete 
                                                delete_quantity = int(input("How many would you like to delete?: "))
                                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                                if delete_quantity <= oranges_quantity and delete_quantity > 0:
                                                    invalid_delete_quant = False
                                                elif delete_quantity > oranges_quantity:
                                                    print("You cannot delete more than what is in your cart. Please try again.")
                                                elif delete_quantity < 0:
                                                    print("Number must be positive. Please try again.")
                                                elif delete_quantity == 0:
                                                    print("Number cannot be 0. Please try again.")
                                            except:
                                                print("Invalid Input. Input must be an integer. Please try again.")
                                        # PROCESS: Removes oranges from the cart and their respective quantity
                                        if oranges_quantity == delete_quantity:
                                            del cart_quantity[cart_items.index("Oranges")]
                                            cart_items.remove("Oranges")
                                        else:
                                            cart_quantity[cart_items.index("Oranges")] = oranges_quantity - delete_quantity
                                        oranges_quantity -= delete_quantity
                                        # PROCESS: Subtracts the cost of the oranges from the total cost
                                        total_cost -= delete_quantity * 1.5
                                        final_total = total_cost + round((total_cost * 0.13), 2)
                                        # OUTPUT: Displays a confirmation message that the oranges have been removed from the cart
                                        print(str(delete_quantity) + " oranges have been removed from the cart.")
                                    # If oranges are not in the cart, it will run this piece of code
                                    else:
                                        # OUTPUT: Displays a message showing that oranges are not in the cart and cannot be deleted
                                        print("This item is not in your cart. Please choose an item in your cart.")
                                    invalid_delete_item = False

                                # If the user wants to delete peaches, it will run this code
                                elif delete_item == "Peaches":
                                    # Checks to see if peaches are in the cart and this will run if it is 
                                    if "Peaches" in cart_items:
                                        invalid_delete_quant = True

                                        # While loop to make sure any invalid input prompts user to try again
                                        while invalid_delete_quant == True:   
                                            # Try and except statement to stop program from crashing if user inputs an invalid input
                                            try:    
                                                # INPUT: Prompts user to input the amount of peaches they would like to delete 
                                                delete_quantity = int(input("How many would you like to delete?: "))
                                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                                if delete_quantity <= peaches_quantity and delete_quantity > 0:
                                                    invalid_delete_quant = False
                                                elif delete_quantity > peaches_quantity:
                                                    print("You cannot delete more than what is in your cart. Please try again.")
                                                elif delete_quantity < 0:
                                                    print("Number must be positive. Please try again.")
                                                elif delete_quantity == 0:
                                                    print("Number cannot be 0. Please try again.")
                                            except:
                                                print("Invalid Input. Input must be an integer. Please try again.")
                                        # PROCESS: Removes peaches from the cart and their respective quantity
                                        if peaches_quantity == delete_quantity:
                                            del cart_quantity[cart_items.index("Peaches")]
                                            cart_items.remove("Peaches")
                                        else:
                                            cart_quantity[cart_items.index("Peaches")] = peaches_quantity - delete_quantity
                                        peaches_quantity -= delete_quantity
                                        # PROCESS: Subtracts the cost of the peaches from the total cost
                                        total_cost -= delete_quantity * 0.75
                                        final_total = total_cost + round((total_cost * 0.13), 2)
                                        # OUTPUT: Displays a confirmation message that the peaches have been removed from the cart
                                        print(str(delete_quantity) + " peaches have been removed from the cart.")
                                    # If peaches are not in the cart, it will run this piece of code
                                    else:
                                        # OUTPUT: Displays a message showing that peaches are not in the cart and cannot be deleted
                                        print("This item is not in your cart. Please choose an item in your cart.")
                                    invalid_delete_item = False

                                # If the user wants to delete kiwis, it will run this code
                                elif delete_item == "Kiwis":
                                    # Checks to see if kiwis are in the cart and this will run if it is 
                                    if "Kiwis" in cart_items:
                                        invalid_delete_quant = True

                                        # While loop to make sure any invalid input prompts user to try again
                                        while invalid_delete_quant == True:   
                                            # Try and except statement to stop program from crashing if user inputs an invalid input
                                            try:    
                                                # INPUT: Prompts user to input the amount of kiwis they would like to delete 
                                                delete_quantity = int(input("How many would you like to delete?: "))
                                                # if statement to check if user inputs a number that is greater than existing fruit or invalid input
                                                if delete_quantity <= kiwis_quantity and delete_quantity > 0:
                                                    invalid_delete_quant = False
                                                elif delete_quantity > kiwis_quantity:
                                                    print("You cannot delete more than what is in your cart. Please try again.")
                                                elif delete_quantity < 0:
                                                    print("Number must be positive. Please try again.")
                                                elif delete_quantity == 0:
                                                    print("Number cannot be 0. Please try again.")
                                            except:
                                                print("Invalid Input. Input must be an integer. Please try again.")
                                        # PROCESS: Removes kiwis from the cart and their respective quantity
                                        if kiwis_quantity == delete_quantity:
                                            del cart_quantity[cart_items.index("Kiwis")]
                                            cart_items.remove("Kiwis")
                                        else:
                                            cart_quantity[cart_items.index("Kiwis")] = kiwis_quantity - delete_quantity
                                        kiwis_quantity -= delete_quantity
                                        # PROCESS: Subtracts the cost of the kiwis from the total cost
                                        total_cost -= delete_quantity 
                                        final_total = total_cost + round((total_cost * 0.13), 2)
                                        # OUTPUT: Displays a confirmation message that the kiwis have been removed from the cart
                                        print("Kiwis have been removed from the cart.")
                                    # If kiwis are not in the cart, it will run this piece of code
                                    else:
                                        # OUTPUT: Displays a message showing that kiwis are not in the cart and cannot be deleted
                                        print("This item is not in your cart. Please choose an item in your cart.")
                                    invalid_delete_item = False

                                # This will run if the user inputs an item not available in the store
                                else:
                                    # OUTPUT: Displays a message saying invalid input and prompts them to choose an item from the list
                                    print("Invalid Input. Please enter an item in your cart.")
                                    continue

                                if len(cart_items) == 0:
                                    x = False
                                    invalid_action = False
                                    print("There is nothing remaining in your cart. You may shop again or leave the store.")
                                
                                elif float(amount_tendered) < final_total:
                                    print("You still cannot afford this purchase. You will need to delete more items.")
                                
                                elif float(amount_tendered) > final_total:
                                    print("You can afford this purchase.")
                                    actual_amount = float(amount_tendered)
                                    y = False

                        # Else statement that will convert the string into a float since it is a valid input
                        else:
                            print("You can afford this purchase.")
                            actual_amount = float(amount_tendered)
                            invalid_amount = False
                            

                    while x == True:
                        # PROCESS: Change is calculated by suntracting the final total from the amount given by the customer
                        change = actual_amount - final_total

                        # OUTPUT: If the change is 0, then the program will display the receipt
                        if change == 0:
                            print("There is no change for this purchase.\nHere is the receipt for your purchase:")
                            print("*" * 30 + "\nRECEIPT\n" + "*" * 30)
                            print("Items:")
                            for i in range(len(cart_items)):
                                print(cart_quantity[i], cart_items[i])
                            print("-" * 30)
                            print("Subtotal: ${:.2f}".format(total_cost))
                            print("Tax: ${:.2f}".format(tax))
                            print("Total: ${:.2f}".format(final_total))
                            print("Method of Transaction: Cash")
                            print("Change: $0.00")
                            print("*" * 30)
                        
                        # If the change is not 0, then the program will calculate the denominations of the change 
                        else:
                            # This function will return the number of bills/coins needed for the change through the denominations function 
                            rounded_change, hundreds, fifties, twenties, tens, fives, toonies, loonies, quarters, dimes, nickels = denominations(change)
                            # OUTPUT: The denominations of the change are displayed as well as the receipt for the purchase
                            print("Total Rounded Change: ${:.2f}".format(rounded_change))
                            print("Here is the denominations for your change:")
                            print("$100 Bills: " + str(hundreds))
                            print("$50 Bills: " + str(fifties))
                            print("$20 Bills: " + str(twenties))
                            print("$10 Bills: " + str(tens))
                            print("$5 Bills: " + str(fives))
                            print("$2 Coins: " + str(toonies))
                            print("$1 Coins: " + str(loonies))
                            print("$0.25 Coins: " + str(quarters))
                            print("$0.10 Coins: " + str(dimes))
                            print("$0.05 Coins: " + str(nickels))
                            print("Here is your receipt for this purchase: ")
                            print("*" * 30 + "\nRECEIPT\n" + "*" * 30)
                            print("Items:")
                            for i in range(len(cart_items)):
                                print(cart_quantity[i], cart_items[i])
                            print("-" * 30)
                            print("Subtotal: ${:.2f}".format(total_cost))
                            print("Tax: ${:.2f}".format(tax))
                            print("Total: ${:.2f}".format(final_total))
                            print("Method of Transaction: Cash")
                            print("Change: ${:.2f}".format(rounded_change))
                            print("*" * 30)
                        
                        x = False
                        invalid_action = False

                # Else statement that runs if the user does not input cash or card
                else:
                    print("Invalid Input. Please enter either Card or Cash.")
        
        # Else statement that runs if the user does not pick an option from the list
        else:
            print("Invalid Input. Please enter an option from the list.")


    invalid_rerun = True

    # While statement that will loop if the user inputs an invalid input
    while invalid_rerun == True:
        # INPUT: Asks the user if they want to run the program again
        rerun = input("Would you like to shop again? (Y/N): ")
        # If user states "Y", then it will rerun the program
        if rerun == "Y":
            invalid_rerun = False
        # If user states "N", program will output a goodbye message and the program will not rerun
        elif rerun == "N":
            print("Thank you for shopping at Aarav's Fruit Shop! \nWe hope to see you again soon!")
            invalid_rerun = False
            shop_again = False
        else:
            print("Invalid Input. Please choose one of the options.")

            