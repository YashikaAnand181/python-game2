print('-------Hey! Welcome to KBC game------- ')
play=input("Do you want to play? ")
if play.lower()=="yes":
    print("Okay! Let's play :)\n")
else:
    print("You have quit")

score=0
price=0
while True:
    total=print('The question is for Rs.1000')
    ques = print("1.What is the full form of DNS? ")
    options=print("a.Domain Name Server \t\tb.Domain Name System \nc.Domain New System \t\td.Domain Name Service \n")
    ans=input("Enter your option: ")

    if ans.lower() == "a":
        print("Correct\n")
        score +=1
        price +=1000

    else:
        print("Incorrect\n")

    total = print('The question is for Rs.2000')
    ques = print("2.Who invented Python? ")
    options=print("a.Charles Babbage \t\tb.Dennis Ritchie \nc.Guido Van Rossum \t\td.None \n")
    ans=input("Enter your option: ")

    if ans.lower() == "c":
        print("Correct\n")
        score += 1
        price +=2000
    else:
        print("Incorrect\n")

    total = print('The question is for Rs.5000')
    ques = print("3.What is the extension of C++ file? ")
    options=print("a..c \t\tb..cpp \nc..py \t\td..net \n")
    ans=input("Enter your option: ")

    if ans.lower() == "b":
        print("Correct\n")
        score += 1
        price +=5000
    else:
        print("Incorrect\n")

    total = print('The question is for Rs.10,000')
    ques = print("4.When is the Republic Day celebrated in India? ")
    options=print("a.Jan 26 \t\tb.Aug 15 \nc.Nov 26 \t\td.Sep 5 \n")
    ans=input("Enter your option: ")

    if ans.lower() == "a":
        print("Correct\n")
        score += 1
        price +=10000
    else:
        print("Incorrect\n")


    total = print('The question is for Rs.20,000')
    ques = print("5.For which field Einstein won awarded the Nobel Prize? ")
    options=print("a.Biology \t\tb.Chemistry \nc.Mathematics \td.Physics \n")
    ans=input("Enter your option: ")

    if ans.lower() == "d":
        print("Correct\n")
        score += 1
        price += 20000
    else:
        print("Incorrect\n")

    play_again =input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("You have quit")
        break


print("You have scored " + str(score) + " points")
print("You have earned Rs." + str(price) + " in total")

