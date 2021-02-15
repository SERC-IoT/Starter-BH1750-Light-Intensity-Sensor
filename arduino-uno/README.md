# Arduino Uno and BH1750 Light Intensity Sensor

![Arduino Sketch Checks](https://github.com/SERC-IoT/Starter-BH1750-Light-Intensity-Sensor/workflows/Arduino%20Sketch%20Checks/badge.svg)

Setup instructions and starter code for using the BH1750 light intensity sensor and an Arduino development board.

<br />

## Files and Folders

| File/Folder | Description |
|--- | --- |
| [arduino/](arduino/) | Arduino projects folder |
| [arduino/bh1750-lux-sensor/bh1750-lux-sensor.ino](arduino/bh1750-lux-sensor/bh1750-lux-sensor.ino) | Simple arduino sketch. |
| [mkr-wifi-1010-setup.md](mkr-wifi-1010-setup.md) | Setup instructions for using an Arduino MKR WiFi 1010 dev board. |
|  |  |

<br />

## Setup

Setup instructions for an Arduino Uno board is below. For MKR WiFi 1010 based setup instructions see [mkr-wifi-1010-setup.md](mkr-wifi-1010-setup.md).

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/uno-bh1750-sensor-circuit-diagram_schem.svg)

#### Components Needed
* BH1750 sensor breakout board
* connecting wires
* arduino uno development board

<br />

![breadboard diagram](assets/uno-bh1750-sensor-circuit-diagram_bb.png)

<br />

### Default Pin Wiring

| Pin No | Function | Device Connection |
| --- | --- | --- |
| 5V | +5V | Vdd |
| GND | GND | GND |
| 18 | SDA |  | SDA |
| 19 | SCL |  | SCL |
|  |  |  |

![pin diagram](assets/Pinout-UNOrev3_latest.png)

<br />

## Arduino

The sketch will work with many different types and chipset of board. To use an Arduino Uno, make sure to select the correct board in Boards Manager.

The arduino sketches require the BH1750 library. It is included in the root additional-libraries folder. Afternatively, it can be downloaded through the Arduino libraries manager or from https://github.com/claws/BH1750.

## References

- https://www.arduino.cc/en/reference/board
- https://github.com/claws/BH1750
