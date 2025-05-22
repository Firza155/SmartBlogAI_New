from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# === Konfigurasi akun login ===
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
        raise Exception("Login gagal, tidak bisa lanjut ke halaman articles.")

    # BUKA HALAMAN ARTICLES
    driver.get("http://127.0.0.1:8000/articles")
    time.sleep(2)

    if "articles" in driver.current_url:
        laporan.append("✅ Berhasil membuka halaman daftar artikel.")
    else:
        laporan.append("❌ Gagal membuka halaman daftar artikel.")
        raise Exception("Gagal membuka halaman daftar artikel.")

    # KLIK TOMBOL 'Lihat' PADA ARTIKEL PERTAMA
    lihat_buttons = driver.find_elements(By.LINK_TEXT, "Lihat")
    if lihat_buttons:
        lihat_buttons[0].click()
        laporan.append("✅ Tombol 'Lihat' diklik.")
    else:
        laporan.append("❌ Tidak menemukan tombol 'Lihat'.")
        raise Exception("Tidak ada artikel untuk dilihat.")

    time.sleep(2)

    # VERIFIKASI HALAMAN ARTIKEL TAMPIL
    title = driver.find_element(By.TAG_NAME, "h1").text
    body = driver.find_element(By.TAG_NAME, "p").text
    if title and body:
        laporan.append(f"✅ Artikel tampil. Judul: '{title}'")
    else:
        laporan.append("❌ Judul atau isi artikel kosong.")

    # KLIK LINK 'Kembali ke Daftar'
    back_link = driver.find_element(By.LINK_TEXT, "← Kembali ke Daftar")
    back_link.click()
    time.sleep(2)

    # VERIFIKASI KEMBALI KE HALAMAN ARTICLES
    if "articles" in driver.current_url and "create" not in driver.current_url:
        laporan.append("✅ Berhasil kembali ke daftar artikel.")
    else:
        laporan.append("❌ Gagal kembali ke daftar artikel.")

except Exception as e:
    laporan.append("❌ Terjadi error: " + str(e))

finally:
    # SIMPAN LAPORAN
    with open("laporan_lihat_kembali_artikel.txt", "w", encoding="utf-8") as file:
        for line in laporan:
            file.write(line + "\n")

    driver.quit()
    print("📝 Test selesai. Laporan disimpan di 'laporan_lihat_kembali_artikel.txt'")
