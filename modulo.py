# importa biblioteca para criação das classes abstratas
from abc import ABC, abstractmethod

# classe abstrata, que irá funcionar como uma interface
class Conta(ABC):
    # interface só possui métodos
    @abstractmethod
    def consultar_saldo(self):
        pass 

    @abstractmethod
    def fazer_deposito(self, valor):
        pass

    @abstractmethod
    def fazer_saque(self, valor):
        pass

# subclasse conta corrente
class ContaCorrente(Conta):
    # atributos
    def __init__(self, nome, cpf, agencia, conta, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo        

    # getter
    @property 
    def nome(self):
        return self.__nome
    
    # setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # getter
    @property 
    def cpf(self):
        return self.__cpf
    
    # setter
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    # getter
    @property 
    def agencia(self):
        return self.__agencia
    
    # setter
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    # getter
    @property 
    def conta(self):
        return self.__conta
    
    # setter
    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    # getter
    @property 
    def saldo(self):
        return self.__saldo
    
    # setter
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # Implementação dos métodos abstratos
    def consultar_saldo(self ):
        return self.__saldo
    
    def fazer_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def fazer_saque(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            return True
        else:
            return False