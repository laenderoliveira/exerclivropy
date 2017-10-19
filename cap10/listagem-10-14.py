class Nome:
    def __init__(self, nome):
        if nome == None or not nome.strip():
            raise ValueError("Nome não pode ser nulo ou branco")
        self.nome = nome
        self.chave = nome.strip().lower()
    def __str__(self):
        return self.nome
    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(id(self),
                                    self.nome, self.chave, type(self).__name__)
    def __eq__(self, outro):
        print("__eq__ Chamado") 
        print(outro)
        return self.nome == outro
    def __lt__(self, outro):
        print("__lt__ Chamado")
        return self.nome < outro