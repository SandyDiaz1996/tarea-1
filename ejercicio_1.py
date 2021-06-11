class Fraccion:
    def __init__(self, numerador, denominador):
        self.numera = numerador
        self.denomi = denominador
    
    def mostrar(self):
        return 'Fracción: {}/{}.'.format(self.numera, self.denomi)
