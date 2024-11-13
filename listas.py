frutas = ['Manzana', 'pera', 'kiwi']

# f = input('Ingrese una fruta : ')

# frutas.append(f)
# print(frutas)
# Creacion para los Registros de fruta
class Fruta:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

nom = input("ingrese el nombre de la fruta : ")
col = input("ingrese el color de la fruta : ")

# creo registro de Fruta
f1 = Fruta(nom, col)

frutas.append(f1)

print(frutas) 
print(frutas[3].nombre , frutas[3].color) 