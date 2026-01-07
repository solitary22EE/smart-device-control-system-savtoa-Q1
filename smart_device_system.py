from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self):
        self_on_ = False

    @abstractmethod

    def start(self):
        pass

    @abstractmethod

    def stop(self):
        pass

    def is_on(self):

        return self._is_on
    
    #Moter device class

    
