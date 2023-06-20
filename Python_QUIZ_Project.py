import sys
lives = 5
get_answer = input("\nWhat is your name? ")
print(get_answer)
response_2 = "\nHello " + str(get_answer)
print(response_2)
#Intro

def lives_remaining():
    while True:
        if lives == 0:
            print("\nYou have run out of lives.")
            sys.exit

def intro_question():
    while True:
        get_answer_2 = input("Do you want to continue? Press Y or N to proceed. ")
        if get_answer_2 == "Yes" or get_answer_2 == "yes":
            print("Okay let's play!")
            print("\nWe will be doing a short quiz. \nYou will only have 5 lives. \nLet's Begin")
            break
        #Exit the program is user says no.
        elif get_answer_2 == "No" or get_answer_2 == "no" or get_answer_2 == "N" or get_answer_2 == "n":
            print("OK take care!")
            sys.exit() 
        elif get_answer_2 == "y" or get_answer_2 == "Y":
            print("Okay let's play!")
            print("\nWe will be doing a short quiz. \nYou will only have 5 lives. \nLet's Begin")
            break
        else:
            print("\nPlease enter your answer with the following answer(Y or N or Yes or No)")
    return get_answer_2
intro_question()


def first_question(lives):
#FIrst question
    
    question_1 = input("\nWhat is the capital of Canada? ")
    print(question_1)
    
    if question_1 == "Ottawa":
        print("\nGood job!")
    elif question_1 == "ottawa":
        print("\nGood job!")
    else:
        lives -= 1
        print("Sorry that's incorrect. Your lives remaining is now " + str(lives))
    return lives
#This is where the variable lives will be given it's new value.
lives = first_question(lives)


if lives == 5:
    print("\nThat one was easy. Time for the next question.")
else:
    print("\nAlright don't worry let's move to the next quesiton.")

#Second question
def second_question(lives):
    while True:
        question_2 = input("\nHow many provinces are there in Canada? ")
        if question_2.isdigit():
            break
        else:
            print("Invalid input. Please enter a number.")
    if question_2 == "10":
        print("\nGood Job!")
    else:
        lives -= 1
        print("\nSorry that's not right. Your lives remaining is " + str(lives))
    return lives
lives = second_question(lives)

#Third question
def third_question(lives):
    while True:
        question_3 = input("\nIs Yellowknife a province? ")
        if question_3.lower() == "no":
            print("That's right!")
            break
        elif question_3.lower() == "yes":
            lives -= 1
            print(f"\nThat's not quite right. Your lives remaining now is {lives}.")
            break
        else:
            print("Please enter 'Yes' or 'No'")
    return lives

lives = third_question(lives)

#Random check
if lives == 5:
    print("\nWow not bad keep it up.")
else:
    print("\nOkay let's move to the next quesiton.")

#Fourth question

def question_4(lives):
    while True:
        question_4 = input("\nWhat is our provincial tax percentage currently in Ontario? ")
        if question_4.isdigit():
            question_4 = int(question_4)
            if question_4 >= 0:
                break
            else:
                print("Invalid amount.")
        else:
            print("Please enter a number.")
    if question_4 == 13:
        print("That's correct.")
    else:
        lives -= 1
        print("\nIncorrect. Your lives remaining is " + str(lives))
    return question_4
lives = question_4(lives)


#Fifth question
def question_5(lives):
    print("\nWho is the prime minister of Canada?")
    question_5_list = ["A. Doug Ford, B. Danielle Smith, C. Justin Trudeau, D. Pierre Poilievre"]
    print(question_5_list)
    get_answer_3 = input("\nA, B, C or D? ")
    if get_answer_3 == "C":
        print("\nGood Job!")
    elif get_answer_3 == "c":
        print("\nNice! That's Right!")
    else:
        print("\nSorry that is incorrect.")
        lives -= 1
    return lives
lives = question_5(lives)

#Sixth question
def sixth_question():
    while True:
        question_6 = input("What is 1+1? ")
        if question_6.isdigit():
            question_6 = int(question_6)
            if question_6 >= 0:
                break
            else:
                    print("Invalid amount.")
        else:
            print("Please enter a number.")
    if question_6 == 2:
            print("Yes that is correct!")
    else:
        print("Sorry that is incorrect.")
        lives -= 1
    return lives
lives = question_5(lives)
