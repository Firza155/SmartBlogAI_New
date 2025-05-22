from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup Chrome driver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/login")
time.sleep(2)

# Data akun login
test_email = "yosionbesty@gmail.com"
test_password = "yosi1234"
laporan = []

try:
    # Isi form login
    driver.find_element(By.ID, "email").send_keys(test_email)
    laporan.append("✅ Email field filled.")

    driver.find_element(By.ID, "password").send_keys(test_password)
    laporan.append("✅ Password field filled.")

    try:
        driver.find_element(By.ID, "remember_me").click()
        laporan.append("✅ 'Remember me' clicked.")
    except:
        laporan.append("⚠️ Checkbox 'Remember me' tidak ditemukan.")

    # Klik tombol Login
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    laporan.append("✅ Login button clicked.")
    time.sleep(3)

    # Langsung menuju halaman articles
    driver.get("http://127.0.0.1:8000/articles")
    time.sleep(2)

    if "articles" in driver.current_url:
        laporan.append("✅ Langsung diarahkan ke halaman /articles.")
    else:
        laporan.append("⚠️ Gagal membuka halaman /articles.")

except Exception as e:
    laporan.append("❌ Error: " + str(e))

# Simpan laporan dengan UTF-8
with open("laporan_login_to_articles.txt", "w", encoding="utf-8") as file:
    for line in laporan:
        file.write(line + "\n")

driver.quit()
print("📝 Test selesai. Laporan tersimpan.")
