class Pessoa:
    nacionalidade = 'brasileiro(a)'
    contador = 0
    @classmethod
    def conta_usuarios(cls):
        return f'Há um total de {cls.contador} usuários cadastrados.'
    def __init__(self, nome, peso, altura):
        self.__cont = Pessoa.contador + 1
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        Pessoa.contador = self.__cont

    def imc(self):
        return f'O IMC de {self.__nome} é: {self.__peso / self.__altura ** 2:.2f} ' \
               f'e sua nacionalidade é {Pessoa.nacionalidade}.'


p1 = Pessoa('Paulo', 79, 1.87)
p2 = Pessoa('Fabio', 75, 1.80)
print(p1.imc())
print(p2.imc())
print(Pessoa.conta_usuarios())
