import RPi.GPIO as GPIO
import time

M1 = 23   # GPIO23
M1 = 24   # GPIO24
E1 = 18   # GPIO18 (PWM)

def setup():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(M1, GPIO.OUT)
    GPIO.setup(M1, GPIO.OUT)
    GPIO.setup(E1, GPIO.OUT)

    # PWM 周波数 500Hz
    global pwm
    pwm = GPIO.PWM(E1, 20000)
    pwm.start(0)  # Duty比0%

def forward(speed):
    GPIO.output(M1, GPIO.HIGH)
    GPIO.output(M1, GPIO.LOW)
    pwm.ChangeDutyCycle(speed * 100 / 1024)  # 0〜1024 → 0〜100%

def stop():
    GPIO.output(M1, GPIO.LOW)
    GPIO.output(M1, GPIO.LOW)
    pwm.ChangeDutyCycle(0)

def main():
    setup()

    try:
        while True:
            # 加速
            for speed in range(0, 1025, 100):
                forward(speed)
                time.sleep(0.5)

            # 減速
            for speed in range(1024, -1, -100):
                forward(speed)
                time.sleep(0.5)

            stop()
            time.sleep(2)

    except KeyboardInterrupt:
        pass

    pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    main()