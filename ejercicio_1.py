class Fraccion:
    def __init__(self, numerador, denominador):
        self.numera = numerador
        self.denomi = denominador
    
    def mostrar(self):
        return 'Fracción: {}/{}.'.format(self.numera, self.denomi)

fraccion1 = Fraccion(5, 8)
fraccion2 = Fraccion(10, 11)
fraccion3 = Fraccion(20, 20)
print('__FRACCIONES__')
print(fraccion1.mostrar())
print(fraccion2.mostrar())
print(fraccion3.mostrar())
