import numpy as np
import pyautogui as pg
import easyocr, keyboard, mouse, cv2, time, random

reader = easyocr.Reader(["en"])

def find_shake_rect(img, resize_factor = 0.4):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    thresh = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)[1]
    dilated = cv2.dilate(thresh, np.ones((3,3),np.uint8))
    resized = cv2.resize(dilated, None, fx=resize_factor, fy=resize_factor, interpolation=cv2.INTER_AREA)

    ocr_results = reader.readtext(resized)

    found = list(filter(lambda v: v[1].lower().strip() == "shake", ocr_results))
    if len(found) == 0:
        cv2.imwrite(f"errors/error{random.random()}.png", resized)
        return None
    
    coords = np.rint(np.array(found[0][0]) * (1/resize_factor)).astype(int)
    return (coords[0], coords[2])

def on_activate():
    screenshot = np.array(pg.screenshot())
    result = find_shake_rect(screenshot)
    if not result:
        print("Could not find shake!")
        return

    point = (result[0] + result[1]) / 2
    time.sleep(0.01)
    mouse.move(*point)
    time.sleep(0.01)
    mouse.click()
    mouse.click()

print("Fischer ready!")

keyboard.add_hotkey("f1", on_activate)
keyboard.wait()
