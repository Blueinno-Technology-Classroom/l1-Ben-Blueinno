# go to https://www.classicgame.com/game/Whack+a+Mole

import time

import pyautogui as gui
from PIL import ImageGrab

gui.PAUSE = 0

# gui.displayMousePosition()

screenshot = ImageGrab.grab()
print(screenshot)

holes = [
    (285, 580),
    (404, 580),
    (522, 580),
    (285, 685),
    (404, 685),
    (522, 685),
    (285, 785),
    (404, 785),
    (522, 785),
]

start_time = time.time()
# time.sleep(5)
gui.click(490, 710)

while time.time() - start_time < 60:
    # print(65 - (time.time() - start_time))
    # time.sleep(1)

    mouseX, mouseY = gui.position()
    # mouseX -= 926
    # mouseY += 2160
    # print(mouseX, mouseY)
    screenshot = ImageGrab.grab()
    screenshot_data = screenshot.load()
    # print(screenshot_data[mouseX, mouseY])

    for hole in holes:
        x = hole[0]  # * 2
        y = hole[1]  # * 2
        r, g, b = screenshot_data[x, y]
        # print(r, g, b)
        if r < 200 and g < 200 and b < 200:
            continue
        else:
            gui.click(hole)
