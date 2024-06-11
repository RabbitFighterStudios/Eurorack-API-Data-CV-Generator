import serial

def send_to_teletype(cv_value, port='/dev/ttyUSB0', baudrate=9600):
    with serial.Serial(port, baudrate) as ser:
        ser.write(f'{cv_value}\n'.encode())

send_to_teletype(pressure_cv)
send_to_teletype(fortnite_cv)
_cv)
