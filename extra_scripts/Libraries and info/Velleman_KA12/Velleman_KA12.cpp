#include "Velleman_KA12.h"

#define KA12_VALUE_COUNT 24

const int ka12_values[KA12_VALUE_COUNT] = {180,182,181,183,177,176,179,178,173,175,174,171,168,169,154,153,152,155,157,159,156,158,170,172};

void ka12_init() {
	pinMode(KA12_LATCH_PIN, OUTPUT);
	pinMode(KA12_CLOCK_PIN, OUTPUT);
	pinMode(KA12_DATA_PIN,  OUTPUT);
}

void ka12_readAll(int *values) {
	int adr;
	for (int cnt=0; cnt < KA12_VALUE_COUNT ; cnt++)
	{
		// send address
		digitalWrite(KA12_LATCH_PIN, LOW);
		shiftOut(KA12_DATA_PIN, KA12_CLOCK_PIN, MSBFIRST, ka12_values[cnt]);  
		digitalWrite(KA12_LATCH_PIN, HIGH);
		delayMicroseconds(100); 

		// write value in array
		values[cnt] = analogRead(A0);
	}

	// turn LED off
	digitalWrite(KA12_LATCH_PIN, LOW);
	shiftOut(KA12_DATA_PIN, KA12_CLOCK_PIN, MSBFIRST, 0);  
	digitalWrite(KA12_LATCH_PIN, HIGH);  
}

int ka12_read(int sensorAdress) {

	sensorAdress=sensorAdress-1;

	  
	digitalWrite(KA12_LATCH_PIN, LOW);
	shiftOut(KA12_DATA_PIN, KA12_CLOCK_PIN, MSBFIRST, ka12_values[sensorAdress]);  
	digitalWrite(KA12_LATCH_PIN, HIGH);
	delayMicroseconds(100); 

	int sensorValue = analogRead(A0);
	   
	// turn LED off
	digitalWrite(KA12_LATCH_PIN, LOW);
	shiftOut(KA12_DATA_PIN, KA12_CLOCK_PIN, MSBFIRST, 0);  
	digitalWrite(KA12_LATCH_PIN, HIGH); 
	  
	return sensorValue;
}
