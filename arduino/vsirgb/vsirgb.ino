// Make sure this matches the rate in the 'config.py' file.
#define BAUDRATE 9600
#define DELAY_TIME 100
#define DATA_LENGTH_LIMIT 512

void setup() {
  // put your setup code here, to run once:
  Serial.begin(BAUDRATE);
  while (!Serial){
    delay(10); // Wait until devices connect.
  }
}

void loop() {
  // put your main code here, to run repeatedly:
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
  delay(DELAY_TIME);
}
