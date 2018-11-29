# A Python replica of Keno Heads or Tails
from random import randint

def game():
    heads = list() # Represents the items in heads
    tails = list() # Represents the items in tails
    output = 0 # Item to be added to one of the lists
    min = 1 # Minimum number generated
    max = 80 # Maximum number generated

    for round in range(0, 20):
        while True: # Generate a number that isn't in heads or tails
            output = randint(min, max)
            if not (output in heads or output in tails):
                min = 1
                max = 80
                break

            # A bit of a bias system to prevent evens from being called as much
            minimum = 9
            if (len(heads) >= minimum or len(tails) >= minimum):
                if (len(heads) > len(tails)): # Force a heads number
                    min = 1
                    max = 40
                elif (len(heads) < len(tails)): # Force a tails number
                    min = 41
                    max = 80

        if (output <= 40): # Add the output to the corresponding list
            heads.append(output)
        else:
            tails.append(output)

        if (11 in (len(heads), len(tails))):
            break # If one of the sides reaches 11, end the game

    heads.sort() # Sort the list items
    tails.sort()
    print("Heads:", heads) # Display the items of each list
    print("Tails:", tails)

    if (len(heads) > len(tails)): # Print out the winner
        print("Heads wins!")
        return "heads"
    elif (len(heads) < len(tails)):
        print("Tails wins!")
        return "tails"
    else:
        print("Evens!")
        return "evens"

def multiple_games_test(games):
    heads = tails = evens = 0

    for i in range(0, games):
        round = game()
        if (round == "heads"):
            heads += 1
        elif (round == "tails"):
            tails += 1
        else:
            evens += 1

    print("\nIn", games, "games:")
    print("Heads won", heads, "times, Tails won", tails, "times, and Evens won", evens, "times.")

debug = False # Change to true to see a wide spectrum of results
if (debug):
    multiple_games_test(100)
else:
    game()
