import pyautogui
import time

# --- CONFIGURATION ---
MESSAGE = "k"
REPEATS = 50
DELAY_BETWEEN_MESSAGES = 0.6  # Seconds to wait between each text
PRE_START_DELAY = 5           # Seconds you have to switch windows
# ---------------------

# 1. FAIL-SAFE: Move mouse to any corner of the screen to kill the script!
pyautogui.FAILSAFE = True

print(f"Starting in {PRE_START_DELAY} seconds...")

# 2. COUNTDOWN: This helps you track time visually
for i in range(PRE_START_DELAY, 0, -1):
    print(f"{i}...")
    time.sleep(1)

print("Go!")

# 3. THE LOOP: This does the heavy lifting
try:
    for n in range(1, REPEATS + 1):
        pyautogui.press('enter')
        
        # Small pause so the chat app doesn't suspect a DDoS attack
        time.sleep(DELAY_BETWEEN_MESSAGES)

    print("Done! Sent all messages.")

except pyautogui.FailSafeException:
    print("\nFail-safe triggered! Script stopped manually.")
