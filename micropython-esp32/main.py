from machine import Pin
import neopixel
import time

# Setting up NeoPixel matrix
neopixel_pin = Pin(18, Pin.OUT)
neopixel_n_cols = 8
neopixel_n_rows = 8
neopixel_matrix = neopixel.NeoPixel(
  neopixel_pin, neopixel_n_cols * neopixel_n_rows
)

rainbow_colours = [
  (255, 0, 0),    # red
  (255, 165, 0),  # orange
  (255, 255, 0),  # yellow
  (0, 255, 0),    # green
  (0, 0, 255),    # blue
  (75, 0, 130),   # indigo
  (128, 0, 255),  # violet
  (255, 192, 203) # pink
]
current_offset = 0

while True:
  # Rotate each column of pixels in the LED display through the colours
  i = 0
  while i < neopixel_n_cols * neopixel_n_rows:
    neopixel_matrix[i] = rainbow_colours[(i - current_offset) % neopixel_n_cols]
    i += 1

  neopixel_matrix.write()

  time.sleep(0.3)
  current_offset += 1