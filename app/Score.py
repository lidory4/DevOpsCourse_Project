import Utils


def add_score(difficulty):
    try:
        with open(Utils.SCORE_FILE_PATH, "r") as file:
            current_score = int(file.read())
            if current_score < 0:
                print("Negative number are not allowed in Scores.txt")
                return Utils.BAD_RETURN_CODE
    except FileNotFoundError:
        current_score = 0 
    except ValueError: #
        print("Scores.txt file is contain wrong value or corrupted")
        return Utils.BAD_RETURN_CODE
    except OSError:
        print("Cannot read Scores.txt")
        return Utils.BAD_RETURN_CODE
    POINTS_OF_WINNING = (difficulty * 3) + 5
    new_score = current_score + POINTS_OF_WINNING
    try:
        with open(Utils.SCORE_FILE_PATH, "w") as file:
            file.write(str(new_score))
    except OSError:
        print("New score failed")
        return Utils.BAD_RETURN_CODE
    return new_score

def read_score():
    try:
        with open(Utils.SCORE_FILE_PATH, "r") as file:
            current_score = int(file.read())
            if current_score < 0:
                return Utils.BAD_RETURN_CODE
    except FileNotFoundError:
        return Utils.BAD_RETURN_CODE   
    except OSError:
        return Utils.BAD_RETURN_CODE
    except ValueError:
        return Utils.BAD_RETURN_CODE
    return current_score