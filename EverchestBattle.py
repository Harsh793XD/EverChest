import time
import pyautogui

def find_and_click_button(button_image, description):
    while True:
        try:
            button_location = pyautogui.locateCenterOnScreen(button_image, confidence=0.8)
            if button_location:
                print(f"{description} found at {button_location}, clicking...")
                pyautogui.click(button_location)
                return True  # Exit loop after clicking
            else:
                print(f"{description} not found. Retrying in 2 seconds...")
                time.sleep(3)
        except pyautogui.ImageNotFoundException:
            print("Image not found, retrying...")
            time.sleep(3)

def main():
    first_button_image = 'NEXT.png'
    second_button_image = 'BATTLE.png'

    while True:
        print("Waiting 20 seconds before searching for the first button...")
        time.sleep(20)
        
        if find_and_click_button(first_button_image, "First button"):
            print("Waiting 3 seconds before searching for the second button...")
            time.sleep(3)
            find_and_click_button(second_button_image, "Second button")

if __name__ == "__main__":
    main()
