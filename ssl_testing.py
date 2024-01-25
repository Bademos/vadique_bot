from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager





URL = 'https://www.avito.ru/moskva/bytovaya_elektronika'
PAUSE_DURATION_SECONDS = 5


def main():
    driver.get(URL)
    sleep(PAUSE_DURATION_SECONDS)


if __name__ == '__main__':
    try:
        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        main()
    except Exception as e:
        print(e)
    finally:
        driver.quit()