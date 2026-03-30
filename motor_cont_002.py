import pigpio
import time

IN1 = 23   # GPIO23
IN2 = 24   # GPIO24
ENA = 18   # GPIO18 (ハードウェアPWM対応ピン)

def setup(pi):
    # GPIO 出力設定
    pi.set_mode(IN1, pigpio.OUTPUT)
    pi.set_mode(IN2, pigpio.OUTPUT)

    # PWM 周波数を 30000Hz に設定
    pi.set_PWM_frequency(ENA, 1000000)

    # Duty比を 0 にして開始
    pi.set_PWM_dutycycle(ENA, 0)

def forward(pi, speed):
    # 方向設定
    pi.write(IN1, 1)
    pi.write(IN2, 0)

    # wiringPi の 0〜1024 → pigpio の 0〜255 に変換
    duty = int(speed * 255 / 1024)
    pi.set_PWM_dutycycle(ENA, duty)

def stop(pi):
    pi.write(IN1, 0)
    pi.write(IN2, 0)
    pi.set_PWM_dutycycle(ENA, 0)

def main():
    pi = pigpio.pi()
    if not pi.connected:
        print("pigpio デーモンが起動していません。")
        return

    setup(pi)

    try:
        while True:
            # 加速
            for speed in range(0, 1025, 100):
                forward(pi, speed)
                time.sleep(0.5)

            # 減速
            for speed in range(1024, -1, -100):
                forward(pi, speed)
                time.sleep(0.5)

            stop(pi)
            time.sleep(2)

    except KeyboardInterrupt:
        pass

    stop(pi)
    pi.stop()

if __name__ == "__main__":
    main()