# micropython script to get lux values from BH1750 sensor

import machine
import time
from bh1750 import BH1750

scl = machine.Pin(5)
sda = machine.Pin(4)
# for esp32 use machine.I2C(-1, scl=scl, sda=sda, freq=100000)
i2c = machine.I2C(scl=scl, sda=sda, freq=100000)

sensor = BH1750(i2c, 0x23)  # secondary address is 0x5c

try:
    while True:
        # get sensor light intensity (lux) and store value in variable 'lux'
        lux = sensor.luminance(BH1750.ONCE_HIRES_1)

        # print value to console.
        # {} is used in conjunction with format() for substitution.
        # .2f       - format to 2 decimal places.
        # end='\r'  - curser will go to the start of the current line instead of making a new line.
        print("Light intensity is {:.2f} lx".format(lux), end='\r')
        time.sleep(1)

except KeyboardInterrupt:
    print('script stopped by user')
finally:
    print('Goodbye!')
