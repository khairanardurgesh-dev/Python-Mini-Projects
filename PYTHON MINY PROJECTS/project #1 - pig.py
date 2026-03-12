import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    
    return roll

while True:    
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
          print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):                        
        print("\nPlayer number", player_idx + 1, "turn has just started")
        print("your total score is:", players_scores[player_idx], "\n")
        current_score = 0

        while True:      
            if current_score == 0:
                choice = input("Do you want to roll? (y/n): ")
                if choice.lower() != 'y':
                    print("You must roll at least once.")
                    continue
            else:
                choice = input("Do you want to roll again? (y/n): ")
                if choice.lower() != 'y':
                    break   
            roll_result = roll()
            print("You rolled a", roll_result)                                                                                           
            if roll_result == 1:
                print("You rolled a 1! Your turn is over and you lose all points for this turn.")
                current_score = 0
                break
            else:
                current_score += roll_result
                print("Your current score for this turn is:", current_score)
        players_scores[player_idx] += current_score
        print("Your total score is now:", players_scores[player_idx])
        if players_scores[player_idx] >= max_score:
            print("\nCongratulations! Player number", player_idx + 1, "wins with a score of", players_scores[player_idx], "!")
            break
        
