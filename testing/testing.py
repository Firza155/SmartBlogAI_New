from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time
import random

# === Konfigurasi Akun Login ===
email = "yosionbesty@gmail.com"
password = "yosi1234"

# === Setup Faker ===
faker = Faker()
judul_artikel = faker.sentence(nb_words=5)
isi_artikel = faker.paragraph(nb_sentences=random.randint(3, 6))
new_title = faker.sentence(nb_words=5)
new_content = faker.paragraph(nb_sentences=4)

# === Laporan Testing ===
laporan = []

# === Inisialisasi Browser ===
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/login")
time.sleep(2)

try:
    # ==== LOGIN ====
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Log in')]").click()
    time.sleep(3)

    if "login" not in driver.current_url:
        laporan.append("✅ Login berhasil.")
    else:
        laporan.append("❌ Login gagal.")
        raise Exception("Login gagal, tidak bisa lanjut.")

    # ==== CREATE ARTIKEL ====
    driver.get("http://127.0.0.1:8000/articles")
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "+ Tambah Artikel").click()
    time.sleep(2)

    driver.find_element(By.NAME, "title").send_keys(judul_artikel)
    driver.find_element(By.NAME, "content").send_keys(isi_artikel)
    laporan.append(f"✅ Form artikel terisi. Judul: '{judul_artikel}'")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Simpan')]").click()
    time.sleep(3)

    # ==== LIHAT ARTIKEL ====
    driver.find_element(By.LINK_TEXT, "Lihat").click()
    time.sleep(2)

    title = driver.find_element(By.TAG_NAME, "h1").text
    body = driver.find_element(By.TAG_NAME, "p").text
    if title and body:
        laporan.append(f"✅ Artikel tampil. Judul: '{title}'")
    else:
        laporan.append("❌ Artikel kosong.")

    driver.find_element(By.LINK_TEXT, "← Kembali ke Daftar").click()
    time.sleep(2)

    # ==== EDIT ARTIKEL ====
    driver.find_elements(By.LINK_TEXT, "Edit")[0].click()
    time.sleep(2)

    title_input = driver.find_element(By.NAME, "title")
    title_input.clear()
    title_input.send_keys(new_title)

    content_input = driver.find_element(By.NAME, "content")
    content_input.clear()
    content_input.send_keys(new_content)

    laporan.append(f"✅ Artikel diedit. Judul baru: '{new_title}'")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Update')]").click()
    time.sleep(3)

    # ==== HAPUS ARTIKEL ====
    hapus_button = driver.find_element(By.XPATH, "//form//button[contains(text(), 'Hapus')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", hapus_button)
    time.sleep(1)
    hapus_button.click()
    time.sleep(1)

    try:
        alert = driver.switch_to.alert
        alert.accept()
        laporan.append("✅ Konfirmasi hapus diterima.")
    except:
        laporan.append("❌ Konfirmasi alert gagal.")

    time.sleep(3)
    laporan.append("✅ Artikel berhasil dihapus.")

except Exception as e:
    laporan.append("❌ Error: " + str(e))

finally:
    # Simpan hasil laporan ke file
    with open("laporan_test_full_artikel.txt", "w", encoding="utf-8") as f:
        for line in laporan:
            f.write(line + "\n")

    driver.quit()
    print("📝 Testing selesai. Laporan disimpan di 'laporan_test_full_artikel.txt'")
