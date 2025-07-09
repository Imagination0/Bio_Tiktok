import chromedriver_autoinstaller
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

def update_tiktok_bio(new_bio):
    options = Options()
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

    options.add_argument(r"--user-data-dir=C:\Users\Lenovo\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--profile-directory=Profile 6")
    options.add_argument("--start-maximized")

    # FIX Chrome crash
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.tiktok.com/settings/profile")

    try:
        wait = WebDriverWait(driver, 30)
        textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, "textarea")))
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
