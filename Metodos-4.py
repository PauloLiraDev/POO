"""
Método -> Comportamento do objeto (funções).
Em Python, dividimos os métodos em 2 grupos: Métodos de instância e métodos de classe.

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade