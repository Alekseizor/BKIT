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


class Adaptee:
    def receiving_sneakers_new(self):
        return ('new factory')


class Adapter(Nikesneakers, Adaptee):
    def receiving_sneakers(self):
        return self.receiving_sneakers_new()


def client_code():
    sneaker = Nikefactory().createsneakers()
    print(sneaker.receiving_sneakers())
    sneaker_new = Adapter().receiving_sneakers()
    print(sneaker_new)
    sneaker_new_color = Adapter().color_sneakers()
    print(sneaker_new_color)
if __name__ == "__main__":
    client_code()
