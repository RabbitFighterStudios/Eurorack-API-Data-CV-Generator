# POC: Generating CV in Eurorack using Live Data from APIs

This Proof of Concept demonstrates how to use APIs to generate Control Voltage (CV) in a Eurorack modular system. We'll use the Monome Teletype module to achieve this.

## Components

- **Monome Teletype**: Digital algorithmic ecosystem module for Eurorack.
- **Computer/Raspberry Pi**: To fetch data from APIs.
- **Python**: To process and send data to the Teletype.

## Monome Teletype Specifications

- **Size**: 18 HP, 32 mm deep
- **Current draw**: 72 mA +12V, 12 mA -12V, 0 mA 5V
- **Features**: Eight trigger inputs, four CV outputs, internal metronome, USB keyboard for modifying scripts, rear ribbon cable for remote control.
- **Patterns**: Lists of numbers with 64 indexes (positions), each pattern stores the same data type as the rest of Teletype: -32384 to 32384.
- **CV outputs**: Create voltages between 0 and 10V (internally seen as 0 to 16384, which is 14 bit).

## Steps

### 1. Setup Environment

- Install the Monome Teletype module in your Eurorack system.
- Connect a USB keyboard to the Teletype for scripting.

### 2. Fetch Data from APIs

Use a computer or Raspberry Pi to fetch live data from APIs. Below is an example using Python.

### 2. Python Code to Fetch Data

```python
import requests

def get_atmospheric_pressure():
    response = requests.get('https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Mexico')
    weather_data = response.json()
    return weather_data['current']['pressure_mb']

def get_fortnite_users():
    response = requests.get('https://api.fortniteapi.com/v1/stats')
    fortnite_data = response.json()
    return fortnite_data['current_users']
```

### 3.  Process Data

* Convert the data into a format that can be sent to the Teletype.

### Data Processing Code
```python
def map_to_teletype_cv(value, min_input, max_input, min_output=0, max_output=16384):
    return int((value - min_input) * (max_output - min_output) / (max_input - min_input) + min_output)

pressure = get_atmospheric_pressure()
pressure_cv = map_to_teletype_cv(pressure, 950, 1050)

fortnite_users = get_fortnite_users()
fortnite_cv = map_to_teletype_cv(fortnite_users, 0, 1000000)
, 1000000)
```

### 4. Send Data to Teletype

* Use USB or serial connection to send the processed data to the Teletype.

```python
import serial

def send_to_teletype(cv_value, port='/dev/ttyUSB0', baudrate=9600):
    with serial.Serial(port, baudrate) as ser:
        ser.write(f'{cv_value}\n'.encode())

send_to_teletype(pressure_cv)
send_to_teletype(fortnite_cv)
_cv)
```

### 5. Teletype Script

* Write a script on the Teletype to receive and interpret the incoming data.

#### Example Teletype Script
```plaintext
# Script 1
# This script triggers when data is received
# Assume we receive data as a simple number for simplicity

CV 1 RX

# Now the CV 1 output will reflect the received value
```

### 6. Connecting the Hardware

#### Hardware Setup:

* Connect the computer or Raspberry Pi to the Teletype's USB port.
* Use a DAC to convert digital signals to analog if needed.

#### CV Outputs:

* Route the Teletype's CV outputs to other modules in your Eurorack system to control pitch, filters, or other parameters.

## Summary

By following these steps, you can create a dynamic system where live data from APIs controls various parameters in your Eurorack setup. This approach allows you to create complex, data-driven modulation and sequencing in your modular synth environment.


