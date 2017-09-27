# Na função de leitura do arquivo, o split gera mais parametros, ocasionando o erro de ValueError
# Minha solução é na função que pede a entrada de dados subistituir a tralha por um outro carcter especial
agenda = []


def pedenome():
    return input("Nome: ").replace("#", "$")


def pedetelefone():
    return input("Telefone: ").replace("#", "$")


def pedearquivo():
    return input("Nome do arquivo: ")


def mostra(nome, telefone):
    print("Nome: {} Telefone: {}".format(nome, telefone))


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    nome = pedenome()
    telefone = pedetelefone()
    agenda.append([nome, telefone])


def apaga():
    nome = pedenome()
    p = pesquisa(nome)
    if p != None:
        del agenda[p]
    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pedenome())
    if p != None:
        print("Encontrado!")
        nome = agenda[p][0]
        telefone = agenda[p][1]
        mostra(nome, telefone)
        nome = pedenome()
        telefone = pedetelefone()
        agenda[p] = [nome, telefone]
    else:
        print("Não encontrado")


def lista():
    print("\nAgenda\n")
    print("-"*6)
    for nome, telefone in agenda:
        mostra(nome, telefone)
    print("-"*6)


def grava():
    nomearquivo = pedearquivo()
    arquivo = open(nomearquivo, "w")
    for nome, telefone in agenda:
        arquivo.write("{}#{}\n".format(nome, telefone))
    arquivo.close()


def le():
    global agenda
    agenda = []
    nomearquivo = pedearquivo()
    arquivo = open(nomearquivo, "r")
    for linha in arquivo.readlines():
        nome, telfone = linha.strip().split("#")
        agenda.append([nome, telfone])
    arquivo.close()

def faixa(pergunta, i, f):
    while True:
        try:
            valor = int(input(pergunta))
            if valor >= i and valor <= f:
                return valor
        except ValueError:
            print("Valor inválido, favor digitar valor entre {} e {}".format(i, f))

def menu():
    print("""
    0 - Sair
    1 - Novo
    2 - Alterar
    3 - Excluir
    4 - Lista
    5 - Grava
    6 - Lê
    """)
    print("{} contato(s) na agenda.".format(len(agenda)))
    return faixa("Escola uma opção: ", 0, 6)

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
