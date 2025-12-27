import random

score_ai = 0
score_u = 0
while True:
    print("1.stone\n2.paper\n3.scissor\n4.exit")
    user = int(input("enter your choice  "))
    if user == 1:
        user = 'stone'
    if user == 2:
        user = 'paper'
    if user == 3:
        user = 'scissor'
    if user == 4 or user == '':
        print('score of AI:' + str(score_ai))
        print('score of user: ' + str(score_u))
        print("you have chose to exit the game ")
        break
    print("CHOICE OF USER: " + user)
    ai = random.randint(1, 3)
    if ai == 1:
        ai = 'stone'
    if ai == 2:
        ai = 'paper'
    if ai == 3:
        ai = 'scissor'
    print("CHOICE OF AI: " + ai)

    if (user == "stone" and ai == "scissor") or (user == "scissor" and ai == "paper") or (
            user == "paper" and ai == "stone"):
        score_u = score_u + 1
        print("User wins!")
    elif (user == ai):
        print("no one wins ")
    else:
        score_ai = score_ai + 1
        print("AI wins!")


