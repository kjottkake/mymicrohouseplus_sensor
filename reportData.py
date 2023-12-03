from sense_hat import SenseHat
import time
import json
from datetime import datetime

# Initialize the SenseHat object
sense = SenseHat()
sense.clear()

# Function to get sensor data and write to a JSON file
def get_and_save_sensor_data():
    while True:
        # Get sensor data
        humid = int(sense.get_humidity())
        temp = int(sense.get_temperature_from_humidity())
        press = int(sense.get_pressure())

        # Prepare data with timestamp
        sensor_data = {
            "timestamp": datetime.now().isoformat(),
            "humidity_percentage": humid,
            "temperature_celsius": temp,
            "pressure_hpa": press
        }

        # Writing data to JSON file
        with open('data.json', 'w') as file:
            json.dump(sensor_data, file, indent=4)

        print(f"Data saved: {sensor_data}")

        # Wait for 30 seconds before the next read
        time.sleep(30)

# Start the data collection and saving process
get_and_save_sensor_data()
