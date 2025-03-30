import pyperclip
import keyboard
import pyautogui
from deep_translator import GoogleTranslator

def translate_clipboard_text():
    # Simulate Ctrl+C to copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    
    # Wait a moment to ensure the clipboard has been updated
    pyautogui.sleep(1)  # Increase the sleep time to make sure clipboard gets updated

    # Get the text from clipboard
    clipboard_text = pyperclip.paste()

    # Check if the clipboard is empty (no text was copied)
    if clipboard_text:
        # Translate the text from Russian to English using deep-translator
        translated = GoogleTranslator(source='auto', target='en').translate(clipboard_text)

        # Copy translated text back to clipboard
        pyperclip.copy(translated)
        print(f"Translated Text: {translated}")

        # Simulate Ctrl+V to paste the translated text
        pyautogui.hotkey('ctrl', 'v')
    else:
        print("No text was copied to the clipboard!")

# Set up the hotkey (Ctrl+Insert)
keyboard.add_hotkey('ctrl+insert', translate_clipboard_text)

print("Press Ctrl+Insert to translate selected text and paste it...")
keyboard.wait()  # Keeps the program running indefinitely
