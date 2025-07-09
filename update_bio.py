from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROFILE_DIR = r"C:\Users\\aldi\\AppData\\Local\\Google\\Chrome\\User Data"

def update_tiktok_bio(new_bio):
    options = Options()
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_argument("--start-maximized")
    # NON-HEADLESS agar kamu bisa lihat
    # Jangan pakai --headless saat debugging

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tiktok.com/settings/profile")

    print("Tunggu browser terbuka... Login manual jika belum login.")

    try:
        # Tunggu sampai user login dan halaman benar-benar muncul
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )

        textarea = driver.find_element(By.TAG_NAME, "textarea")
        textarea.clear()
        textarea.send_keys(new_bio)

        time.sleep(2)
        save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        save_button.click()

        print("✅ Bio berhasil diperbarui!")

    except Exception as e:
        print("❌ Gagal update bio:", e)

    time.sleep(5)
    driver.quit()
