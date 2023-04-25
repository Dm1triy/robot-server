import serial
import time
import multiprocessing


class Accel:
    def __init__(self):
        self.port = '/dev/ttyUSB0'
        self.timeout = 1
        self.is_connected = False
        self.stream = None

        self.last_data = None
        self.is_data_available = False

        self.connect()
        self.run_stream()

    def connect(self):
        try:
            self.stream = serial.Serial(self.port, 9600, timeout=self.timeout)
            self.is_connected = True
        except serial.serialutil.SerialException as err:
            print(f"Unexpected {err=}, {type(err)=}\n")
            print(f"can't listen port {self.port}")
            self.is_connected = False
        time.sleep(1)

    def run_stream(self):
        while self.is_connected:
            is_data_available, period, get_time = self.wait_until_data()
            if not is_data_available:
                self.is_connected = False
                break

            line = self.stream.readline()
            if line[0] != 88:
                print(str(line, "utf-8"))
                continue
            accel = list(map(float, line.strip().split()[1::2]))
            print(f'Get Accelerometer data: X={accel[0]}, Y={accel[1]}, Z={accel[2]}, delay={period}')
            self.last_data = [accel, period, get_time]
            self.is_data_available = True

        print("stream is shout down!")

    def wait_until_data(self, period=0.1):
        start_time = time.time()
        time_ceiling = start_time + self.timeout
        while time.time() < time_ceiling:
            get_time = time.time()
            if self.stream.in_waiting:
                #print(f"Data is ready! get_time: {get_time} \nperiod {get_time-start_time}")
                return True, get_time-start_time, get_time
            time.sleep(period)
        print(f"Timeout {self.port}")
        return False, None, None

    def get_data(self):
        if self.is_data_available:
            return self.last_data
        return None


if __name__ == "__main__":
    test = Accel()
    while True:
        t = test.get_data()
        print(t)

