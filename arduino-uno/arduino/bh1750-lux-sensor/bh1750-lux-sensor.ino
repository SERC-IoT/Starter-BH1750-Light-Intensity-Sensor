/*
 * Sketch that reads light intensity (lux) from a BH1750 sensor, and prints the reading to the serial console.
 */

// include the libraries we need
#include <Wire.h>
#include <BH1750.h>

// create sensor object
// primary address is 0x23. alternative address is 0x5C.
BH1750 lightMeter(0x23);
 
void setup() {
  Serial.begin(9600);

  // Initialize the I2C bus (BH1750 library doesn't do this automatically)
  // For esp8266 or esp32 can specify I2C pins as such: Wire.begin(SCL pin, SDA pin);
  Wire.begin();

  // wait until serial port opens
  while (! Serial) {
    delay(1);
  }

  // check sensor starts correctly
  if (lightMeter.begin(BH1750::CONTINUOUS_HIGH_RES_MODE)) {
    Serial.println(F("BH1750 Sensor Readings"));
  }
  else {
    Serial.println(F("Error initialising BH1750"));
  }
}

void loop() {
  // read light level from sensor if ready
  if (lightMeter.measurementReady()) {
    float lux = lightMeter.readLightLevel();
    Serial.print("Light: ");
    Serial.print(lux);
    Serial.println(" lx");
  }
  delay(1000);
}
