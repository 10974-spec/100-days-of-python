import random

def roll():  # Changed from play_game() to roll()
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (1-4): ") 
    if players.isdigit():
        players = int(players)
        if 1 <= players <= 4:
            break
        else:
            print("Must be between 1 and 4 players.")

max_score = 50
player_scores = [0 for _ in range(players)]     

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()  # Now this will work
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("You have accumulated:", current_score, "points")
        
        player_scores[player_idx] += current_score
        print("Your total score is now:", player_scores[player_idx], "points")

# After the game ends
winning_score = max(player_scores)
winning_player = player_scores.index(winning_score) + 1
print(f"\nPlayer {winning_player} wins with a score of {winning_score}!")