import Utils


def add_score(difficulty):
    try:
        with open(Utils.SCORES_FILE_NAME, "r") as file:
            current_score = int(file.read())
            if current_score < 0:
                print("Negative number are not allowed in Scores.txt")
                return Utils.BAD_RETURN_CODE
    except FileNotFoundError:
        current_score = 0 
    except ValueError:
        print("Scores.txt file is contain wrong value or corrupted")
        return Utils.BAD_RETURN_CODE
    except OSError:
        print("Cannot read Scores.txt")
        return Utils.BAD_RETURN_CODE
    POINTS_OF_WINNING = (difficulty * 3) + 5
    new_score = current_score + POINTS_OF_WINNING
    try:
        with open(Utils.SCORES_FILE_NAME, "w") as file:
            file.write(str(new_score))
    except OSError:
        print("New score failed")
        return Utils.BAD_RETURN_CODE
    return new_score
