#include <Velleman_KA12.h>

int all[24];
int sensor;

void setup() {
  Serial.begin(115200);
  ka12_init(); 
}

void loop() {
  
  ka12_readAll(all);
  for (int i=0; i < 24; i=i+1) {
  Serial.print(i);
  Serial.print(" / ");
  Serial.println(all[i]); 
  }
  
  
  sensor = ka12_read(1);
  Serial.print("Waarde sensor 1 :");
  Serial.println(sensor); 
  
  
  delay(1000);
}
