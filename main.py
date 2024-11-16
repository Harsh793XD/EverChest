import cv2
import pyautogui
import time
import numpy as np

# Load the button image
button_image = cv2.imread('EQUIP.png', 0)  # Grayscale mode

# Define a function to detect and click the button
def detect_and_click_button():
    # Take a screenshot of the screen
    screen = pyautogui.screenshot()
    screen_gray = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2GRAY)

    # Match the button image in the screen
    result = cv2.matchTemplate(screen_gray, button_image, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Adjust threshold as needed

    # Get the coordinates of the detected area
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        # Calculate the center of the detected button
        button_x = max_loc[0] + button_image.shape[1] // 2
        button_y = max_loc[1] + button_image.shape[0] // 2

        # Click the button
        pyautogui.click(button_x, button_y)
        print("Button clicked!")
    else:
        print("Button not found on screen.")

# Loop to continuously check for the button
while True:
    detect_and_click_button()
    time.sleep(3)  # Adjust the interval as needed
