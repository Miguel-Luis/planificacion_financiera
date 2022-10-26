from abc import abstractmethod
from abc import ABCMeta

class Nomina:
    def __str__(self):
        pass

    @abstractmethod
    def perfilar(self):
        pass

    @abstractmethod
    def get_retorno_obligatorias(self):
        pass

    @abstractmethod
    def get_mesada(self):
        pass
