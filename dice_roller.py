
# add dependencies
# random library for random rice roll
import random

# create lists for dice options
die_options = ["d4", "d6", "d8", "d10", "d12", "d20"]
options_d4 = [1, 2 ,3, 4]
options_d6 = [1, 2 ,3, 4, 5, 6]
options_d8 = [1, 2 ,3, 4, 5, 6, 7, 8] 
options_d10 = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10]   
options_d12 = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
options_d20 = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] 
    
# input for how many of which die is being rolled and how many times you will roll it
print(f"Time to roll some dice! Here are the dice you can choose from {die_options}")
type_of_die = str(input("Which type of die are you rolling?"))
number_of_die = int(input("How many times will you roll it?"))

# verify that the type_of_die input is valid

if type_of_die in die_options: 
    
    # check which type_of_die was input 
    if type_of_die == "d4":
        
        #set final roll result to 0 to begin
        result_d4 = 0
        
        #loop through rolling the type_of_die input = number_of_die
        for x in range(number_of_die):
            #provides a random result from list of options_d4
            roll_d4 = random.choice(options_d4)
            #prints the result of each roll
            print(f"You roll a {roll_d4}")
            #totals all of the rolls into a final result
            result_d4 = result_d4 + roll_d4
        #print final result of rolls
        print(f"Your total result is {result_d4}!")
    
    #repeat conditionals above for all die_options
    elif type_of_die == "d6":
        result_d6 = 0

        for x in range(number_of_die):
            roll_d6 = random.choice(options_d6)
            print(f"You roll a {roll_d6}")
            result_d6 = result_d6 + roll_d6
        print(f"Your total result is {result_d6}!")

    elif type_of_die == "d8":
        result_d8 = 0

        for x in range(number_of_die):
            roll_d8 = random.choice(options_d8)
            print(f"You roll a {roll_d8}")
            result_d8 = result_d8 + roll_d8
        print(f"Your total result is {result_d8}!")

    elif type_of_die == "d10":
        result_d10 = 0

        for x in range(number_of_die):
            roll_d10 = random.choice(options_d10)
            print(f"You roll a {roll_d10}")
            result_d10 = result_d10 + roll_d10
        print(f"Your total result is {result_d10}!")
    
    elif type_of_die == "d12":
        result_d12 = 0

        for x in range(number_of_die):
            roll_d12 = random.choice(options_d12)
            print(f"You roll a {roll_d12}")
            result_d12 = result_d12 + roll_d12
        print(f"Your total result is {result_d12}!")

    elif type_of_die == "d20":
        result_d20 = 0

        for x in range(number_of_die):
            roll_d20 = random.choice(options_d20)
            
            if roll_d20 == 20:
                print(f"Critical hit! You roll a {roll_d20}!")
            else:    
                print(f"You roll a {roll_d20}")

            result_d20 = result_d20 + roll_d20
        print(f"Your total result is {result_d20}!")

    else:
        #if an error occurs
        print("Something went wrong, please try again")

else:
    #if a valid die option was not entered
    print("Please enter a valid die option.")