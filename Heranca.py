"""
A herança é uma forma que temos na orientação a objetos de poder reaproveitar código ou extender classes.
Com a herança, a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e métodos
da classe herdada.
    Cliente:
        -nome;
        -sobrenome;
        -cpf;
        -renda;
    Funcionario:
        -nome;
        -sobrenome;
        -cpf;
        -matricula;

print(cliente1.nome_completo())
print(cliente1.renda())
print(cliente1.nacionalidade)
print(cliente1.__dict__)
print(funcionario1.__dict__)

# Sobrescrita de método, ocorre quando reeescrevemos um método presente na super classe em classes filhas.
"""


class Pessoa:
    nacionalidade = 'brasileiro(a)'

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def cpf(self):
        return self.__cpf


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    def renda(self):
        return self.__renda


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        return f'Funcionário: {self._Pessoa__nome} | Matrícula: {self.__matricula} | {super().cpf()}'


cliente1 = Cliente('Joana', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '123.456.789-00', 23456)
print(funcionario1.nome_completo())