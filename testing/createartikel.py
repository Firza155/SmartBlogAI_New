from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import random

# ==== Konfigurasi akun login ====
email = "yosionbesty@gmail.com"
password = "yosi1234"

# ==== Setup faker untuk data random ====
faker = Faker()
judul_artikel = faker.sentence(nb_words=5)
isi_artikel = faker.paragraph(nb_sentences=random.randint(3, 6))

# ==== Setup Laporan ====
laporan = []

# ==== Mulai Selenium ====
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
        raise Exception("Login gagal, tidak dapat lanjut ke halaman articles.")

    # BUKA HALAMAN ARTICLES
    driver.get("http://127.0.0.1:8000/articles")
    time.sleep(2)

    if "articles" in driver.current_url:
        laporan.append("✅ Berhasil membuka halaman daftar artikel.")
    else:
        laporan.append("❌ Gagal membuka halaman daftar artikel.")
        raise Exception("Gagal membuka halaman daftar artikel.")

    # KLIK TOMBOL "+ Tambah Artikel"
    try:
        tambah_artikel_button = driver.find_element(By.LINK_TEXT, "+ Tambah Artikel")
        tambah_artikel_button.click()
        laporan.append("✅ Tombol '+ Tambah Artikel' berhasil diklik.")
    except:
        laporan.append("❌ Gagal menemukan tombol '+ Tambah Artikel'.")
        raise Exception("Tidak dapat melanjutkan ke halaman create.")

    time.sleep(2)

    # ISI FORM ARTIKEL DENGAN DATA RANDOM
    driver.find_element(By.NAME, "title").send_keys(judul_artikel)
    driver.find_element(By.NAME, "content").send_keys(isi_artikel)
    laporan.append(f"✅ Form artikel terisi. Judul: '{judul_artikel}', Isi: '{isi_artikel[:60]}...'")

    # SUBMIT ARTIKEL
    driver.find_element(By.XPATH, "//button[contains(text(), 'Simpan')]").click()
    time.sleep(3)

    # CEK REDIRECT
    if "articles" in driver.current_url and "create" not in driver.current_url:
        laporan.append("✅ Artikel berhasil disubmit dan redirect ke halaman index.")
    else:
        laporan.append("⚠️ Redirect setelah submit tidak sesuai harapan. Cek manual hasilnya.")

except Exception as e:
    laporan.append("❌ Terjadi kesalahan: " + str(e))

finally:
    # SIMPAN LAPORAN
    with open("laporan_create_artikel.txt", "w", encoding="utf-8") as file:
        for line in laporan:
            file.write(line + "\n")

    driver.quit()
    print("📝 Test selesai. Laporan disimpan di 'laporan_create_artikel.txt'")
