def welcome(name):
    return "Hello "+name+" and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"

def load_game():
    while True:
        try:
            game = int(input("""Please choose a game to play:
1. Memory Game - Memorize the sequence in 0.7 seconds, Blink and you lose.
2. Guess Game - Guess the secret number, Remember the House always wins.
3. Currency Roulette - Guess how many shekels a random USD amount is worth, Your bank is watching.
"""))
            if game <= 3 and game > 0:
                break
            print("Choose number between 1-3")
        except ValueError:
            print("Please enter whole number")
    if game == 1:
        print("Great you choose Memory Game now lets see how good you are\n")
    elif game == 2:
        print("Great you choose Guess Game now lets see how good you are\n")
    elif game == 3:
        print("Great you choose Currency Roulette now lets see how good you are\n")
    while True:
        try:
            difficulty = int(input("""Please choose game difficulty from noob to world class:
1.Noob - Not judging
2.Good -Comci Comsa
3.Pro - Lets start
4.Legendery - Mannn!!
5.WorlClass - Dont wast my time
"""))
            if difficulty <= 5 and difficulty > 0:
                return game, difficulty
            print("Choose number between 1-5")
        except ValueError:
            print("Please enter whole number")
