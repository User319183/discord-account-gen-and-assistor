import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.console import ConsoleX, LogLevel
import random
import string
import pyperclip
import secrets
from faker import Faker

# DISCORD
DISCORD_URL = 'https://discord.com/register'
EMAIL_INPUT_SELECTOR = 'input[name="email"]'
DISPLAY_NAME_INPUT_SELECTOR = 'input[name="global_name"]'
USERNAME_INPUT_SELECTOR = 'input[name="username"]'
PASSWORD_INPUT_SELECTOR = 'input[name="password"]'
MONTHS = ['january','february','march','april','may','june','july','august','september','october', 'november','december']

# HCAPTCHA
ARROW_IMAGE_SELECTOR = 'img.arrow-1CLBFh'
HCAPTCHA_IFRAME_SELECTOR = 'iframe[src*="hcaptcha.com"]'
CHECKMARK_SELECTOR = 'div#checkbox'

# Create a Faker instance
fake = Faker()

def generate_realistic_name():
    return fake.name().replace(' ', random.choice(['_', '.']))

def generateDOB():
    year = str(random.randint(1997,2001))
    month = MONTHS[random.randint(0,11)]
    day = str(random.randint(1,28))
    return f"{year}-{month}-{day}"

def create_driver():
    options = uc.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
    return uc.Chrome(options=options)

def set_input_value(driver, css_selector, value):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )
    element.clear()
    element.send_keys(value)
    
def switch_to_hcaptcha_iframe(driver):
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, HCAPTCHA_IFRAME_SELECTOR)))

def click_checkmark(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, CHECKMARK_SELECTOR))).click()
    
def switch_back_from_iframe(driver):
    driver.switch_to.default_content()

# Add a setting for realistic names
realistic_names = True

def main():
    console = ConsoleX()
    console.clear()
    console.log("Starting the main function", LogLevel.INFO)
    while True: # Loop to create multiple instances
        driver = create_driver()
        try:
            console.log("Opening Discord URL", LogLevel.INFO)
            driver.get(DISCORD_URL)
            DisplayAndUsernameAndEmail = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            console.log(f"Generated Display & Username: {DisplayAndUsernameAndEmail}", LogLevel.SUCCESS)
            pyperclip.copy(DisplayAndUsernameAndEmail)
            email = f"{DisplayAndUsernameAndEmail}@supenc.com"
            password = secrets.token_hex(10)
            console.log("Entering email", LogLevel.INFO)
            set_input_value(driver, EMAIL_INPUT_SELECTOR, email)
            console.log(f"Email: {email}", LogLevel.SUCCESS)
            
            if realistic_names:
                console.log("The realistic names setting is enabled", LogLevel.INFO)
                display_name = generate_realistic_name()
                username = generate_realistic_name()
            else:
                console.log("The realistic names setting is disabled", LogLevel.INFO)
                display_name = "fuckedbyuser319183"
                username = f"fuckedbyuser319183_{DisplayAndUsernameAndEmail}"

            console.log("Entering display name", LogLevel.INFO)
            set_input_value(driver, DISPLAY_NAME_INPUT_SELECTOR, display_name)
            console.log(f"Display Name: {display_name}", LogLevel.SUCCESS)

            console.log("Entering username", LogLevel.INFO)
            set_input_value(driver, USERNAME_INPUT_SELECTOR, username)
            console.log(f"Username: {username}", LogLevel.SUCCESS)
            
            password = f"generatedbyuser319183_{password}"
            console.log("Entering password", LogLevel.INFO)
            set_input_value(driver, PASSWORD_INPUT_SELECTOR, password)
            console.log(f"Password: {password}", LogLevel.SUCCESS)
            
            dob = generateDOB()
            year, month, day = dob.split('-')

            set_input_value(driver, '[id="react-select-2-input"]', month)
            set_input_value(driver, '[id="react-select-3-input"]', day)
            set_input_value(driver, '[id="react-select-4-input"]', year)
            
            try:
                tos_checkbox = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[type='checkbox']"))
                )
                tos_checkbox.click()
            except Exception as e:
                console.log("No TOS Checkbox was detected", LogLevel.DEBUG)

            submit_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[type="submit"]'))
            )
            submit_button.click()
            
            console.log("Submitted the form", LogLevel.SUCCESS)
            switch_to_hcaptcha_iframe(driver)
            console.log("Switched to hCaptcha iframe", LogLevel.SUCCESS)
            click_checkmark(driver)
            console.log("Clicked the checkmark", LogLevel.SUCCESS)
            switch_back_from_iframe(driver)
            console.log("Switched back from iframe", LogLevel.SUCCESS)

            user_input = console.input("Enter the number 1 for logging the token: ")
            if user_input == '1':
                console.log("Executing JS script to get token", LogLevel.INFO)
                js_script = """
                console.clear();
                let m = [];
                (webpackChunkdiscord_app.push([[''],{},e => {m=[];for(let c in e.c)m.push(e.c[c])}]),m);
                return m.find(m => m?.exports?.default?.getToken !== void 0).exports.default.getToken();
                """
                token = driver.execute_script(js_script)
                console.log(f"Token : {token}", LogLevel.SUCCESS)
                pyperclip.copy(f"{email}:{password}:{token}") # email:password:token
                console.log("Copied the email, password, and token to clipboard", LogLevel.SUCCESS)
        except Exception as e:
            console.log(f"An error occurred: {e}", LogLevel.ERROR)
        finally:
            try:
                console.log("Closing the driver", LogLevel.INFO)
                driver.quit()
            except Exception as e:
                console.log(f"An error occurred while closing the driver: {e}", LogLevel.ERROR)
            console.log("Finished the main function", LogLevel.INFO)

        user_input = console.input("Press enter to create another instance, waiting for user to change IP/VPN. Type 'exit' to exit: ")
        if user_input == 'exit':
            break
        
        
if __name__ == "__main__":
    main()
