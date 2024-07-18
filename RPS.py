# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[], play_order={}):
    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    if not opponent_history:
        prev_play = "R"
        opponent_history.append(prev_play)
    
    guess = "P"

    if len(opponent_history) > 6:
        last_seven = "".join(opponent_history[-7:])
        play_order[last_seven] = play_order.get(last_seven, 0) + 1

    potential_plays = [
        "".join(opponent_history[-6:]) + "R",
        "".join(opponent_history[-6:]) + "P",
        "".join(opponent_history[-6:]) + "S"
    ]

    sub_order = {
        k: play_order[k]
        for k in potential_plays if k in play_order
    }

    if sub_order:
        prediction = max(sub_order, key=sub_order.get)[-1:]
        guess = ideal_response[prediction]

    return guess
