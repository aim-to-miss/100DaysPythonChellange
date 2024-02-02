class Car:
    __match_args__ = ('brand', 'model', 'milage')
    def __init__(self, brand, model, milage):
        self.brand = brand
        self.model = model
        self.milage = milage


def matchMe(car):
    match car:
        case Car('Toyota','Allion',25):
            print('My Friend\'s Car!')
        case Car('Audi','A8',10):
            print('Your Car!')
        case Car (var1, var2, var3) if var1 != "":
            print('Others car: Brand ', var1, 'Model ', var2,' Milage ', var3)
        case Car():
            print("My parking space but no Car!")
        case _:
            print("If nothing matches! Still there is hope.")

cases = [
    Car("","",0),
    Car("Toyota","Allion", 25),
    Car("Audi","A8",10),
    Car("Toyota","Rush",14),
    Car("Mahindra", "Centuro", 25)
    ]

for case in cases:
    matchMe(case)

