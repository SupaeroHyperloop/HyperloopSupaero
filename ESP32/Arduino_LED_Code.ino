#define azul 15


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.print("Programa para encender luz");
  pinMode(azul, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(azul, HIGH); 
  Serial.print("La luz esta encendida\n");
  delay(1000);
  digitalWrite(azul, LOW);
  Serial.print("La luz esta apagada\n");
  delay(1000);

}
