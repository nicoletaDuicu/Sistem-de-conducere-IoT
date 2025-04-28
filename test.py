import serial

try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    print("Portul s-a deschis cu succes!")
    ser.close()
except Exception as e:
    print(f"Eroare la deschiderea portului: {e}")