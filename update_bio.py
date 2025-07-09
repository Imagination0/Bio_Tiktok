from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def update_tiktok_bio(new_bio):
    options = Options()

    # 1. Path ke folder "User Data" Chrome kamu (bukan folder Profile-nya)
    options.add_argument(r"--user-data-dir=C:\Users\aldi\AppData\Local\Google\Chrome\User Data")

    # 2. Tentukan profile-directory (bukan Default, kalau kamu pakai yang lain)
    options.add_argument("--profile-directory=Profile 6")  # Ganti sesuai hasil dari chrome://version

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
        print("✅ Bio berhasil diperbarui!")

    except Exception as e:
        print("❌ Gagal update bio:", e)

    time.sleep(5)
    driver.quit()
