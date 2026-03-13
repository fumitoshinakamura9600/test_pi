from gpiozero import Servo
from time import sleep

# サーボモーターの制御ピンを指定
servo = Servo(18)  # GPIO 18 番ピンを使用

# サーボモーターをゆっくり動かす関数
def slow_move_servo(start, end, step, delay):
    """
    サーボモーターをゆっくり動かす関数。

    :param start: 開始位置 (-1.0 から 1.0)
    :param end: 終了位置 (-1.0 から 1.0)
    :param step: 動かすステップの大きさ
    :param delay: ステップ間の遅延時間（秒）
    """
    if start < end:
        position = start
        while position <= end:
            servo.value = position
            sleep(delay)
            position += step
    else:
        position = start
        while position >= end:
            servo.value = position
            sleep(delay)
            position -= step

# メイン処理
try:
    print("サーボモーターをゆっくり動かします...")
    # -1.0 から 1.0 までゆっくり動かす
    slow_move_servo(-1.0, 1.0, 0.1, 0.2)
    # 1.0 から -1.0 までゆっくり戻す
    slow_move_servo(1.0, -1.0, 0.1, 0.2)
except KeyboardInterrupt:
    print("\n操作を中断しました。")
finally:
    servo.detach()
    print("サーボモーターを停止しました。")