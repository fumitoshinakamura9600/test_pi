from flask import Flask, request
import pigpio

app = Flask(__name__)
pi = pigpio.pi()
SERVO_PIN = 18

@app.route("/set_angle")
def set_angle():
    angle = int(request.args.get("value", 90))
    pulse = int(500 + (angle / 180) * 2000)
    pi.set_servo_pulsewidth(SERVO_PIN, pulse)
    return f"Angle set to {angle}"

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    app.run(host="192.168.4.1", port=5000)
