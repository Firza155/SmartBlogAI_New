from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# === Konfigurasi Akun ===
email = "yosionbesty@gmail.com"
password = "yosi1234"

# === Setup Laporan ===
laporan = []

# === Mulai Selenium ===
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/login")
time.sleep(2)

try:
    # LOGIN
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    time.sleep(3)

    if "login" not in driver.current_url:
        laporan.append("✅ Login berhasil.")
    else:
        laporan.append("❌ Login gagal.")
        raise Exception("Login gagal, tidak dapat lanjut ke halaman daftar artikel.")

    # BUKA HALAMAN DAFTAR ARTIKEL
    driver.get("http://127.0.0.1:8000/articles")
    time.sleep(2)

    if "articles" in driver.current_url:
        laporan.append("✅ Berhasil membuka halaman daftar artikel.")
    else:
        laporan.append("❌ Gagal membuka halaman daftar artikel.")
        raise Exception("Gagal membuka halaman daftar artikel.")

    # TEMUKAN TOMBOL 'Hapus' DENGAN CLASS SPESIFIK
    try:
        hapus_button = driver.find_element(By.XPATH, "//form//button[contains(text(), 'Hapus')]")
        driver.execute_script("arguments[0].scrollIntoView(true);", hapus_button)
        time.sleep(1)
        hapus_button.click()
        laporan.append("✅ Tombol 'Hapus' diklik.")
    except Exception as e:
        laporan.append("❌ Tidak dapat menemukan tombol 'Hapus'.")
        raise Exception("Tombol 'Hapus' tidak ditemukan: " + str(e))

    # TANGANI KONFIRMASI ALERT
    time.sleep(1)
    try:
        alert = driver.switch_to.alert
        alert.accept()
        laporan.append("✅ Konfirmasi alert diterima.")
    except Exception as e:
        laporan.append("❌ Gagal menangani alert konfirmasi: " + str(e))
        raise Exception("Alert konfirmasi tidak muncul atau gagal di-handle.")

    # Tunggu penghapusan selesai
    time.sleep(3)

    if "articles" in driver.current_url:
        laporan.append("✅ Setelah hapus, redirect ke halaman daftar artikel berhasil.")
    else:
        laporan.append("⚠️ Redirect setelah hapus tidak sesuai harapan. URL saat ini: " + driver.current_url)

except Exception as e:
    laporan.append("❌ Terjadi error: " + str(e))

finally:
    # SIMPAN LAPORAN
    with open("laporan_hapus_artikel.txt", "w", encoding="utf-8") as file:
        for line in laporan:
            file.write(line + "\n")

    driver.quit()
    print("📝 Test selesai. Laporan disimpan di 'laporan_hapus_artikel.txt'")
