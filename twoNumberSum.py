import consecutive1s
from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        pass



