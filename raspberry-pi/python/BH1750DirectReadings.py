#!/usr/bin/python
import time
import smbus

# Define some constants from the datasheet

DEVICE     = 0x23   # Default device I2C address
                    # 0x5C alternative address

POWER_DOWN = 0x00   # No active state
POWER_ON   = 0x01   # Power on
RESET      = 0x07   # Reset data register value

# Continuous modes
CONTINUOUS_LOW_RES_MODE    = 0x13  # 4lx resolution. Time typically 16ms.
CONTINUOUS_HIGH_RES_MODE_1 = 0x10  # 1lx resolution. Time typically 120ms.
CONTINUOUS_HIGH_RES_MODE_2 = 0x11  # 0.5lx resolution. Time typically 120ms.

# One shot modes. Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE    = 0x23  # 4lx resolution. Time typically 16ms.
ONE_TIME_HIGH_RES_MODE_1 = 0x20  # 1lx resolution. Time typically 120ms.
ONE_TIME_HIGH_RES_MODE_2 = 0x21  # 0.5lx resolution. Time typically 120ms


# bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)   # Rev 2 Pi uses 1


def convert_to_number(data):
    '''Simple function to convert 2 bytes of data into a decimal number.'''
    return data[1] + (256 * data[0])


def read_light(addr=DEVICE):
    '''Read data from I2C interface'''
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    return convert_to_number(data) / 1.2  # for mode 2 need to divide again by 2


def main():
    '''run to loop reading'''
    while True:
        print("Light Level : {:.2f} lx    ".format(read_light(0x5C)), end='\r')
        time.sleep(0.5)


if __name__ == "__main__":
    main()
