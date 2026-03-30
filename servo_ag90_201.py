import pigpio
import time

# pigpioデーモンへ接続
pi = pigpio.pi()
if not pi.connected:
    exit()

SERVO_PIN = 18   # サーボPWMピン
SWITCH_PIN = 23  # スイッチ入力ピン（任意で変更OK）

# スイッチ入力設定（プルアップ）
pi.set_mode(SWITCH_PIN, pigpio.INPUT)
pi.set_pull_up_down(SWITCH_PIN, pigpio.PUD_UP)  # 内蔵プルアップ

# サーボのパルス幅（一般的なSG90系）
MIN_PW = 500    # -90°
MID_PW = 1500   # 0°
MAX_PW = 2400   # +90°

def angle_to_pulsewidth(angle):
    """角度(-90〜90)をパルス幅(500〜2400us)に変換"""
    return MIN_PW + (MAX_PW - MIN_PW) * (angle + 90) / 180

def move_servo_smooth(current, target, step_delay=0.01):
    """現在角度 → 目標角度へゆっくり移動"""
    step = 1 if target > current else -1
    for angle in range(current, target + step, step):
        pi.set_servo_pulsewidth(SERVO_PIN, angle_to_pulsewidth(angle))
        time.sleep(step_delay)
    return target

# 初期角度（90°）
current_angle = 90
pi.set_servo_pulsewidth(SERVO_PIN, angle_to_pulsewidth(current_angle))
time.sleep(0.5)

print("スイッチを押すと 0°、離すと 90° に動きます。Ctrl+C で終了。")

try:
    while True:
        sw = pi.read(SWITCH_PIN)  # 0 = 押されている, 1 = 離されている

        if sw == 0 and current_angle != 0:
            # スイッチ押されている → 0°へ
            current_angle = move_servo_smooth(current_angle, 0)

        elif sw == 1 and current_angle != 90:
            # スイッチ離されている → 90°へ
            current_angle = move_servo_smooth(current_angle, 90)

        time.sleep(0.06)

except KeyboardInterrupt:
    pass

# サーボ信号を停止
pi.set_servo_pulsewidth(SERVO_PIN, 0)
pi.stop()