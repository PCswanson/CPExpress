import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False) #define neopixels

count = 0
light1 = 4


while True:

    pixels[9] = (0,0,255) # turn pixel 9 (the timer pixel) blue

    # check to see if light1 is a multiple of count
    if (count % light1 == 0):
        pixels[0] = (10, 0, 0)
    else:
        pixels[0] = (0,0,0)


    pixels.show() # show pixels

    time.sleep(.5) #sleep for .5 seconds

    pixels[9] = (0,0,0) #turn timer pixel off
    pixels.show()

    time.sleep(.5)
    count += 1 #add 1 to the count
