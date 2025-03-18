# iOSbuddy-1.0

iOSBuddy 1.0

🚀 Overview

iOSBuddy 1.0 is a Mac utility script designed to help users manage Screen Time settings, disable iCloud sync, reset the local Screen Time passcode, and retrieve lost Apple ID or Wi-Fi passwords. It provides a simple, automated way to regain control over your Mac’s restrictions and credentials.

⚠️ Disclaimer: This tool is for educational purposes only. The author is not responsible for misuse or any policy violations.

🎯 Features

✅ Checks if Screen Time is managed via iCloud Family Sharing✅ Disables iCloud sync for Screen Time✅ Removes the local Screen Time passcode✅ Recovers saved Wi-Fi passwords✅ Assists with Apple ID recovery steps✅ Cool ASCII animation when disabling Screen Time

📌 Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/iOSBuddy.git
cd iOSBuddy

2️⃣ Install Dependencies

pip3 install --user

🚀 Usage

To disable Screen Time and reset the passcode, simply run:

python3 iosbuddy.py

To retrieve a saved Wi-Fi password, run:

python3 iosbuddy.py --wifi "YourWiFiName"

To get Apple ID recovery options, run:

python3 iosbuddy.py --appleid

You will see an ASCII animation followed by the requested action being performed.

🛠 Troubleshooting

🔹 Screen Time doesn’t disable?Make sure you have admin access and run the script with sudo:

sudo python3 iosbuddy.py

🔹 iCloud keeps restoring settings?Make sure to restart your Mac after running the script to apply changes.

🔹 Wi-Fi password recovery not working?Ensure you are retrieving the password for a Wi-Fi network your Mac has connected to before.

⚖️ Legal Notice

This project is intended for personal use and educational purposes only. Modifying system settings without permission may violate Apple’s policies.

By using this software, you agree that you are solely responsible for how you use it.

⭐ Contributing

Feel free to fork the project, submit pull requests, or suggest improvements!

📜 License

MIT License – Free to use, modify, and distribute.

