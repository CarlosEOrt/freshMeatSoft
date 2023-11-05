#include <DHT.h>

#define DHTTYPE DHT22
 
const int DHTPin = 2;
 
DHT dht(DHTPin, DHTTYPE);
                                                                                                                                  
void setup() 
{
   Serial.begin(9600);
 
   dht.begin();
}
 
void loop() 
{
   float h = dht.readHumidity();
   float t = dht.readTemperature();
   float f = dht.readTemperature(true);
 
   if (isnan(t) || isnan(f) || isnan(h))
   {
      Serial.println("Error en el sensor!");
      return;
   }

   Serial.println(t);
   Serial.println(f);
   Serial.println(h);
}