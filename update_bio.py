from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Ganti dengan path ke profil Chrome kamu
PROFILE_DIR = r"C:\Users\aldi\AppData\Local\Google\Chrome\User Data"

def update_tiktok_bio(new_bio):
    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tiktok.com/settings/profile")
    time.sleep(10)

    try:
        textarea = driver.find_element(By.TAG_NAME, "textarea")
        textarea.clear()
        textarea.send_keys(new_bio)
        time.sleep(1)
        save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        save_button.click()
        print("Bio updated successfully")
    except Exception as e:
        print("Gagal update bio:", e)

    time.sleep(5)
    driver.quit()
