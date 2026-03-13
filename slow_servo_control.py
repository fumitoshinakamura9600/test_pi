from gpiozero import PWMOutputDevice
from time import sleep

# サーボモーターの制御ピンを指定
servo = PWMOutputDevice(18, frequency=50)  # GPIO 18 番ピンを使用、周波数 50Hz

# 角度を PWM パルス幅に変換する関数
def angle_to_pwm(angle):
    """
    角度を PWM パルス幅に変換。
    :param angle: -90 から 90 度の角度
    :return: PWM パルス幅（0.0 から 1.0）
    """
    min_pulse = 0.5  # 最小パルス幅（ミリ秒）
    max_pulse = 2.4  # 最大パルス幅（ミリ秒）
    pulse_range = max_pulse - min_pulse
    duty_cycle = (min_pulse + (angle + 90) * pulse_range / 180) / 20  # 20ms周期に正規化
    return duty_cycle

# サーボモーターをゆっくり動かす関数
def slow_move_servo(start_angle, end_angle, step, delay):
    """
    サーボモーターをゆっくり動かす関数。

    :param start_angle: 開始角度 (-90 から 90)
    :param end_angle: 終了角度 (-90 から 90)
    :param step: 動かすステップの大きさ（度数）
    :param delay: ステップ間の遅延時間（秒）
    """
    if start_angle < end_angle:
        angle = start_angle
        while angle <= end_angle:
            servo.value = angle_to_pwm(angle)
            sleep(delay)
            angle += step
    else:
        angle = start_angle
        while angle >= end_angle:
            servo.value = angle_to_pwm(angle)
            sleep(delay)
            angle -= step

# メイン処理
try:
    print("サーボモーターをゆっくり動かします...")
    # -90度から90度までゆっくり動かす
    slow_move_servo(-90, 90, 5, 0.2)
    # 90度から-90度までゆっくり戻す
    slow_move_servo(90, -90, 5, 0.2)
except KeyboardInterrupt:
    print("\n操作を中断しました。")
finally:
    servo.off()
    print("サーボモーターを停止しました。")