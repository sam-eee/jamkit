
IN LIBRARY FOLDER

Install Velleman KA-12 and MLX90393 library into the Arduino IDE.

Install Dynamixel SDK as per instructions here: http://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/library_setup/python_windows/#python-windows

PYTHON CODE FILES WITH FUNCTIONS IN PYTHON FOLDER:
AX-12 (Requires all files in the AX-12 folder for it to work, uses a library: 
	ax12_code.py functions can be used to directly on the motors, self explainatory
	
	motorsliders.py is a script that creates sliders for the user to move the motors using the functions defined in ax12_code.py
	Useful for testing and manual manipulation.


sensor_process.py
	This file has the functions for the Pi to open and close serial connections, request, process and save serial data from the Arduino for all sensors. The user can decide how they want to split the outputs for control etc, but it runs forever.
	Recommended order of data per request cycle from the Arduino: 16 Rotational pots analog readings, 4 1D analog readings, 4 3D digital readings (X,Y,Z)

ARDUINO CODE
	Arduino_Sensors is uploaded to the Arduino to analogread all analog sensors and the I2C 3D hall effect sensors. Is set up for 16 rotational, 4 1D, 4 3D. Same for sensor_process.py
	
DISCLAIMER: THE CODE HAS NOT BE DEBUGGED DUE TO BEING UNABLE TO TEST IT ON THE ACTUAL ROBOT DUE TO THE INABILITY TO BUILD IT DUE TO COVID-19. IT SHOULD BE FINE, BUT MAY NEED SOME MINOR DEBUGS.
