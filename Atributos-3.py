"""
- Atributo -> Características do objeto.
Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;

# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utlizado para a construção do objeto.
# OBS: Self é o próprio objeto executando o método.

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja,
que deve ser acessado somente dentro da própria classe onde está declarado, utiliza-se __ (duplo underscore) no início
de seu nome.
Isso é conhecido também como Name Mangling.

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos
# Atributos sinalizados como privados fora da classe.

# Exemplo

# user = Acesso('user@gmail.com', '123456')
# print(user.__senha) # AttributeError
# user.mostra_email()
# user.mostra_senha()
# print(user._Acesso__senha) # Temos acesso, mas não deveríamos, isso é conhecido como (Name Mangling)

# O que significa atributos de instância?
# Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.

# Atributos de Classe
# São declarados diretamente na classe (fora do construtor). Geralmente já inicializamos um valor
# e este valor, é compartilhado entre todas as instâncias da classe. Ou seja, todas as instâncias terão o mesmo valor
# para tal atributo.


class Produto:

    # Atributo de classe
    imposto = 1.05  # 5% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        Produto.contador = self.id


p1 = Produto('PlayStation 4', 'Console', 2300)
p2 = Produto('Xbox S', 'Console', 4500)

print(p1.id)
print(p2.id)

"""

# Classes com atributos de instância público
class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

#Atributos públicos e privados


class Acesso:
    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.__email)

# Atributos Dinâmicos: Um atributo de instância que pode ser criado em tempo de execução.
# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso.
print(p2.peso)

# Deletando atributos 