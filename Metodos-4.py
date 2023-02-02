"""
Método -> Comportamento do objeto (funções).
Em Python, dividimos os métodos em 2 grupos: Métodos de instância e métodos de classe.

Métodos de instância

O método dunder __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir
da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underscore)
OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos. E não é recomendado que criemos dunders,
pois são métodos nativos do Python.

p1 = Produto('Playstation 4', 'VideoGame', 2300)
print(p1.desconto(50))
print(Produto.desconto(p1, 50))
user1 = Usuario('João', 'Alfredo', 'joao@gmail.com', 1234)
print(user1.nome_completo())

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
    print('Usuário criado com sucesso.')
else:
    print('Senha não confere')
    exit()
senha = input('Informe a senha para acesso: ')
if user.checa_senha(senha):
    print('Acesso permitido')
    print(user.senha)
else:
    print('Acesso negado')

# Métodos de classe
user = Usuario('Xablau', 'Lira', 'paulolira@gmail.com', '123456')
Usuario.conta_usuarios()
print(user._Usuario__gera_usuario())

"""
from passlib.hash import pbkdf2_sha256 as cryp

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:
    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return self.__valor * (100 - porcentagem) / 100


class Usuario:
    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos um total de {cls.contador} usuários.')

    @staticmethod
    def definicao():
        return 'Olá'

    def __init__(self, nome, sobrenome, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = cryp.hash(senha, rounds=200000, salt_size=16)
        self.cont = Usuario.contador + 1
        Usuario.contador = self.cont
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.senha):
            return True
        return False

    def __gera_usuario(self):
        return self.email.split('@')[0]


# Método estático
print(Usuario.definicao())