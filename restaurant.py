"""Restaurant Menu"""


"""Create a function to ask the user if they are admin or customer:"""

import random
def who_are_you():
    print(f"are you a admin[A] or customer[C]".title())
    user_input = input("Please select one: ")
    if user_input == "a":
        pass_code()
    elif user_input == "c":
        get_order()
    else:
        print("sorry thats not a option")


"""This function is a password access function for chef"""
def pass_code():
    default_password = "0000"
    count = 3
    while True:
        print("Please enter the 4-digit pin")
        password = input('>')
        if password == default_password:
            # print(f"Hello chef")
            file = open("/Users/vinitha/Desktop/project/stock_items.txt","r")
            print(file.readline())
            break
        else:
            count = count - 1
            print(f"sorry!!!! you have only {count} tries...good luck".title())
            if count == 0:
                break

"""This function is used to get the order from user on different cuisine"""

def get_order():
    print(f"Here is our menu: \n"
    f"We have:\nindian[I],\nchinese[C],\namerican[A].\n"
    f"What can i get for you? ".title())
    order_input = input(">")
    if order_input == "i":
        indian_cuisine()
    elif order_input == "c":
        chinese_cuisine()
    elif order_input == "a":
        american_cuisine()
    else:
        print(f"sorry we don't serve it".title())
        #order_complete()

def indian_cuisine():
    #global dish_input
    print(f"what would you like to order in indian_cuisine/n"
    f"We have\n"
    "chicken_briyani[CB],naan[N],butter_chicken[BC]")
    dish_input = input()
    if dish_input == "cb":
        order_list(dish_input)
        complete_order()
    elif dish_input == "n":
        order_list(dish_input)
        complete_order()
    elif dish_input == "bc":
        order_list(dish_input)
        complete_order()

def chinese_cuisine():
    #global dish_input
    print(f"what would you like to order in indian_cuisine/n"
    f"We have\n"
    "friedrice[FR],dragon_chicken[DC],dumplings[D]")
    dish_input = input()
    if dish_input == "fr":
        order_list(dish_input)
        complete_order()
    elif dish_input == "dc":
        order_list(dish_input)
        complete_order()
    elif dish_input == "d":
        order_list(dish_input)
        complete_order()

def american_cuisine():
    #global dish_input
    print(f"what would you like to order in indian_cuisine/n"
    f"We have\n"
    "burger[B],fish&chips[FC],chicken strips[CS]")
    dish_input = input()
    if dish_input == "b":
        order_list(dish_input)
        complete_order()
        #order_list()
    elif dish_input == "fc":
        order_list(dish_input)
        complete_order()
    elif dish_input == "cs":
        order_list(dish_input)
        complete_order()

"""this function appended the user oder in a list"""
completed_order = []
def order_list(dish_input):
    
    completed_order.append(dish_input)
    return completed_order
    #print(completed_order)

"""asking user if the order is complete or not"""

def complete_order():
    print("would you like to order more? Yes[Y]/No[N]: ")
    user_decision = input()
    if user_decision == "y":
        get_order()
    else:
        print("complete_order")
        final_order = completed_order
        # for order in final_order:
        #     print(f"These are the final items: {order}")
        print(final_order)
        print("Your order will be ready in 5 mins!!!Do you like to play a game?Y?N")
        game_desicion = input()
        if game_desicion == "y":
            game()
        else:
            print("This is your confirmed order.")
            for order in completed_order:
                print(f"your final order list is : {order}")

"""playing game during the wait-time"""
def game():
    list = ['tea','fries','cake','coffee','cheese']
    word_to_be_guessed = random.choice(list)
    #print(word_to_be_guessed)
    print(f"Hello user the random word is a {len(word_to_be_guessed)} length word")
    user_dic = {}
    word_guess = ['_'] * len(word_to_be_guessed)
    print(word_guess)
    attempts = len(word_to_be_guessed)
    count = 0
    while True:
        not_found = False
        user_input = input("PLease enter your first character ?" )
        if user_input in user_dic:
            print(f"sorry u have alreday printed this {user_input}".title()) 
        else:
            for index,value in enumerate(word_to_be_guessed):
                if user_input == value:
                    word_guess[index]=user_input
                    not_found = True
                    count = count + 1
                    user_dic[user_input] = index

                    #print(user_dic)
                    # if user_input in user_dic:
                    #     print(f"sorry u have alreday printed this {user_input}")  
            if count == len(word_to_be_guessed):
                print(f"hi you have guessed correctly!!!! you will be getting the dish for free".title()
                )
                print(word_guess)
                break
            if not not_found:
                    print("Wrong guess")
                    attempts = attempts - 1
                    print(f"Wrong guess.You have only {attempts} attempts".title())
                    if attempts == 0:
                        print(f"sorry better luck next time".title())
                        break
            print(word_guess)


who_are_you()