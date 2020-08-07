from abc import abstractmethod
# --------------------------------------------------------------------------- #
# Generic
# --------------------------------------------------------------------------- #
class Singleton(object):
    """
    Singleton base class
    """
    def __new__(cls, *args, **kwargs):
        """ Create a new instance
        """
        if '_inst' not in vars(cls):
            cls._inst = object.__new__(cls)
        return cls._inst


class BaseSensor:

    def __init__(self):
        """
        constructor
        """
        pass

    @abstractmethod
    def raw_value(self):
        """
        get raw value from sensor
        :return: NotImplementedError
        """
        raise NotImplementedError

    @abstractmethod
    def _scale(self):
        """
        scale
        :return: NotImplementedError
        """
        raise NotImplementedError

    @abstractmethod
    def scaled_value(self):
        """
        return scaled value
        :return: NotImplementedError
        """
        raise NotImplementedError


