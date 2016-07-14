import random
"""We need to import this module in order for the computer to randomly choose from the given list"""
count=0
win=0
num_of_hr=0
num_of_hp=0
num_of_hs=0
"""the above statements initialize our counted variables"""

def computer_choice(r,p,s):
"""this function tells the computer what to play, depending on the previous input of the user"""    
    if r>p and r>s:
        computer="Paper"
    elif p>r and p>s:
        computer="Scissors"
    elif s>r and s>p:
        computer="Rock"
    else:
        computer=random.choice(["Rock","Paper","Scissors"])
    return computer

while True:
"""Unless the user chooses to quit, this loop will continue to run."""
    computer=computer_choice(num_of_hr,num_of_hp,num_of_hs)
    your_turn=raw_input("Your turn: ")

    if your_turn not in ["Rock","Paper","Scissors"]:
        if your_turn=="Quit":
            break
        else: print "Please try one of these: Rock, Paper, Scissors"
    
    elif your_turn=="Rock":
        num_of_hr+=1
        if computer=="Scissors":
            print "You win!"
            win+=1
        elif computer=="Paper":
            print "You lose"
        elif computer==your_turn:
            print "Draw"
    elif your_turn=="Paper":
        num_of_hp+=1
        if computer=="Rock":
            print "You win!"
            win+=1
        elif computer=="Scissors":
            print "You lose"
        elif computer==your_turn:
            print "Draw"
    elif your_turn=="Scissors":
        num_of_hs+=1
        if computer=="Paper":
            print "You win!"
            win+=1
        elif computer=="Rock":
            print "You lose"
        elif computer==your_turn:
            print "Draw"
    
    count+=1
print "Number of games played:", count
print "Number of human wins:", win
        