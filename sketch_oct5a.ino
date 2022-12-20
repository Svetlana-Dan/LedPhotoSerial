#define led_pin 3
#define sensor_pin A2

void setup() {
  Serial.begin(9600);
  pinMode(led_pin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0){ //проверяем пришли ли символы
    char message = Serial.read(); 
    if (message == 'u'){
      digitalWrite(led_pin, HIGH);
    }
    else if (message == 'd'){
      digitalWrite(led_pin, LOW);
    }
    else if (message == 'f' || message == 'a'){
      int val = analogRead(sensor_pin); 
      val = map(val, 0, 1023, 100, 999); //аналоговый может меняться от 0 до 1023, а нам нужно 3 значное число, потому что питон принимает 3 символа
      Serial.print(val);
    }
    else if(message != 'b'){
      Serial.println("Unknown message");
    }
  }


}
