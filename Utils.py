import os


SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1 #failure, scroe can't be negative number

def Screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

