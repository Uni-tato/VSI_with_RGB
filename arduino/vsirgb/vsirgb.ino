// Make sure this matches the rate in the 'config.py' file.
#define BAUDRATE 9600
#define DELAY_TIME 100

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
    char data = Serial.read();
    char str[2];
    str[0] = data;
    str[1] = '/0';
    Serial.print(str);
  }
  delay(DELAY_TIME);
}
