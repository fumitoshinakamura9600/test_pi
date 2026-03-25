from gpiozero import AngularServo
from time import sleep

# サーボの設定
# min_pulse_width と max_pulse_width はサーボに合わせて調整
servo = AngularServo(
    18,                     # GPIOピン番号
    min_angle=-90,
    max_angle=90,
    min_pulse_width=0.0005, # 0.5ms
    max_pulse_width=0.0024  # 2.4ms
)

# -90° に移動
servo.angle = -90
sleep(1)

# -90° から +90° へゆっくり回転
for degree in range(-90, 91):
    servo.angle = degree
    sleep(0.01)  # 10ms待機