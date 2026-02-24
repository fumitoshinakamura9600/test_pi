from gpiozero import Servo
import time
import warnings

warnings.filterwarnings("ignore")

servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000)

def move_servo(angle, hold_time=0.5):
    if angle < -90 or angle > 90:
        raise ValueError("Angle must be between -90 and 90")
    servo.value = angle / 90.0
    time.sleep(hold_time)
    servo.detach()

move_servo(10)