//#include <Adafruit_TLC59711.h> // 12-Channel driver
#include <Adafruit_TLC5947.h> // 24-Channel driver
// If your driver boards are not compatible with these libraries then you'll need use something else.
// Please share any modifications you think others might like here: https://github.com/Uni-tato/VSI_with_RGB

// Make sure this matches the rate in the 'config.py' file.
#define BAUDRATE 9600
#define DELAY_TIME 5000
#define DATA_LENGTH_LIMIT 512
#define RGB_COUNT 3

#define LED_DRIVER_CHAIN_LENGTH 1
#define DATA_PIN 4
#define CLOCK_PIN 5
#define LATCH_PIN 6
#define OE_PIN -1

#define color colour

//Adafruit_TLC5711 tlc = Adafruit_TLC5711(LED_DRIVER_CHAIN_LENGTH, CLOCK_PIN, DATA_PIN);
Adafruit_TLC5947 tlc = Adafruit_TLC5947(LED_DRIVER_CHAIN_LENGTH, CLOCK_PIN, DATA_PIN, LATCH_PIN);

byte RGB_MAPPING[RGB_COUNT] = [0,1,2]; // define which port each led device is plugged into.

void ping_data(){
  if (Serial.available()){
    char data[DATA_LENGTH_LIMIT];
    int i = 0;
    while (Serial.available()){
      data[i] = Serial.read();
      i++;
    }
    data[i] = '\0';
    Serial.println(data);
  }
}

byte from_hex(char input){
  if (input >= 'A' && input <= 'F'){
    return (byte) input - 'A' + 10;
  }else if (input >= '0' && input <= '9'){
    return (byte) input - '0';
  }
}

void wait_for_serial(){
  while (not Serial.available()) {
    delay(10);
  }
}

void set_colour(byte rgb_i, byte R, byte G, byte B){
  port = RGB_MAPPING[rgb_i];
  tlc.setLED(port, R, G, B);
  tlc.write();
}

void set_colours_from_hex(){
  for (byte rgb_i = 0; rgb_i < RGB_COUNT; rgb_i++){
    
    byte R = from_hex(Serial.read()) * (byte) 16;
    wait_for_serial();
    byte R += from_hex(Serial.read());
    wait_for_serial();
    
    byte G = from_hex(Serial.read()) * (byte) 16;
    wait_for_serial();
    byte G += from_hex(Serial.read());
    wait_for_serial();
    
    byte B = from_hex(Serial.read()) * (byte) 16;
    wait_for_serial();
    byte B += from_hex(Serial.read());
    if (rgb_i != RGB_COUNT -1){
      wait_for_serial();
    }

    set_colour(rgb_i, R, G, B);
  }
      
      intensity = from_hex(Serial.read()) * (byte) 16;
      wait_for_serial();
      intensity += from_hex(Serial.read());
      if (rgb_i != RGB_COUNT-1 || colour_i != 2){
        // Don't need to wait after very last value.
        wait_for_serial();
      }

      set_colour(rgb_i, colour_i, intensity);
    }
  }
}

void set_colours_from_bytes(){
  for (byte rgb_i = 0; rgb_i < RGB_COUNT; rgb_i++){
    byte R = Serial.read();
    wait_for_serial();
    byte G = Serial.read();
    wait_for_serial();
    byte B = Serial.read();
    if (rgb_i != RGB_COUNT -1){
      wait_for_serial();
    }

    set_colour(rgb_i, R, G, B);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUDRATE);
  while (!Serial){
    delay(10); // Wait until devices connect.
  }
  
  tlc.begin();
  if (OE >= 0){
    pinMode(OE, OUTPUT);
    digitalWrite(OE, LOW);
  }
}

void loop() {
  if (Serial.available()){
    set_colours_from_bytes();
  }
  
  delay(DELAY_TIME);
}
