lst = ['xx','Rock','Paper','Scissors']
def displayOptions():
    print("""
            Select anyone by number
            1. Rock
            2. Papers
            3. Scissors """)
def RPSGame2P(p1,p2):
    if p1 == p2:
        print("Its a Tie")
        return
    if p1 == 'Rock':
        if p2 == 'Scissors':
            print(f'{Player1} wins the match'.format(Player1))
            return
        else:
            print(f'{Player2} wins the match'.format(Player2))
            return
    if p1 == 'Scissors':
        if p2 == 'Paper':
            print(f'{Player1} wins the match'.format(Player1))
            return
        else:
            print(f'{Player2} wins the match'.format(Player2))
            return
    if p1 == 'Paper':
        if p2 == 'Rock':
            print(f'{Player1} wins the match'.format(Player1))
            return
        else:
            print(f'{Player2} wins the match'.format(Player2))
            return
def RPSGame1P(my_choice,python_choice):
    if my_choice == "Rock" and (python_choice == "Scissors"):
        print("Win")
        return 
    elif my_choice == "Scissors" and (python_choice == "Paper"):
        print("Win")
        return
    elif my_choice == "Paper" and (python_choice == "Rock"):
        print("Win")
        return
    elif my_choice == python_choice:
        print("Draw")
        return
    else:
        print("Lose")
        return
noOfPlayers = int(input("""
1. One Player
2. Two Player """))
if noOfPlayers == 1:
    displayOptions()
    my_choice = int(input())
    python_choice = int(input())
    RPSGame1P(lst[my_choice],lst[python_choice])
elif noOfPlayers == 2:
    Player1 = input("Enter Player Name1")
    Player2 = input("Enter Player Name2")
    displayOptions()
    p1 = int(input(f'{Player1}! Select Anyone '))
    p2 = int(input(f'{Player2}! Select Anyone '))
    RPSGame2P(lst[p1],lst[p2])
else:
    print("Invalid Input")
