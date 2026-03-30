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

# ★ 最初の位置（例：0° → -90°へゆっくり移動）
current_angle = 90
target_angle = -90

step = -1 if target_angle < current_angle else 1

for degree in range(current_angle, target_angle + step, step):
    pi.set_servo_pulsewidth(SERVO_PIN, angle_to_pulsewidth(degree))
    time.sleep(0.05)

# 1秒待機
time.sleep(1)

# ★ -90° → +90° にゆっくりスイープ
for degree in range(-90, 91):
    pi.set_servo_pulsewidth(SERVO_PIN, angle_to_pulsewidth(degree))
    time.sleep(0.05)

# サーボ信号を停止
pi.set_servo_pulsewidth(SERVO_PIN, 0)

# pigpio切断
pi.stop()