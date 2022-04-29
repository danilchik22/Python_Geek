from abc import ABC, abstractmethod


class Closes(ABC):
    costs = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def cost(self):
        pass


class Coat(Closes):
    def __init__(self, name, V):
        super().__init__(name)
        self.V = V
        Closes.costs += self.cost

    @property
    def cost(self):
        return self.V / 6.5 + 0.5


class Suit(Closes):
    def __init__(self, name, H):
        super().__init__(name)
        self.H = H
        Closes.costs += self.cost

    @property
    def cost(self):
        return 2 * self.H + 0.3


if __name__ == "__main__":
    coat = Coat("Пальто", 3)
    suit = Suit("Костюм", 2)
    print(Closes.costs)
