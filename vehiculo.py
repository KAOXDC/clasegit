class Vehiculo:

    def __init__(self, marca, cilindraje):
        self.marca = marca
        self.cilindraje = cilindraje


v1 = Vehiculo('Ford', 1600)
v2 = Vehiculo('Kia', 1400)

print(v1.marca, v1.cilindraje)