import os
from pynput import keyboard
import pyautogui
import time

# Directory to save screenshots
save_dir = r"C:\sshots"

# Create the directory if it doesn't exist
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Counter for screenshot numbering
screenshot_count = 1

def on_press(key):
    global screenshot_count
    
    if key == keyboard.Key.print_screen:
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        
        # Generate the filename
        filename = f"shot{screenshot_count}.png"
        filepath = os.path.join(save_dir, filename)
        
        # Save the screenshot
        screenshot.save(filepath)
        
        print(f"Screenshot saved: {filepath}")
        
        # Increment the counter
        screenshot_count += 1
        
        # Small delay to prevent multiple captures for a single press
        time.sleep(0.1)

# Set up the listener
with keyboard.Listener(on_press=on_press) as listener:
    print("Screenshot program is running. Press 'Print Screen' to take a screenshot.")
    print("Press Ctrl+C to exit.")
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\nProgram terminated.")