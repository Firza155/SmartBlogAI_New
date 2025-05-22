from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
import time

# === Konfigurasi Akun ===
email = "yosionbesty@gmail.com"
password = "yosi1234"

# === Setup Faker untuk data random ===
faker = Faker()
new_title = faker.sentence(nb_words=5)
new_content = faker.paragraph(nb_sentences=4)

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
        raise Exception("Login gagal, tidak bisa lanjut ke halaman artikel.")

    # BUKA HALAMAN ARTICLES
    driver.get("http://127.0.0.1:8000/articles")
    time.sleep(2)

    if "articles" in driver.current_url:
        laporan.append("✅ Berhasil membuka halaman daftar artikel.")
    else:
        laporan.append("❌ Gagal membuka halaman daftar artikel.")
        raise Exception("Gagal membuka halaman daftar artikel.")

    # KLIK TOMBOL 'Edit' ARTIKEL PERTAMA
    edit_buttons = driver.find_elements(By.LINK_TEXT, "Edit")
    if edit_buttons:
        edit_buttons[0].click()
        laporan.append("✅ Tombol 'Edit' diklik.")
    else:
        laporan.append("❌ Tidak menemukan tombol 'Edit'.")
        raise Exception("Tidak ada artikel untuk diedit.")

    time.sleep(2)

    # VERIFIKASI HALAMAN EDIT
    if "articles" in driver.current_url and "edit" in driver.current_url:
        laporan.append("✅ Halaman edit artikel terbuka.")
    else:
        laporan.append("❌ Gagal membuka halaman edit artikel.")
        raise Exception("Gagal membuka halaman edit artikel.")

    # UBAH DATA JUDUL & ISI
    title_input = driver.find_element(By.NAME, "title")
    title_input.clear()
    title_input.send_keys(new_title)

    content_input = driver.find_element(By.NAME, "content")
    content_input.clear()
    content_input.send_keys(new_content)

    laporan.append(f"✅ Artikel diedit. Judul baru: '{new_title}', Isi baru: '{new_content[:60]}...'")

    # SUBMIT FORM
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Update')]")
    submit_button.click()
    time.sleep(3)

    # VERIFIKASI REDIRECT KE INDEX
    if "articles" in driver.current_url and "edit" not in driver.current_url:
        laporan.append("✅ Redirect berhasil ke daftar artikel setelah update.")
    else:
        laporan.append("⚠️ Redirect tidak sesuai setelah update. Periksa hasilnya.")

except Exception as e:
    laporan.append("❌ Terjadi error: " + str(e))

finally:
    # SIMPAN LAPORAN
    with open("laporan_edit_artikel.txt", "w", encoding="utf-8") as file:
        for line in laporan:
            file.write(line + "\n")

    driver.quit()
    print("📝 Test selesai. Laporan disimpan di 'laporan_edit_artikel.txt'")
