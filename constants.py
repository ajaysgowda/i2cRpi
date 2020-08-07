from interfaces import Singleton

class GY521(Singleton):
    PWR_M = 0x6B
    DIV = 0x19
    CONFIG = 0x1A
    GYRO_CONFIG = 0x1B
    INT_EN = 0x38
    ACCEL_X = 0x3B
    ACCEL_Y = 0x3D
    ACCEL_Z = 0x3F
    GYRO_X = 0x43
    GYRO_Y = 0x45
    GYRO_Z = 0x47