from pynput import keyboard
import pyautogui

click_coordinates = {
    '1': (710, 750),
    '2': (795, 750),
    '3': (890, 750),
    '4': (970, 750),
}

def perform_click(x, y):
    current_x, current_y = pyautogui.position()
    pyautogui.click(x, y)
    pyautogui.moveTo(current_x, current_y)

def on_key_press(key):
    try:
        key = key.char  # Try to get the character corresponding to the key
        if key in click_coordinates:
            x, y = click_coordinates[key]
            perform_click(x, y)
    except AttributeError:
        pass

print("Starting...")
# Create a keyboard listener
with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
