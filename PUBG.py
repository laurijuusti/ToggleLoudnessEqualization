import os
import time
import subprocess
import psutil

def toggle_loudness_eq(enable):
    try:
        # Path to registry key containing loudness equalization value (changes depending your audio device, mine begins with c17...)
        registry_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\MMDevices\Audio\Render\{c17ae955-087d-41c8-92f4-50c1cf4d896e}\FxProperties"
        registry_key = r"{fc52a749-4be9-4510-896e-966ba6525980},3"
        
        # Flip Loudness EQ bit on, or off
        value = "0b00000001000000ffff0000" if enable else "0b0000000100000000000000"
        
        # Command to set the registry value
        command = f'reg add "HKLM\\{registry_path}" /v "{registry_key}" /t REG_BINARY /d {value} /f'
        
        # Run the command
        subprocess.run(command, check=True, shell=True)
        print(f"Loudness Equalization {'enabled' if enable else 'disabled'}")
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")
        
def start_game():
    try:
        # Path to steam
        steam_path = r"C:\Program Files (x86)\Steam\steam.exe"
        
        # Command to launch PUBG
        steam_command = f'"{steam_path}" steam://rungameid/578080'
        
        # Start the game
        subprocess.Popen(steam_command, shell=True)
        print("Launching PUBG...")
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")

def is_game_running():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if "TslGame" in process.info['name']:
            return True
    return False

def main():
    try:
        toggle_loudness_eq(True)
        start_game()

        while True:
            time.sleep(30)  

            if not is_game_running():
                print("PUBG process not detected. Disabling Loudness Equalization...")
                toggle_loudness_eq(False)
                print("Loudness Equalization disabled. Exiting script.")
                break
    except Exception as e:
        print(f"Error in main script: {e}")
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()
