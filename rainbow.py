from modules import ws2812
from fpioa_manager import *
import time

# Initialize WS2812 LED
fm.register(8)
class_ws2812 = ws2812(8, 100)

# Define rainbow colors
rainbow_colors = [
    (255, 0, 0),     # Red
    (255, 127, 0),   # Orange
    (255, 255, 0),   # Yellow
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (75, 0, 130),    # Indigo
    (148, 0, 211)    # Violet
]

# Initialize variables
index = 0

while True:
    current_color = rainbow_colors[index]
    next_index = (index + 1) % len(rainbow_colors)
    next_color = rainbow_colors[next_index]

    # Gradually transition from current color to next color
    for i in range(100):
        r = int(current_color[0] + (next_color[0] - current_color[0]) * i / 100)
        g = int(current_color[1] + (next_color[1] - current_color[1]) * i / 100)
        b = int(current_color[2] + (next_color[2] - current_color[2]) * i / 100)

        for j in range(100):
            class_ws2812.set_led(j, (r, g, b))

        class_ws2812.display()
        time.sleep(0.02)  # Adjust the delay to change the speed of color transition

    index = next_index
