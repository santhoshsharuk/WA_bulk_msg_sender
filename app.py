import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# === Chrome Options ===
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("user-data-dir=C:\\Users\\user\\selenium-profile")  # Keeps login

# === Start Chrome ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com")
print("⚡ Scan the QR code (only first time). Waiting for WhatsApp Web to load...")
time.sleep(20)  # give time to scan QR

# === Load CSV ===
# CSV Format: Name,Number
data = pd.read_csv("contacts.csv")

# === Message Template ===
# You can write: "Hello {name}, this is a test message!"
message_template = "Hello {name}, this is an automated message from Z3 Connect 🚀"

for index, row in data.iterrows():
    name = str(row['Name'])
    number = str(row['Number'])

    # Personalize message
    message = message_template.format(name=name)

    print(f"📤 Sending to {name} ({number})...")

    # Open chat directly via wa.me link
    driver.get(f"https://web.whatsapp.com/send?phone={number}&text={message}")
    time.sleep(10)  # wait for chat to load

    try:
        # Find and click send button
        send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send']")
        send_button.click()
        print(f"✅ Message sent to {name}")
    except Exception as e:
        print(f"❌ Failed to send to {name}: {e}")

    time.sleep(5)  # delay between messages

print("🎉 All messages sent!")
driver.quit()
