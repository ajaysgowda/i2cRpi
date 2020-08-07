from interfaces import BaseSensor
from constants import GY521

class TempGy512(BaseSensor):
    def __init__(self):
        self.constants = GY521

    def raw_value(self, ):
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr + 1)
        value = ((high << 8) | low)
        if (value > 32768):
            value = value - 65536
        return value

class MPU