#Basic version.

# print("Your welcome to my Rock Scissor Paper game")
# p1 = input("Player one pls enter your choice :  ")
# print("*** NO CHEATING ***\n" *15,end="" )
# p2 = input("Player two pls enter your choice : ")
# if (p1 == p2):
#     print("Player one is win.")
# elif (p1== "Rock" and p2 == "Scissor" ) or (p1 == "Scissor" and p2 == "Paper") or (p1 == "Paper" and p2== "Rock"):
#     print("Tie")
# else:
#     print("player two is win")

#Less Basic Version.
import random

player_wins = 0
computer_wins =0
print("Your welcome to my Rock Scissor Paper game")
best_of = int(input("Best of what? "))
while player_wins < best_of and computer_wins < best_of:
    x = random.randint(0,2)
    if x == 0:
        p2 = "rock"
    elif x ==1:
        p2= "paper"
    else:
        p2="scissor"
    print(f"-----Player score :{player_wins} Computer score :{computer_wins}-----")
    
    p1 = input("Humen player  enter your choice or quit(q) : ").lower()
    if p1 =="q":
        break
    print ( "Computer Moved " + p2 )
    
    if p1 == p2 :
        print("Tie")
    elif p1 =="rock":
        if p2 =="paper":
            print("Computer wins")
            computer_wins+=1
        else:
            print("Humen Wins")
            player_wins+=1
    elif p1 =="paper":
        if p2 =="scissor":
            print("Computer wins")
            computer_wins+=1
        else:
            print("Humen Wins")
            player_wins+=1
    elif p1 =="scissor":
        if p2 =="rock":
            print("Computer wins")
            computer_wins+=1
        else:
            print("Humen Wins")
            player_wins+=1
    else:
        print("Someting went wrong")