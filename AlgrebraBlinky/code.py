import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False)
count = 0
light1 = 4
light2 = 7

while True:

    if (count % light1 == 0):
        pixels[0] = (10, 0, 0)
    else:
        pixels[0] = (0,0,0)

    if (count % light2 == 0):
        pixels[1] = (10,0,0)
    else:
        pixels[1] = (0,0,0)



    pixels.show()
    time.sleep(1)
    count += 1
