import os

from random import randint

# This function clears the screenß.
def clear_screen():
    os.system('clear') # Clears the screen. For windows change to 'cls'.


# This function creates a simple menu
def create_menu():
    print 30 * "-" , "MENU" , 30 * "-"                # MENU
    print "1. OPTELLEN"                               # Adding
    print "2. AFTREKKEN"                              # Substraction
    print "3. KEER-SOMMEN"                            # Multiplication
    print "4. DELEN"                                  # Division
    print "5. STOPPEN"                                # Quit
    print 67 * "-"


# This function asks the answer for 10 additions of two random numbers.
# It checks the input and if a mistake is made, it gives the right answer.
def adding():
    print 5 * "\n"
    for x in range(1, 10):
        a = randint(0,20)
        b = randint(0,20)
        correct_answer = a + b
        print "          %d + %d =" % (a, b),
        answer = raw_input()
        if answer.isdigit():
            if int(answer) != correct_answer:
                print "HELAAS    %d + %d = %d" % (a, b, correct_answer)
        else:
            print "Je kunt alleen getallen intypen."         # Only numbers


# This function asks the answer for 10 substractions of two random numbers.
# The result can't be negative, by making the first random number the biggest.
# It checks the input and if a mistake is made, it gives the right answer.
def substracting():
    print 5 * "\n"
    for x in range(1, 10):
        a = randint(0,20)
        b = randint(0,20)
        if b > a:  # Switch the numbers if b > a
            a, b = b, a
        print "          %d - %d =" % (a, b),
        answer = raw_input()
        if answer.isdigit():
            if int(answer) != a - b:
                print "HELAAS    %d - %d = %d" % (a, b, a - b )
        else:
            print "Je kunt alleen getallen intypen."        # Only numbers


# This function asks the answer for 10 multiplications of two random numbers.
# It checks the input and if a mistake is made, it gives the right answer.
def multiplying():
    print 5 * "\n"
    for x in range(1, 10):
        a = randint(0,10)
        b = randint(0,20)
        print "          %d * %d =" % (a, b),
        answer = raw_input()
        if answer.isdigit():
            if int(answer) != a * b:
                print "HELAAS    %d * %d = %d" % (a, b, a * b )
        else:
            print "Je kunt alleen getallen intypen."       # Only numbers


# This function asks the answer for 10 created divisions.
# One factor of the division is made by multiplying two random numbers.
# The 2nd random number, which can't be zero is used as the divider.
# It also checks the input and if a mistake is made, it gives the right answer.
def division():
    print 5 * "\n"
    for x in range(1, 10):
        a = randint(0,9)
        b = randint(1,9)     # It's division so b can't be zero
        print "          %d / %d =" % (a * b, b),
        answer = raw_input()
        if answer.isdigit():
            if int(answer) != c / b:
                print "HELAAS    %d / %d = %d" % (a * b, b, a * b / b )
        else:
            print "Je kunt alleen getallen intypen."     # Only numbers


# The main program starts here

# A boolean for the menu
in_menu = True

while in_menu:        # Stay in the menu until in_menu = False
    clear_screen()
    create_menu()
    choice = raw_input("Kies wat je wilt doen [1-5]: ")       # Choose [1-5]
    if choice == "1":
        clear_screen()
        adding()
    elif choice == "2":
        clear_screen()
        substracting()
    elif choice == "3":
        clear_screen()
        multiplying()
    elif choice == "4":
        clear_screen()
        division()
    elif choice == "5":
        clear_screen()
        in_menu = False
        print "Tot de volgende keer!"                     # See you next time
