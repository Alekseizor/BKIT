class ShoesFactory:
    def Factory(self):
        return ('classic factory')

    def color(self):
        return ('красный')


class Adaptee:
    def Factory_new(self):
        return ('new factory')


class Adapter(ShoesFactory, Adaptee):
    def Factory(self):
        return self.Factory_new()


def client_code(factory=ShoesFactory):
    print(factory.Factory())


if __name__ == "__main__":
    Sneaker = ShoesFactory()
    print(Sneaker.Factory())
    adapt = Adaptee()
    print(adapt.Factory_new())
    adapter = Adapter()
    print(adapter.Factory(), adapter.color())