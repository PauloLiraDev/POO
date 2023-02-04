class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        Conta.contador += 1
        self.__limite = limite

    def extrato(self):
        return f'Olá, {self.__titular} seu saldo é de: {self.__saldo}. Seu limite é de {self.__limite}'

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor do depósito precisa ser positivo.')

    def sacar(self, valor):
        if self.__saldo < valor:
            print('Saldo insuficiente.')
        else:
            self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        if self.__saldo < valor:
            print('Não foi possível realizar a transferência.')
        else:
            self.__saldo -= valor
            conta_destino.__saldo += valor
            print(f'Você realizou uma transferência para {conta_destino.__titular} no valor de {valor}')


cc = Conta('Mario', 2000, 5000)
cc2 = Conta('Joana', 1500, 5000)
print(cc2.extrato())
cc.transferir(1500, cc2)
print(cc2.extrato())