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
        else:
            print(f"Saldo insuficiente! {self.saldo}")
    
    def resumo(self):
        print(f"CC Número: {self.numero} Saldo: R${self.saldo:10.2f}")
        for cliente in self.clientes:
            print("Nome: %s\nTelefone: %s\n" % (cliente.nome, cliente.telefone))

    def extrato(self):
        print(f"\nCC Número: {self.numero}")
        for op, valor in self.operacoes:
            print(f"{op:10} {valor:10.2f}")
        print(f"Saldo: {self.saldo:10.2f}")