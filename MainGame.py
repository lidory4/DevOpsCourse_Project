import Live
import GuessGame

name = input("Please write your nickname\n")
hello = Live.welcome(name)
print(hello)

#Run the game menu
game, difficulty = Live.load_game() 
#Run GuessGame
if game == 2:
    result = GuessGame.play(difficulty)

if result:
    print("Winner")
else:
    print("Loser")
