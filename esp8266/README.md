# ESP8266 and BH1750 Light Intensity Sensor

![MicroPython Checks](https://github.com/SERC-IoT/Starter-BH1750-Light-Intensity-Sensor/workflows/MicroPython%20Checks/badge.svg) ![Pylint score](../../../blob/badges/.github/badges/micropythonpylint.svg)

Code for getting started with a BH1750 light insensity sensor and a ESP8266 microcontroller.

<br />

## Files and Folders

| File/Folder | Description |
|--- | --- |
| [arduino/](../arduino-uno/arduino) | For Arduino, use the sketches in the Arduino Uno folder [../arduino-uno/arduino](../arduino-uno/arduino) |
| [micropython/](micropython/) | folder for micropython scripts. Pymakr is configured to sync this folder with the micropython device. |
| [micropython/light_readings.py](micropython/light_readings.py) | micropython script that reads the light lux values and prints them to the repl. |
| [esp32-setup.md](esp32-setup.md) | Setup instructions for using an ESP32 dev board. |
| [esp8266-micropython-setup.ps1](esp8266-micropython-setup.ps1) | PowerShell script to install MicroPython on ESP8266 device and upload scripts. |
|  |  |

<br />

## Setup

Setup instructions for a WeMos D1 mini are below. For ESP32 based setup instructions see [esp32-setup.md](esp32-setup.md).

## Circuit Diagram

Wire the components as shown in the diagram.

![circuit diagram](assets/esp8266-bh1750-lux-sensor-circuit-diagram_schem.svg)

#### Components Needed

* BH1750 sensor
* connecting wires
* esp8266 device

<br />

![breadboard diagram](assets/esp8266-bh1750-lux-sensor-circuit-diagram_bb.png)

<br />

### Default Pin Wiring

| Pin No | Function |  | Device Connection |
| --- | --- | --- | --- |
|  |  |  |  |
| 1 | +3.3V |  | Vdd |
| 6 | GND |  | GND |
| D2 | GPIO4 |  | SDA |
| D1 | GPIO5 |  | SCL |
|  |  |  |  |

![pin diagram](assets/wemos-d1-mini-pinout.png)

Further details and other board pin out diagrams can be found here: https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/

<br />

## Arduino

The sketch will work with many different types and chipset of board. To use an ESP8266 board with Arduino IDE, you will need to install the relevant board configuration files. Follow the instructions here: https://arduino-esp8266.readthedocs.io/en/latest/installing.html

The arduino sketches require the BH1750 library. It is included in the root additional-libraries folder. Afternatively, it can be downloaded through the Arduino libraries manager or from https://github.com/claws/BH1750.

<br />

## MicroPython

The MicroPython script uses a module from https://github.com/PinkInk/upylib/tree/master/bh1750. It is included in the [micropython/lib](micropython/lib) folder.

### Uploading Files

Test files can be uploaded using [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy).

```pwsh
PS> ampy --port <COM port of device> --baud 115200 put micropython/light_readings.py
PS> ampy --port <COM port of device> --baud 115200 put micropython/lib
```

A PowerShell script ([esp8266-micropython-setup.ps1](esp8266-micropython-setup.ps1)) is also included to automatically setup MicroPython on an ESP8266 device.

```pwsh
PS> .\esp8266-micropython-setup.ps1
```

<br />

## References

- https://randomnerdtutorials.com/esp8266-pinout-reference-gpios/
- https://github.com/claws/BH1750
- https://github.com/PinkInk/upylib/tree/master/bh1750
