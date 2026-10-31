import Live
import MemoryGame
import GuessGame
import CurrencyRouletteGame

name = input("Please write your nickname\n")
hello = Live.welcome(name)
print(hello)

#Run the game menu
game, difficulty = Live.load_game() 
#Run games
if game == 1:
    result = MemoryGame.play(difficulty)
elif game == 2:
    result = GuessGame.play(difficulty)
elif game == 3:
    result = CurrencyRouletteGame.play(difficulty)
if result:
    print("Winner")
elif result is None:
    pass
else:
    print("Loser")
