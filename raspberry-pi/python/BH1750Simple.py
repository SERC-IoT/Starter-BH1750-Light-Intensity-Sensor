# simple script to get lux values from BH1750 sensor

import time

import bh1750

try:
    import smbus2 as smbus
except ImportError:
    import smbus

# create i2c bus object. usually bus 1.
bus = smbus.SMBus(1)

# create sensor object. default address is 0x23. secondary address is 0x5C
sensor = bh1750.BH1750(bus, addr=0x23)

try:
    print("Reading lux values from sensor. Press Ctrl-C to exit")
    print("")
    print("Sensitivity: {:d}".format(sensor.mtreg))

    while True:
        print("Light level: {:3.2f} lx  ".format(sensor.measure_high_res()), end='\r')
        time.sleep(1)

except KeyboardInterrupt:
    print('script stopped by user')
finally:
    bus.close()
    print('Goodbye!')
