from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionarConta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, dataNascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = dataNascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeuSaldo = valor > saldo

        if (excedeuSaldo):
            print('\n===== ERRO! VOCÊ NÃO TEM SALDO SUFICIENTE!! =====')
            
        elif (valor > 0):
            self._saldo -= valor
            print('\n===== SUCESSO, OPERAÇÃO EXECUTADA! =====')
            return True

        else:
            print('\n===== ERRO, INFORME UM VALOR VÁLIDO! =====')

        return False

    def depositar(self, valor):
        
        if (valor > 0):
            self._saldo += valor
            print('\n===== SUCESSO, OPERAÇÃO EXECUTADA! =====')
        else:
            print('\n===== ERRO, INFORME UM VALOR VÁLIDO! =====')
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limiteSaques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limiteSaques = limiteSaques

    def sacar(self, valor):
        numeroSaques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeuLimite = valor > self.limite
        excedeuSaques = numeroSaques >= self.limiteSaques

        if excedeuLimite:
             print('\n===== ERRO! O VALOR DO SAQUE EXCEDE O LIMITE! =====')

        elif excedeuSaques:
            print('\n===== ERRO! QUANTIDADE DE SAQUE EXCEDIDA, VOLTE AMANHÃ! =====')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return '''
            AGÊNCIA:\t{}
            C/C:\t\t{}
            TITULAR:\t{}
        '''.format(self.agencia, self.numero, self.cliente.nome)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionarTransacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%s'),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucessoTransacao = conta.sacar(self.valor)

        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucessoTransacao = conta.depositar(self.valor)

        if sucessoTransacao:
            conta.historico.adicionarTransacao(self)