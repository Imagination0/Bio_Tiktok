from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def update_tiktok_bio(new_bio):
    print("🔧 Menghubungkan ke Chrome remote debugging...")

    options = Options()
    options.debugger_address = "127.0.0.1:9222"

    driver = webdriver.Chrome(options=options)
    print("🌐 Navigasi ke halaman TikTok...")

    driver.get("https://www.tiktok.com/settings/profile")

    try:
        wait = WebDriverWait(driver, 30)
        textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
        textarea.clear()
        textarea.send_keys(new_bio)
        print("✍️ Bio diisi...")

        save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
        save_button.click()
        print("💾 Bio disimpan.")
    except Exception as e:
        print("❌ Terjadi error:", e)

    time.sleep(5)
    driver.quit()
