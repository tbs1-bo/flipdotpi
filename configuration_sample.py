"""
Some default configuration options with default values.
Copy this file to configuration.py and change the values as needed.
"""

WIDTH = 28
HEIGHT = 13

flipdotdisplay = {
    #"serialdevice": "spy:///dev/ttyUSB0",  # use this for debugging
    "serialdevice": "/dev/ttyUSB0",
    "serialbaudrate": 115200,
    "i2c_address": 0x20,
    "modules": [18],
    "buffered": False
}

display_server = {
    "host": "0.0.0.0",
    "port": 10101
}

remote_display = {
    "host": "localhost",
    "port": 10101
}

simulator = {
    "fps": 60
}


mqtt_broker = 'mqtt.eclipse.org'
mqtt_topic_display = 'fff_display'
mqtt_topic_info = 'fff_display_info'

web_conference_url = 'https://meet.ffmuc.net/flipflapflop'
