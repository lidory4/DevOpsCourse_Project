import os


HERE = os.path.dirname(os.path.abspath(__file__))
SCORES_FILE_NAME = "Scores.txt"
SCORE_FILE_PATH = os.getenv("SCORES_FILE", os.path.join(HERE, "..", SCORES_FILE_NAME))
BAD_RETURN_CODE = -1 #failure, scroe can't be negative number

def Screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

