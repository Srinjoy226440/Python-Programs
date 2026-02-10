import pyautogui
import time

print("Let's go")

time.sleep(5) # Give yourself time to position the mouse
pyautogui.click() # Clicks the box to make it 'active'

for i in range(20):
    # Typing with an interval makes it look human to Instagram
    pyautogui.typewrite("Hello Tanvi", interval=0.1) 
    time.sleep(0.5)
    pyautogui.press('enter') 
    time.sleep(1) # Wait for the message to actually send
