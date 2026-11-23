import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_scores_service(application_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") 
    browser = None
    try:
        browser = webdriver.Chrome(options=options)
        browser.get(application_url)
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.presence_of_element_located((By.ID, "score")))
        text = element.text.strip()
        if not text.isdigit():
            print("Not a whole number: " + text)
            return False
        score = int(text)
        if score < 1 or score > 1000:
            print("Out of range: " + text)
            return False
        return True
    except Exception as error:
        print("Test failed: " + str(error))
        return False
    finally:
        if browser is not None:
            browser.quit()

def main_function():
    url = "http://localhost:8777"
    if test_scores_service(url):
        print("Passed")
        sys.exit(0)
    else:
        print("Failed")
        sys.exit(-1)

main_function()