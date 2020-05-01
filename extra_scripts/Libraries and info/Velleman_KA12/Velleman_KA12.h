/*
 * Velleman KA12 - Analog extension shield
 * Version 1.0 March, 2015
 * Copyright 2015 Velleman nv
 * 
 */

#ifndef VELLEMAN_KA12_H
#define VELLEMAN_KA12_H

#include "Arduino.h"

#define KA12_LATCH_PIN 6
#define KA12_CLOCK_PIN 7
#define KA12_DATA_PIN  5

void ka12_init();
void ka12_readAll(int *values);
int ka12_read(int sensorAdress);

#endif