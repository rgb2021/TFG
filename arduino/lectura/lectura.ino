#include <ArduinoJson.h>
#include <SoftwareSerial.h>
#include <SimpleDHT.h>
#include <BH1750.h>

BH1750 lightMeter;

int pinDHT22 = 2;
SimpleDHT22 dht22(pinDHT22);
int pinHumedadSuelo = A0; // Puerto analógico A0 para la lectura del fotosensor
unsigned long tiempoPaso = 60000; //milisegundos entre paso
const int alAire = 780;
const int enAgua = 350;


void setup() {
  Serial.begin(9600);
  Wire.begin();
  lightMeter.begin();
}

void loop() 
{
  int humedadSuelo = map(analogRead(A0),alAire,enAgua,0,100);
  //int humedadSuelo = analogRead(A0);

  float lux = lightMeter.readLightLevel();
  float temperatura = 0;
  float humedad = 0;
  dht22.read2(&temperatura, &humedad, NULL);

  StaticJsonDocument<200> doc;

  doc["lux"] = lux;
  doc["temperatura"] = temperatura;
  doc["humedad"] = humedad;
  doc["humedadSuelo"] = humedadSuelo;

  String jsonStr;
  serializeJson(doc, jsonStr);
  Serial.println(jsonStr);
  delay(tiempoPaso);
}
