import random
import requests
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

def get_rate():
    try:
        response = requests.get("https://v6.exchangerate-api.com/v6/e4dfcc0635f10fd9d4e8805b/latest/USD", timeout=0.1)
        response.raise_for_status()
        data = response.json()
        rate = data["conversion_rates"]["ILS"]
        if rate > 0:
            return rate
    except requests.exceptions.RequestException:
        print("API service is unavailable")
    except (KeyError, TypeError):
        print("ILS is missing or invalid from the response")
    return None

def random_amount():
    amount = random.randint(1, 100)
    return amount

def usd_to_ils(amount, rate):
    rate = Decimal(str(rate))
    ils_amount = rate * amount
    ils_amount = ils_amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return ils_amount

def get_money_interval(difficulty, ils_amount):
    t = ils_amount
    d = difficulty
    lower = t - (5 - d)
    upper = t + (5 - d)
    return lower, upper

def get_guess_from_user(amount):
    while True:
        try:
            ils_guess = Decimal(input("Let see how lucky you are, this is the amount " + str(amount) + ". Now tell me what is the ILS? "))
            if ils_guess.is_finite() and ils_guess >= 0:
                return ils_guess
            else:
                print("Please enter non-negative number.")
        except InvalidOperation:
            print("Please enter number.")

def play(difficulty):
    rate = get_rate()
    if not rate:
        print("This round was cancelled, try again later.")
        return None
    amount = random_amount()
    ils_amount = usd_to_ils(amount, rate)
    lower, upper = get_money_interval(difficulty, ils_amount)
    ils_guess = get_guess_from_user(amount)
    win = lower <= ils_guess <= upper
    if win == True:
        return win 
    else:
        print("Aiiiii!! the correct answer is " + str(ils_amount) + "USD. The exchange rate today is " + str(rate))
        return False

#play(1)
#get_guess_from_user(31.5)
#print(usd_to_ils(10, 3.114561231565413213213))
#print(get_money_interval(2, usd_to_ils(10, 3.60)))
#print(usd_to_ils(10, 3.6))
#print(get_rate())