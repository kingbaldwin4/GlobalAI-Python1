import random
game = ["Rock","Paper","Scissors"]
round_num = int(input("How many rounds you want to play ? "))
counter = 1
p1_score = 0
p2_score = 0
while(counter<=round_num):
    print("Round ",counter)
    random_choose_p1 = game[random.randrange(len(game))]
    random_choose_p2 = game[random.randrange(len(game))]
    print("Player1 choose: ",random_choose_p1)
    print("Player2 choose: ",random_choose_p2)
    if(random_choose_p1 == "Rock" and random_choose_p2 == "Paper"):
        print("Player2 win...")
        p2_score+=1
    elif(random_choose_p1 == "Paper" and random_choose_p2 == "Rock"):
        print("Player1 win...")
        p1_score+=1
    elif(random_choose_p1 == "Rock" and random_choose_p2 == "Scissors"):
        print("Player1 win...")
    elif(random_choose_p1 == "Scissors" and random_choose_p2 == "Rock"):
        print("Player2 win...")
        p1_score+=1
    elif(random_choose_p1 == "Scissors" and random_choose_p2 == "Paper"):
        print("Player1 win...")
        p1_score+=1
    elif(random_choose_p1 == "Paper" and random_choose_p2 == "Scissors"):
        print("Player2 win...")
        p2_score+=1
    else:
        print("Tie Condition")
    counter+=1


print("Player1 score: ",p1_score)
print("Player2 score: ",p2_score)
if(p1_score > p2_score):
    print("Player1 wins the game...")
elif(p1_score < p2_score):
    print("Player2 wins the game...")
else:
    print("It's a tie game...")