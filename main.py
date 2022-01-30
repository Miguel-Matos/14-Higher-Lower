import art
import game_data
import random

def game():

    def item_generator():
        chosen_number = random.randint(0, len(game_data.data) - 1)
        return chosen_number
    item_selector_a = item_generator()
    item_selector_b = item_generator()
    score = 0
    game_over = False

    while game_over == False:
        print(art.logo)
        if score > 0:
            print(f"Correct! Your score is: {score}")
        print(f'Compare A: {game_data.data[item_selector_a] ["name"]}, a {game_data.data[item_selector_a] ["description"]}, from {game_data.data[item_selector_a] ["country"]}')
        print(art.vs)
        print(f'Against B: {game_data.data[item_selector_b] ["name"]}, a {game_data.data[item_selector_b] ["description"]}, from {game_data.data[item_selector_b] ["country"]}')

        player_guess = input("Who has more followers? A or B: ").upper()
        if player_guess == "A":
            if game_data.data[item_selector_a]["follower_count"] > game_data.data[item_selector_b]["follower_count"]:
                    item_selector_a = item_generator()
                    item_selector_b = item_generator()
                    score += 1
                   
            elif game_data.data[item_selector_a]["follower_count"] < game_data.data[item_selector_b]["follower_count"]:
                    game_over = True
        elif player_guess == "B":
            if game_data.data[item_selector_b]["follower_count"] > game_data.data[item_selector_a]["follower_count"]:
                    item_selector_a = item_generator()
                    item_selector_b = item_generator()
                    score += 1
            elif game_data.data[item_selector_b]["follower_count"] < game_data.data[item_selector_a]["follower_count"]:
                    game_over = True
    endgame = input(f"Game Over! Your final score is {score}! Do you want to play again? Y or N: ").lower()
    if endgame == "y":
        game()
game()