import time
#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIOの18番ピンを出力に設定
GPIO.setup(18, GPIO.OUT)

#GPIOの18番ピンをPWM出力に設定
pwm = GPIO.PWM(18, 50)  # 50HzのPWM
pwm.start(0)  # PWMを開始、初期値は0

#-90°の位置に移動
pwm.ChangeDutyCycle(2.5)  # 2.5%のデューティサイクルは-90°に対応
time.sleep(1)  #1秒待機

#少しずつ回転
for degree in range(-90,91):
    dc = 2.5 + (12.0-2.5)/180:* (degree + 90)  # デューティサイクルを計算
    p.ChangeDutyCycle(dc)  # デューティサイクルを変更
    time.sleep(0.03)  # 300ms待機
    p.ChangeDutyCycle(0)  # デューティサイクルを0にして停止
    