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
x = random.randint(0,2)
if x == 0:
    p2 = "rock"
elif x ==1:
    p2= "paper"
else:
    p2="scissor"
print("Your welcome to my Rock Scissor Paper game")
p1 = input(" Humen player  enter your choice : ").lower()
print ( "Computer Moved " + p2 )
if p1 == p2 :
    print("Tie")
elif p1 =="rock":
    if p2 =="paper":
        print("Computer wins")
    else:
        print("Humen Wins")
elif p1 =="paper":
    if p2 =="scissor":
        print("Computer wins")
    else:
        print("Humen Wins")
elif p1 =="scissor":
    if p2 =="rock":
        print("Computer wins")
    else:
        print("Humen Wins")
else:
    print("Someting went wrong")