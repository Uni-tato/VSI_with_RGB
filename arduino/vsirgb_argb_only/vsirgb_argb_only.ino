#include <FastLED.h>

#define BAUDRATE 9600 // Make sure this matches the rate in the 'config.py' file.

#define DATA_PIN_1  3
#define LED_TYPE    WS2811
#define COLOUR_ORDER GRB
#define NUM_LEDS    8
CRGB leds[NUM_LEDS];

void wait_for_serial(){
  while (not Serial.available()) {
    delay(10);
  }
}

void setup() {

  // Tell FastLED about the leds used.
  FastLED.addLeds<LED_TYPE, DATA_PIN_1, COLOUR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalLEDStrip);
  
  Serial.begin(BAUDRATE);
  while (!Serial){
    delay(10); // wait for the decices to connect.
  }

  pinMode(DATA_PIN_1, OUTPUT);

}

void loop() {
  if (Serial.available()){
    // Recieved data from the device, update leds.

    // Read the colour values from serial.
    byte R = Serial.read();
    wait_for_serial();
    byte G = Serial.read();
    wait_for_serial();
    byte B = Serial.read();

    // Send this colour to the rgb device.
    for (int i = 0; i < NUM_LEDS; i++){
      leds[i] = CRGB(R,G,B);
      FastLED.show();
      delay(50);
    }
  }

  delay(1000);
}
