from abc import ABC, abstractmethod


class ABSDeck(ABC):
    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def pickACard(self):
        pass


class ABSAcc(ABC):
    @abstractmethod
    def getBalance(self):
        pass

    @abstractmethod
    def setBalance(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
