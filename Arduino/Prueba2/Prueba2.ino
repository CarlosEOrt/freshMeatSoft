#include <DHT.h>

#define DHTTYPE DHT22
 
const int DHTPin = 2;
const int ledPinCalentamiento = 8;
const int ledPinEnfriamiento = 9;
const float rangoMenorCalentamiento = 15.0;
const float rangoMayorCalentamiento = 20.0;
const float rangoMenorEnfriamiento = 25.0;
const float rangoMayorEnfriamiento = 30.0;
bool calentando = false;
bool enfriando = false;
int contadorPrueba = 20;
 
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
  delay(2000);

  float humidity = dht.readHumidity();
  float celsius = dht.readTemperature();
  float fahrenheit = dht.readTemperature(true);
 
  if (isnan(celsius) || isnan(fahrenheit) || isnan(humidity))
  {
    Serial.println("Error en el sensor!");
    return;
  }

  if(calentando)
  {
    contadorPrueba+=1;
  }

  if(enfriando)
  {
    contadorPrueba-=1;
  }

  if(!calentando && !enfriando)
  {
    contadorPrueba+=1;
  }

  if(contadorPrueba<=rangoMenorCalentamiento)
  {
    calentando = true;
    digitalWrite(ledPinCalentamiento, HIGH);
  }

  if(calentando && contadorPrueba>=rangoMayorCalentamiento)
  {
    calentando = false;
    digitalWrite(ledPinCalentamiento, LOW);
  }

  if(contadorPrueba>=rangoMayorEnfriamiento)
  {
    enfriando = true;
    digitalWrite(ledPinEnfriamiento, HIGH);
  }

  if(enfriando && contadorPrueba<=rangoMenorEnfriamiento)
  {
    enfriando = false;
    digitalWrite(ledPinEnfriamiento, LOW);
  }

  Serial.println(celsius);
  Serial.println(fahrenheit);
  Serial.println(humidity);
  Serial.print("Contador Prueba: ");
  Serial.println(contadorPrueba);
}