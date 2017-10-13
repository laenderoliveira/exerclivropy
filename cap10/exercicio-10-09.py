class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adiciona_cidade(self, cidade):
        self.cidades.append(cidade)
    
    def lista_cidades(self):
        for cidade in self.cidades:
            print(f"{cidade.nome} - {self.sigla} ({cidade.populacao} habitantes)")
    
    def populacao(self):
        total = 0
        for cidade in self.cidades:
            total += cidade.populacao
        print(f"População total do Estado {self.sigla}: {total} habitantes")
           
class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

mg = Estado("Minas Gerais", "MG")
cajuru = Cidade("Carmo do Cajuru", 20123)
divinopolis = Cidade("Divinopolis", 245231)
mg.adiciona_cidade(cajuru)
mg.adiciona_cidade(divinopolis)
mg.lista_cidades()
mg.populacao()