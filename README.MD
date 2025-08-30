<div align="center">
📩 WhatsApp Bulk Sender
Automate personalized WhatsApp messages directly from your computer using Python & Selenium.
</div>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python Version">
<img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
<img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Status">
</p>
A simple yet powerful script to automate sending customized WhatsApp messages to a list of contacts from a CSV file. Perfect for sending reminders, notifications, or personalized greetings.
✨ Core Features
📲 Bulk Messaging: Send messages to an unlimited number of contacts.
📄 CSV Contact Management: Easily manage your contacts in a simple contacts.csv file.
✍️ Message Personalization: Use placeholders like {name} to create unique, personal messages.
🔐 Session Persistence: Scan the QR code only once. Your login session is saved for all future runs.
🚀 Lightweight & Simple: Minimal setup required to get you started in minutes.
🚀 Getting Started
Follow these steps to set up and run the project on your local machine.
📋 Prerequisites
Before you begin, ensure you have the following installed:
Python 3.10+
Google Chrome browser
A working WhatsApp account
⚙️ Installation
Clone the repository:
code
Bash
git clone https://github.com/your-username/whatsapp-bulk-sender.git
cd whatsapp-bulk-sender
Install the required libraries:
Create a file named requirements.txt with the content below:
code
Txt
pandas
selenium
webdriver-manager
Then, run this command in your terminal:
code
Bash
pip install -r requirements.txt
🛠️ How to Use
Step 1: Prepare Your Contact List
Open contacts.csv and add your contacts. The file must have two columns: Name and Number.
IMPORTANT: The phone number must include the country code without any +, -, or spaces.
Example contacts.csv:
code
Csv
Name,Number
Shafeek,919360220928
Sharuk,918110960489
Maria,34600123123
Step 2: Customize Your Message
Open the app.py script and edit the message_template variable. The {name} placeholder will be automatically replaced with the contact's name from your CSV file.
Example message_template:
code
Python
# Edit this line in app.py
message_template = "Hello {name}, this is a friendly reminder about our meeting tomorrow! 👋"
Step 3: Run the Script
Execute the script from your terminal:
code
Bash
python app.py
On your first run: A Chrome window will open. Scan the QR code with your phone to log in to WhatsApp Web.
On subsequent runs: The script will automatically use your saved session to log in.
The terminal will show the progress as each message is sent.
⚠️ Important Disclaimer
This project is intended for educational purposes only. Automating WhatsApp messaging can violate their Terms of Service. The developers of this project are not responsible for any consequences of its use, such as your account being blocked.
Use this tool responsibly and at your own risk.