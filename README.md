This project implements a remote lighting control system based on an Arduino microcontroller and a Python Flask server.
Communication between the server and the Arduino is established using UART (Universal Asynchronous Receiver/Transmitter) protocol via the USB port.
The system allows users to remotely turn lights ON/OFF through a simple web interface.

Technologies Used

-Arduino UNO/Nano (microcontroller to control lights)

-Python Flask (web server handling HTTP requests and serial communication)

-HTML/CSS (frontend web interface for user control)

-UART Serial Communication 



  System Architecture
  
-Arduino is connected to the lights (via digital output pins) and listens for UART serial commands (ON, OFF).

-Python Flask Server runs locally on a PC, sending serial commands over USB UART to the Arduino.

-Web Interface served by Flask allows users to press control buttons.

-Commands entered via the browser are sent to the Arduino in real-time.

