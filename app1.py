from flask import Flask, render_template, request
import serial

app = Flask(__name__)  # Corect: __name, nu _name

# Portul serial (modifică dacă Arduino e pe alt port)
ser = serial.Serial('COM3', 9600, timeout=1)

@app.route("/")
def index():
    return render_template("web.html")

@app.route("/control_led", methods=["POST"])
def control_led():
    status = request.form["status"]
    if status == "ON":
        ser.write(b'A')  # Trimite 'A' spre Arduino pentru aprindere
    else:
        ser.write(b'S')  # Trimite 'S' spre Arduino pentru stingere
    return "OK"

if __name__  == "__main__":
    app.run(debug=True, use_reloader=False)  # evităm dublarea portului
