#include <DHT.h>

#define DHTTYPE DHT22
 
const int DHTPin = 2;
const int ledPinCalentamiento = 9;
const int ledPinEnfriamiento = 8;
const float rangoMenorCalentamiento = 20.0;
const float rangoMayorCalentamiento = 23.0;
const float rangoMenorEnfriamiento = 24.0;
const float rangoMayorEnfriamiento = 27.0;
bool calentando = false;
bool enfriando = false;
String imprimir = "";
 
DHT dht(DHTPin, DHTTYPE);
                                                                                                                                  
void setup() 
{
  Serial.begin(9600);
 
  pinMode(ledPinCalentamiento, OUTPUT); 
  pinMode(ledPinEnfriamiento, OUTPUT); 

  dht.begin();
}
 
void loop() 
{
  float humidity = dht.readHumidity();
  float celsius = dht.readTemperature();
  float fahrenheit = dht.readTemperature(true);
 
  if (isnan(celsius) || isnan(fahrenheit) || isnan(humidity))
  {
    Serial.println("Error en el sensor!");
    return;
  }

  if(celsius<=rangoMenorCalentamiento)
  {
    calentando = true;
    digitalWrite(ledPinCalentamiento, HIGH);
  }

  if(calentando && celsius>=rangoMayorCalentamiento)
  {
    calentando = false;
    digitalWrite(ledPinCalentamiento, LOW);
  }

  if(celsius>=rangoMayorEnfriamiento)
  {
    enfriando = true;
    digitalWrite(ledPinEnfriamiento, HIGH);
  }

  if(enfriando && celsius<=rangoMenorEnfriamiento)
  {
    enfriando = false;
    digitalWrite(ledPinEnfriamiento, LOW);
  }

  imprimir = String(celsius, 2);
  imprimir.concat("C");
  Serial.println(imprimir);
  imprimir = String(fahrenheit, 2);
  imprimir.concat("F");
  Serial.println(imprimir);
  imprimir = String(humidity, 2);
  imprimir.concat("H");
  Serial.println(imprimir);
}