import Utils


def add_score(difficulty):
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
    except FileNotFoundError:
        current_score = 0 

    POINTS_OF_WINNING = (difficulty * 3) + 5
    new_score = current_score + POINTS_OF_WINNING

    with open(Utils.SCORES_FILE_NAME, "w") as file:
        file.write(str(new_score))
