import random 

def play():
    user = input("What's your choice? rock(r), paper(p) or scissor(s)\n")
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "It's a tie"
    if is_Win(user, computer):
        return "You win!"
    return "You Lost!"


def is_Win(player, computer):
    if (player == "r" and computer == "s") or (player == "p" and computer == "r") or (player == "s" and computer == "p"):
        return True
    
while True:
    print(play())
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != 'Y':
        break
