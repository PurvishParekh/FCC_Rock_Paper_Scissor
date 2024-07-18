# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_play, opponent_history=[], play_order={}):
    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # chain_length = 2

    # markov_chain = { '': {move: 0 for move in ("R", "P", "S")} }

    # def update_chain(history):
    #     if len(opponent_history) >= chain_length:
    #         key = "".join(history[-chain_length:])
    #         if key:  # Check if key is not empty string
    #             if key not in markov_chain:
    #                 markov_chain[key] = {move: 0 for move in ("R", "P", "S")}
    #             next_move = opponent_history[-1]
    #             markov_chain[key][next_move] += 1

    # if len(opponent_history) >= chain_length:
    #     update_chain(opponent_history)
    
    # def predict_next_move():
    #     most_frequent_key = max(markov_chain, key=lambda key: sum(markov_chain[key].values()))
    #     probs = markov_chain[most_frequent_key]
    #     return max(probs, key=probs.get)

    # if markov_chain:
    #     predict_move = predict_next_move()
    #     return ideal_response[predict_move]

    # return random.choice(('R', 'P', 'S'))


    # guess = "P"
    # guess_history=[]
    # guess_history.append(guess)

    # # Track opponent's last 4 moves
    # last_four_moves = opponent_history[-4:]

    # # Initialize probabilities for each move (Rock, Paper, Scissors)
    # probs = {'R': 0.33, 'P': 0.33, 'S': 0.33}
    # ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    # moves = ("R", "P", "S")
    # # Decoy throw (20% chance)
    # if random.random() < 0.2:
    #     probs[random.choice(moves)] += 0.95  # Increase probability of random move

    # # Update probabilities based on patterns (you can add more patterns here)
    # if len(last_four_moves) >= 3:
    #     # If opponent played the same move 3 times in a row, favor the counter move
    #     if last_four_moves[-3:] == last_four_moves[-1]:
    #         probs[ideal_response[last_four_moves[-1]]] += 0.2

    # if (guess_history[-1]=="P" and opponent_history[-1]=="R"):
    #     probs["P"] += 0.95

    # if (guess_history[-1]=="P" and opponent_history[-1]=="S"):
    #     probs[opponent_history[-2]] += 0.95

    # if (guess_history[-1]=="P" and opponent_history[-1]=="P"):
    #     probs["S"] += 0.95  # R R IS BETTER
    #     if ( opponent_history[-1] and opponent_history[-2]) == "P":
    #        probs["R"] += 0.95    #TRY S R

    # # Track opponent's last 10 moves (for Mrugesh)
    # last_ten_moves = opponent_history[-10:]
    

    # # Update probabilities based on patterns (you can add more patterns here)
    # if len(last_ten_moves) >= 3:
    #     # Exploit Kris (always throws counter)
    #     # probs[ideal_response[guess_history[-1]]] += 0.5  # Favor move that beats Kris' counter

    #     # Play a mix of moves against Mrugesh
    #     move_counts = {move: last_ten_moves.count(move) for move in moves}
    #     least_frequent_move = max(move_counts, key=move_counts.get)
    #     if random.random() < 0.7:  # Randomness first (70% chance)
    #         probs[random.choice(moves)] += 0.5  # Slightly favor random move
    #     else:
    #         probs[least_frequent_move] += 0.9  # Favor least frequent move (after randomness)
    

    # # mrugesh
    # # last_ten = guess_history[-10:]
    # # most_frequent = max(set(last_ten), key=last_ten.count)
    # # if not most_frequent == '':
    # #     probs[ideal_response[ideal_response[most_frequent]]] += 0.5


    # # kris
    # # probs[ideal_response[ideal_response[guess_history[-1]]]] += 0.2

    # # Normalize probabilities to add up to 1
    # total_prob = sum(probs.values())
    # for move in probs:
    #     probs[move] /= total_prob

    # # Choose a move based on the probability distribution
    # guess = random.choices(list(probs.keys()), weights=list(probs.values()))[0]
    # guess_history.append(guess)
    # return guess





    
    # guess = "P"
    
    # moves = ("R", "P", "S")

    
            
    # if len(opponent_history) >= 2:
    #     if (guess_history[-1]=="R" and opponent_history[-1]=="P"):
    #         guess = opponent_history[-2] #
    #         # if random.random() < 0.2:
    #         #     guess = "P"

    #     if (guess_history[-1]=="P" and opponent_history[-1]=="R"):
    #         guess = "P" # ONLY P
    #         # if random.random() < 0.2:
    #         #     guess = random.choice(["P", "S"]) # WORKS BUT ONLY SOMETIMES

    #     if (guess_history[-1]=="P" and opponent_history[-1]=="S"):
    #         guess = opponent_history[-2]
    #         # if random.random() < 0.25: #0.003 MIGHT WORK WITH SOME ADJUSTMENTS
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="S" and opponent_history[-1]=="P"):
    #         guess = "S" #
    #         # if random.random() < 0.25:
    #         #     guess = random.choice(["P", "R"])

    #     if (guess_history[-1]=="S" and opponent_history[-1]=="R"):
    #         guess = opponent_history[-2] #
    #         # if random.random() < 0.2:
    #         #     guess = random.choice(["R", "P"])

    #     if (guess_history[-1]=="R" and opponent_history[-1]=="S"):
    #         guess = "R" #
    #         # if random.random() < 0.1:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="P" and opponent_history[-1]=="P"):
    #         guess = "S"  # R R IS BETTER
    #         if ( opponent_history[-1] and opponent_history[-2]) == "P":
    #             guess = "R"    #TRY S R
    #         #     if random.random() < 0.1:
    #         #         guess = random.choice(moves)
    #         # if random.random() < 0.25:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="R" and opponent_history[-1]=="R"):
    #         guess = "S"  #
    #         if (opponent_history[-1] and opponent_history[-2]) == "R":
    #             guess = "P"  # P IS BETTER
    #         #     if random.random() < 0.1:
    #         #         guess = random.choice(moves)
    #         # if random.random() < 0.1:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="S" and opponent_history[-1]=="S"):
    #         guess = "S"
    #         if (opponent_history[-1] and opponent_history[-2]) == "S":
    #             guess = "R" #
    #         #     if random.random() < 0.1:
    #         #         guess = random.choice(moves)
    #         # if random.random() < 0.1:
    #         #     guess = random.choice(moves)
        
        
    # else :
    #     guess = random.choice(["P", "S"])

    
    
    # if len(guess_history) > 1:
    #     last_two = "".join(guess_history[-2:])
    #     play_order[0][last_two] += 1
        
        
    #     potential_plays = [
    #         guess_history[-1] + "R",
    #         guess_history[-1] + "P",
    #         guess_history[-1] + "S",
    #     ]

    #     sub_order = {
    #         k: play_order[0][k]
    #         for k in potential_plays if k in play_order[0]
    #     }
    #     # print(play_order)
    #     prediction = max(sub_order, key=sub_order.get)[-1:]

    #     ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    #     if random.random() < 0.1:
    #         guess = ideal_response[ideal_response[prediction]]    
    
    # guess_history.append(guess)
    
    # return guess

    
    # guess_history = ["P","P"]
    # guess = "P"
    # guess_history.append(guess)
    # moves = ("R", "P", "S")

    # if len(guess_history_new) > 1:
    #     last_two = "".join(guess_history_new[-2:])
    #     if len(last_two) == 2:
    #         play_order[0][last_two] += 1
        
        
    #     potential_plays = [
    #         guess_history_new[-1] + "R",
    #         guess_history_new[-1] + "P",
    #         guess_history_new[-1] + "S",
    #     ]

    #     sub_order = {
    #         k: play_order[0][k]
    #         for k in potential_plays if k in play_order[0]
    #     }
    #     # print(sub_order)
    #     # print(max(sub_order,key=sub_order.get))
    #     prediction = max(sub_order, key=sub_order.get)[-1:]

    #     ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    #     # if random.random() < 0.1:
    #     #     guess = ideal_response[ideal_response[prediction]]

    # if len(opponent_history) > 2:
    #     if (guess_history[-1]=="R" and opponent_history[-1]=="P"):
    #         guess = "S" #
    #         # if opponent_history[-1] == "P" and opponent_history[-2] == "P":
    #         #     if random.random() < 0.3:
    #         #         guess = "R"
    #         # if opponent_history[-1] == "P" and opponent_history[-2] == "R":
    #         #     if random.random() < 0.3:
    #         #         guess = "S"
    #         # if random.random() < 0.00001:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="P" and opponent_history[-1]=="R"):
    #         guess = "P" # ONLY P
    #         # if random.random() < 0.1:
    #         #     guess = "R"
    #         # if random.random() < 0.1:
    #         #     guess = random.choice(move) # WORKS BUT ONLY SOMETIMES

    #     if (guess_history[-1]=="P" and opponent_history[-1]=="S"):
    #         guess = opponent_history[-2] # R MIGHT WORK
    #         # if random.random() < 0.1:
    #         #     guess = "R"
    #         # if random.random() < 0.0025: #0.003 MIGHT WORK WITH SOME ADJUSTMENTS
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="S" and opponent_history[-1]=="P"):
    #         guess = "S" #
    #         # if random.random() < 0.2:
    #         #     guess = "P"
    #         # if opponent_history[-1] == "P" and opponent_history[-2] == "P":
    #         #     if random.random() < 0.2:
    #         #         guess = "R"
    #         # if random.random() < 0.25:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="S" and opponent_history[-1]=="R"):
    #         guess = "S" #
    #         # if random.random() < 0.3:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="R" and opponent_history[-1]=="S"):
    #         guess = "R" #
    #         # if random.random() < 0.1:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="P" and opponent_history[-1]=="P"):
    #         guess = "R"  # R R IS BETTER
    #         if ( opponent_history[-1] and opponent_history[-2]) == "P":
    #             guess = "S" #TRY S R
    #             if random.random() < 0.8:
    #                 guess = ideal_response[ideal_response[prediction]]
    #         #     if random.random() < 0.0001:
    #         #         guess = random.choice(moves)
    #         # if random.random() < 0.0025:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="R" and opponent_history[-1]=="R"):
    #         guess = "S" #
    #         if (opponent_history[-1] and opponent_history[-2]) == "R":
    #             guess = "S" # P IS BETTER # Neccessary for QUINCY
    #         #     if random.random() < 0.0001:
    #         #         guess = random.choice(moves)
    #         # if random.random() < 0.0001:
    #         #     guess = random.choice(moves)

    #     if (guess_history[-1]=="S" and opponent_history[-1]=="S"):
    #         guess = "S"
    #         if (opponent_history[-1] and opponent_history[-2]) == "S":
    #             guess = "R" #
    #         #     if random.random() < 0.0001:
    #         #         guess = random.choice(moves)
    #         # if random.random() < 0.1:
    #         #     guess = random.choice(moves)
    # else :
    #     guess = "P"

    # guess_history.append(guess)

     

    # guess_history_new.append(guess)
    
    # return guess


    # guess = "P"
    # i = random.choice([1,1,1,1,2,2,3,4])

    # if ( i == 1 ): # abby
    #     if len(guess_history_new) > 1:
    #         last_two = "".join(guess_history_new[-2:])
    #         if len(last_two) == 2:
    #             play_order[0][last_two] += 1
            
            
    #         potential_plays = [
    #             guess_history_new[-1] + "R",
    #             guess_history_new[-1] + "P",
    #             guess_history_new[-1] + "S",
    #         ]

    #         sub_order = {
    #             k: play_order[0][k]
    #             for k in potential_plays if k in play_order[0]
    #         }
    #         # print(sub_order)
    #         # print(max(sub_order,key=sub_order.get))
    #         prediction = max(sub_order, key=sub_order.get)[-1:]

    #         ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    #         if random.random() < 0.6:
    #             guess = ideal_response[ideal_response[prediction]] 

        

    # elif ( i == 2 ): # kriss
    #     if len(guess_history_new) > 1:
    #         guess = ideal_response[guess_history_new[-1]]

    # elif ( i == 3 ): # mrugesh
    #     if len(guess_history_new) > 10:
    #         last_ten = guess_history_new[-10:]
    #         most_frequent = max(set(last_ten), key=last_ten.count)

    #         if most_frequent == '':
    #             most_frequent = "S"

    #         guess = ideal_response[ideal_response[most_frequent]]

    # elif ( i == 4 ): # quincy
        
    #     choices = ["R", "R", "P", "P", "S"]
    #     guess = ideal_response[choices[counter[0] % len(choices)]]

    # else:
    #     guess = random.choice(["P","R","S"])

    # counter[0] += 1
    # guess_history_new.append(guess)
    # return guess


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