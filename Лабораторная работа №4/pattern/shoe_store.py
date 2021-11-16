from __future__ import annotations
from abc import ABC, abstractmethod


class ShoesFactory(ABC):
    @abstractmethod
    def createsneakers(self):
        pass

    @abstractmethod
    def createslates(self):
        pass


class Nikefactory(ShoesFactory):

    def createsneakers(self):
        return Nikesneakers()

    def createslates(self):
        return Nikeslates()


class Adidasfactory(ShoesFactory):

    def createsneakers(self):
        return Adidassneakers()

    def createslates(self):
        return Adidasslates()


class sneakers(ABC):
    def color_sneakers(self):
        self.color = input()
        return self.color

    @abstractmethod
    def receiving_sneakers(self):
        pass


class Adidassneakers(sneakers):
    def receiving_sneakers(self):
        return ("Create Adidassneakers")


class Nikesneakers(sneakers):
    def receiving_sneakers(self):
        return ("Create Nikesneakers")


class slates(ABC):
    @abstractmethod
    def receiving_slates(self):
        pass

    @abstractmethod
    def style_slates(self, collaborator: sneakers):
        pass


class Nikeslates(slates):
    def receiving_slates(self):
        return ("Create Nikeslates")

    def style_slates(self, collaborator=sneakers):
        return 'Цвет кроссовок был {}'.format(collaborator.color_sneakers())


class Adidasslates(slates):
    def receiving_slates(self):
        return ("Create Adidasslates")

    def style_slates(self, collaborator=sneakers):
        return 'Цвет кроссовок был {}'.format(collaborator.color_sneakers())


def client_code(ShoesFactory):
    sneaker = ShoesFactory.createsneakers()
    print(sneaker.receiving_sneakers())
    slate = ShoesFactory.createslates()
    print(slate.style_slates(sneaker))
    print(slate.receiving_slates())


if __name__ == "__main__":
    """
    Клиентский код может работать с любым конкретным классом фабрики.
    """
    print("Тест первого производства:")
    client_code(Nikefactory())
    print("\n")
    print("Тест второго производства:")
    client_code(Adidasfactory())
