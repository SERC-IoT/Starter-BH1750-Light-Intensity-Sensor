# Setup for MKR WiFi 1010 dev board

Setup instructions for an Arduino MKR WiFi 1010 development board.

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/mkr-bh1750-sensor-circuit-diagram_schem.png)

#### Components Needed
* BH1750 sensor breakout board
* connecting wires
* MKR WiFi 1010 development board

<br />

![breadboard diagram](assets/mkr-bh1750-sensor-circuit-diagram_bb.png)

<br />

### Default Pin Wiring

| Pin No | Function |  | Device Connection |
| --- | --- | --- | --- |
|  |  |  |  |
| VCC | +3.3V |  | Vdd |
| GND | GND |  | GND |
| 11 | SDA |  | SDA |
| 12 | SCL |  | SCL |
|  |  |  |  |

![pin diagram](assets/Pinout-MKRwifi1010_latest.png)

<br>

## Arduino

Drivers and board details need to be installed to use the Arduino MKR series. Follow the instructions here: https://www.arduino.cc/en/Guide/MKRWiFi1010#toc2

The arduino sketches require the BH1750 library. It is included in the root additional-libraries folder. Afternatively, it can be downloaded through the Arduino libraries manager or from https://github.com/claws/BH1750.
