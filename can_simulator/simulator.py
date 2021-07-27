import serial

if __name__ == "__main__":
    print("nothing happening yet 😞💔")
    PORT = "COM2"  # example port
    ser = serial.Serial(
        port=PORT, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
    )
    while 1:
        ser.write(b"Hello World")  # writes hello world to the port
    ser.close()  # closes the port
