import pigpio
import time

# pigpioデーモンへ接続
pi = pigpio.pi()
if not pi.connected:
    exit()

SERVO_PIN = 18  # PWM対応ピン（GPIO18,19,12,13など）

# サーボのパルス幅（一般的なSG90系）
MIN_PW = 500   # -90°
MAX_PW = 2400  # +90°

def angle_to_pulsewidth(angle):
    """角度(-90〜90)をパルス幅(500〜2400us)に変換"""
    return MIN_PW + (MAX_PW - MIN_PW) * (angle + 90) / 180

# 90° → -90° にゆっくりスイープ
for degree in range(90, -90):
    pw = angle_to_pulsewidth(degree)
    pi.set_servo_pulsewidth(SERVO_PIN, pw)
    time.sleep(0.05)

# -90° → +90° にゆっくりスイープ
for degree in range(-90, 90):
    pw = angle_to_pulsewidth(degree)
    pi.set_servo_pulsewidth(SERVO_PIN, pw)
    time.sleep(0.05)

# サーボ信号を停止
pi.set_servo_pulsewidth(SERVO_PIN, 0)

# pigpio切断
pi.stop()