# servo_server.py
import socket
import pigpio
import time

HOST = "0.0.0.0"
PORT = 50000

pi = pigpio.pi()
SERVO_PIN = 18

MIN_PW = 500
MAX_PW = 2400

def angle_to_pulsewidth(angle):
    return MIN_PW + (MAX_PW - MIN_PW) * (angle + 90) / 180

# ソケットサーバー開始
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Waiting for connection...")

    conn, addr = s.accept()
    print("Connected:", addr)

    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            angle = int(data.decode())
            print("Received angle:", angle)

            pi.set_servo_pulsewidth(SERVO_PIN, angle_to_pulsewidth(angle))
            time.sleep(0.02)
