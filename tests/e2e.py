import selenium
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import sys


def test_scores_service(URL):
    driver = selenium.webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(URL)
    if driver.find_elements(By.ID, 'score'):
        score_element = driver.find_element(By.ID, 'score')
        score = int(score_element.text)
        if 0 <= score <= 1000:
            return True
        else:
            return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    URL = sys.argv[1]
    if test_scores_service(URL):
        sys.exit(0)

    sys.exit(-1)
