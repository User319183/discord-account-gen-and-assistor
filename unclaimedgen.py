import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string
import pyperclip
from modules.console import ConsoleX, LogLevel


DISCORD_URL = 'https://discord.com/'
OPEN_DISCORD_BUTTON_SELECTOR = 'button[data-testid="button-open-discord-in-browser"]'
DISPLAY_NAME_INPUT_SELECTOR = 'input[type="text"].username-1XgXmI'
ARROW_IMAGE_SELECTOR = 'img.arrow-1CLBFh'

def create_driver():
    options = uc.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    return uc.Chrome(options=options)

def open_discord(driver):
    driver.get(DISCORD_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, OPEN_DISCORD_BUTTON_SELECTOR))).click()

def enter_display_name(driver):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, DISPLAY_NAME_INPUT_SELECTOR))).send_keys(random_string)

def submit_display_name(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ARROW_IMAGE_SELECTOR))).click()

def main():
    console = ConsoleX()
    console.clear()
    driver = create_driver()
    if driver is None:
        return
    try:
        while True: # Loop to handle multiple instances
            open_discord(driver)
            console.log("Opened Discord", LogLevel.SUCCESS)
            enter_display_name(driver)
            console.log("Entered display name", LogLevel.SUCCESS)
            submit_display_name(driver)
            # Wait for user input
            user_input = input("Enter the number 1 for logging the token: ")
            if user_input == '1':
                js_script = """
                console.clear();
                let m = [];
                (webpackChunkdiscord_app.push([[''],{},e => {m=[];for(let c in e.c)m.push(e.c[c])}]),m);
                return m.find(m => m?.exports?.default?.getToken !== void 0).exports.default.getToken();
                """
                token = driver.execute_script(js_script)
                console.log(f"Token : {token}", LogLevel.SUCCESS)
                pyperclip.copy(token)
                console.log("Copied the token to clipboard", LogLevel.SUCCESS)
            driver.delete_all_cookies()
    except Exception as e:
        console.log(f"An error occurred: {e}", LogLevel.ERROR)
    finally:
        driver.quit()
        
if __name__ == "__main__":
    main()