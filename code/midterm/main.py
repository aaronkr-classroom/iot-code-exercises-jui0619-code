# main.py
from lib.room_sensor import RoomSensor

sensors = [
    RoomSensor("Kitchen", 31, 72, 180),
    RoomSensor("Bedroom", 23, 50, 300),
    RoomSensor("Balcony", 27, 45, 500),
]

count = {
    "Comfortable": 0,
    "Normal": 0,
    "Warning": 0
}

for sensor in sensors:
    sensor.show_info()
    comfort = sensor.comfort_level()
    light = sensor.light_status()
    print(f"Comfort Level: {comfort}")
    print(f"Light Status: {light}")
    print()

    count[comfort] += 1

print(f"Comfortable: {count['Comfortable']}")
print(f"Normal: {count['Normal']}")
print(f"Warning: {count['Warning']}")