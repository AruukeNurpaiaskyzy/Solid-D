class ICoffeeMachine:
    def brew(self):
        pass

class EspressoMachine(ICoffeeMachine):
    def brew(self):
        print("Espresso is ready!")

class CoffeeShop:
    def __init__(self, machine: ICoffeeMachine):
        self.machine = machine  # зависит от абстракции

    def serve_coffee(self):
        self.machine.brew()
