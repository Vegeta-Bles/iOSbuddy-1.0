import subprocess
import argparse
import time

def startup_graphic():
    """Displays a cool startup animation with ASCII art."""
    frames = [
        "\033[1;34m[🔹] Initializing...\033[0m",
        "\033[1;36m[🔹🔹] Loading Modules...\033[0m",
        "\033[1;32m[🔹🔹🔹] Disabling Screen Time...\033[0m"
    ]
    for frame in frames:
        print(frame)
        time.sleep(1)
    
    # ASCII animation of Screen Time splitting
    split_animation = [
        "\033[1;35m  ⏳   \033[0m",
        "\033[1;35m ⏳    \033[0m",
        "\033[1;35m⏳     \033[0m",
        "\033[1;35m ⏳    \033[0m",
        "\033[1;35m  ⏳   \033[0m",
        "\033[1;31m💀 SCREEN TIME DISABLED! 💀\033[0m"
    ]
    for line in split_animation:
        print(line)
        time.sleep(0.5)

def get_wifi_password(wifi_name):
    """Retrieve the saved Wi-Fi password for a given network."""
    try:
        command = f"security find-generic-password -ga '{wifi_name}' 2>&1 | grep 'password:'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if "password:" in result.stdout:
            print(f"✅ Wi-Fi Password for {wifi_name}: {result.stdout.split('"')[1]}")
        else:
            print(f"❌ Could not retrieve the password for {wifi_name}.")
    except Exception as e:
        print(f"Error: {e}")

def recover_mac_passcode():
    """Attempts to retrieve Mac user account passwords if stored in Keychain."""
    try:
        print("🔍 Searching for saved Mac login passwords...")
        command = "security find-generic-password -ga 'Mac Login' 2>&1 | grep 'password:'"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        if "password:" in result.stdout:
            print(f"✅ Found Password: {result.stdout.split('"')[1]}")
        else:
            print("❌ Could not retrieve the Mac login password. Try macOS Recovery Mode.")
    except Exception as e:
        print(f"Error: {e}")

def reset_screen_time_passcode():
    """Attempts to reset the Screen Time passcode by identifying and deleting its database (Admin required)."""
    try:
        print("Screen Time passcode reset attempt in progress...")
        startup_graphic()  # Run animation only if resetting Screen Time
        possible_files = [
            "/Library/Application Support/com.apple.ScreenTime.plist",
            "/private/var/folders/.../com.apple.ScreenTime.plist",  # Example path; user must check actual result
        ]
        for file in possible_files:
            if os.path.exists(file):
                print(f"Deleting: {file}")
                command = ["sudo", "rm", "-f", file]
                subprocess.run(command, capture_output=True, text=True)
        print("Screen Time passcode reset attempt completed. Restart your Mac for changes to take effect.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("\nWelcome to iOSBuddy 1.0 - Choose an option:")
    print("1️⃣ Disable Screen Time")
    print("2️⃣ Recover Wi-Fi Password")
    print("3️⃣ Recover Mac Login Passcode")
    print("4️⃣ Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    
    if choice == "1":
        reset_screen_time_passcode()
    elif choice == "2":
        wifi_name = input("Enter the Wi-Fi network name: ")
        get_wifi_password(wifi_name)
    elif choice == "3":
        recover_mac_passcode()
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid option, please try again.")

if __name__ == "__main__":
    main()