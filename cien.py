import json
import os
import sys

class Conjunto100Numeros:
    def __init__(self, archivo='estado_conjunto.json'):
        self.archivo = archivo
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                datos = json.load(f)
                self.numeros = set(datos['numeros'])
                self.extraido = datos['extraido']
        else:
            self.numeros = set(range(1, 101))
            self.extraido = None

    def guardar_estado(self):
        with open(self.archivo, 'w') as f:
            json.dump({
                'numeros': list(self.numeros),
                'extraido': self.extraido
            }, f)

    def extract(self, numero):
        if not (1 <= numero <= 100):
            raise ValueError("el numero debe estar entre 1 y 100")
        if numero not in self.numeros:
            raise ValueError("el numero ya ha sido extraido o no esta en el rango")
        self.numeros.remove(numero)
        self.extraido = numero
        self.guardar_estado()

    def calcular_numero_extraido(self):
        if self.extraido is None:
            raise ValueError("no se extrajo ningún numero")
        return self.extraido

    def mostrar_numero_extraido(self):
        try:
            numero = self.calcular_numero_extraido()
            print(f"el numero extraido es: {numero}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <numero_a_extraer>")
        sys.exit(1)

    try:
        numero_a_extraer = int(sys.argv[1])
    except ValueError:
        print("debe ser un numero entero")
        sys.exit(1)

    conjunto = Conjunto100Numeros()
    try:
        conjunto.extract(numero_a_extraer)
        conjunto.mostrar_numero_extraido()
    except ValueError as e:
        print(e)
