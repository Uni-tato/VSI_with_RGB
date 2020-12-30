// Make sure this matches the rate in the 'config.py' file.
#define BAUDRATE 9600
#define DELAY_TIME 5000
#define DATA_LENGTH_LIMIT 512
#define RGB_COUNT 3

#define color colour



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

void set_colour(byte rgb_i, byte colour_i, byte intensity){
  Serial.print("RGB #"); Serial.print((int) rgb_i);
  
  if (colour_i == 0){
    Serial.print(" Red set to: ");
  }else if (colour_i == 1){
    Serial.print(" Green set to: ");
  }else if (colour_i == 2){
    Serial.print(" Blue set to: ");
  }else{
    Serial.print("Whoopsie, something went wrong!");
  }

  Serial.println((int) intensity);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUDRATE);
  while (!Serial){
    delay(10); // Wait until devices connect.
  }
}

void loop() {
  
  if (Serial.available()){
    for (byte rgb_i = 0; rgb_i < RGB_COUNT; rgb_i++){
      for (byte colour_i = 0; colour_i < 3; colour_i++){
        byte intensity;
        
        intensity = from_hex(Serial.read()) * (byte) 16;
        wait_for_serial();
        intensity += from_hex(Serial.read());
        wait_for_serial();

        set_colour(rgb_i, colour_i, intensity);
      }
    }
  }
  
  delay(DELAY_TIME);
}
