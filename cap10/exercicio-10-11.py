class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPOSITO", valor])
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print("Saldo insuficiente!")
            return False
    
    def resumo(self):
        print(f"CC Número: {self.numero} Saldo: R${self.saldo:10.2f}")
        for cliente in self.clientes:
            print("Nome: %s\nTelefone: %s\n" % (cliente.nome, cliente.telefone))

    def extrato(self):
        print(f"\nCC Número: {self.numero}")
        for op, valor in self.operacoes:
            print(f"{op:10} {valor:10.2f}")
        print(f"Saldo: {self.saldo:10.2f}")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            return Conta.saque(self, valor)
    def extrato(self):
        Conta.extrato(self)
        print(f"Limite: {self.limite}")
        print(f"Disponível Saque: {self.limite + self.saldo}")

laender = ContaEspecial([Cliente("Laender", "991510701")], 42991, 500, 200)
laender.resumo()
laender.saque(10000)
laender.resumo()
laender.extrato()