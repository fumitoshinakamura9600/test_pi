# servo_ag90_001 - Raspberry Pi Servo Control

Control AG90 servo motors on Raspberry Pi with Python.

> **For AI assistants**: To initialize context for this project, say "Please read COPILOT-INIT.md to initialize"

## Quick Start

```python
from servo_ag90_001 import move_servo

# Move servo to 45 degrees for 0.5 seconds
move_servo(45)

# Move servo to -30 degrees for 1 second
move_servo(-30, hold_time=1.0)
```

## Requirements

- Raspberry Pi with GPIO support
- AG90 servo motor
- gpiozero library
- Python 3

## Wiring

- Servo Signal → GPIO 18 (BCM)
- Servo VCC → 5V
- Servo GND → GND

## Documentation

- **COPILOT-INIT.md** - AI context (conventions, architecture, working approach)
- **PROJECT_STATUS.md** - Current development status and recent work