#include <Wire.h>
#include <MLX90393.h> //From https://github.com/tedyapo/arduino-MLX90393 by Theodore Yapo
#include <Velleman_KA12.h> //From https://www.velleman.eu/downloads/files/downloads/velleman_ka12.zip

int num_ana=18; //Change the number to suit the number of analog sensors, up to 24.
//Rotational sensors should be wired from port 1, followed by 1D hall effect sensors.

int num_3d=3; //Change the number to suit the number of MLX90393 sensors, up to 8
int all[num_ana];
int sensor;


MLX90393 mlx;
MLX90393::txyz data; //Create a structure, called data, of four floats (t, x, y, and z)


#define TCAADDR 0x70 //I2C address for the TCA9548A multiplexer

//Function to select the I2C ports on the TCA9548A. 
void tcaselect(uint8_t i) {
  if (i > 7) return;
 
  Wire.beginTransmission(TCAADDR);
  Wire.write(1 << i);
  Wire.endTransmission();  
}

void setup()
{
  Serial.begin(9600);
  Wire.begin();

  for(int i=0;i<num_3d;i=i+1){
  tcaselect(i)
  byte status = mlx.begin(0,1);
  Serial.println();
  mlx.setGainSel(0);
  mlx.setResolution(0, 0, 0); //x, y, z
  mlx.setOverSampling(1);
  mlx.setDigitalFiltering(7);
  mlx.setTemperatureCompensation(1);
  }

  //See MLX90393.h and .cpp for additional functions including:
  //set/getOverSample, set/getTemperatureOverSample, set/getDigitalFiltering, set/getResolution
  //set/getTemperatureCompensation, setOffsets, setWThresholds

  ka12_init(); //Initialise the KA-12
  
}

void loop()
{
    ka12_readAll(all);
    String output="";
    for (int i=0; i < num_ana; i=i+1) {
      output=output+all[i]+",";
    }
    
    //Output the MLX90393 x,y,z data from the TCA9584A port 0 ascending
    for(int i=0;i<num_3d;i=i+1){
      tcaselect(i)
      mlx.readData(data); //Read the values from the sensor
      output=output+data.x+","+data.y+","+data.z"+",";
    }
    output.remove(output.length()-1,1);
    Serial.println(output);
    //delay(0.1);
}
