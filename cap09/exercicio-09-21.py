agenda = []


def pedenome():
    return input("Nome: ").replace("#", "$")


def pedetelefone():
    return input("Telefone: ").replace("#", "$")


def pedearquivo():
    return input("Nome do arquivo: ")


def mostra(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")


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

    if p is not None:
        m = "Certeza que quer excluir? (1 - Para confirmar / 0 - para sair): "
        valor = faixa(m, 0, 1)
        if valor == 1:
            del agenda[p]
        else:
            print("Não foi apagado!")
    else:
        print("Nome não encontrado.")


def altera():
    p = pesquisa(pedenome())
    if p is not None:
        print("Encontrado!")
        nome = agenda[p][0]
        telefone = agenda[p][1]
        mostra(nome, telefone)
        nome = pedenome()
        telefone = pedetelefone()
        m = "Certeza que quer alterar? (1 - Para confirmar / 0 - para sair): "
        valor = faixa(m, 0, 1)
        if valor == 1:
            agenda[p] = [nome, telefone]
        else:
            print("Não alterado!")
    else:
        print("Não encontrado")


def lista():
    print("\nAgenda\n")
    print("-"*6)
    for n, d in enumerate(agenda):
        nome, telefone = d
        print(n+1, end=' ')
        mostra(nome, telefone)
    print("-"*6)


def grava():
    nomearquivo = pedearquivo()
    arquivo = open(nomearquivo, "w")
    for nome, telefone in agenda:
        arquivo.write(f"{nome}#{telefone}\n")
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
            print(f"Valor inválido, favor digitar valor entre {i} e {f}")


def ordena():
    global agenda
    agenda.sort()
    lista()


def menu():
    print("""
    0 - Sair
    1 - Novo
    2 - Alterar
    3 - Excluir
    4 - Lista
    5 - Grava
    6 - Lê
    7 - Ordena por Nome
    """)
    la = len(agenda)
    print(f"{la} contato(s) na agenda.")
    return faixa("Escola uma opção: ", 0, 7)


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
    elif opcao == 7:
        ordena()
