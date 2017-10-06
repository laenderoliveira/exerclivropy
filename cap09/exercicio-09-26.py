agenda = []
gravou = True


def pedenome(op=""):
    i = input("Nome: ").replace("#", "$")
    if i == "":
        i = op
    return i


def pedetelefone(op=""):
    i = input("Telefone: ").replace("#", "$")
    if i == "":
        i = op
    return i

def pedeaniversario():
    return input("Aniversário Ex 27/03/1998: ")


def pedeemail():
    return input("Email: ")


def pedearquivo():
    return input("Nome do arquivo: ")


def mostra(nome, telefone, aniversario, email):
    print(f"Nome: {nome} Telefone: {telefone} Niver: {aniversario} Email: {email}")


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None


def verifica_repetido(nome):
    for contato in agenda:
        if contato[0].lower() == nome.lower():
            print("Nome já existe!")
            return False
    return True

def novo():
    global gravou
    nome = pedenome()
    if verifica_repetido(nome):
        telefone = pedetelefone()
        aniversario = pedeaniversario()
        email = pedeemail()
        agenda.append([nome, telefone, aniversario, email])
        gravou = False


def apaga():
    global gravou
    nome = pedenome()
    p = pesquisa(nome)

    if p is not None:
        m = "Certeza que quer excluir? (1 - Para confirmar / 0 - para sair): "
        valor = faixa(m, 0, 1)
        if valor == 1:
            del agenda[p]
            gravou = False
        else:
            print("Não foi apagado!")
    else:
        print("Nome não encontrado.")


def altera():
    global gravou
    p = pesquisa(pedenome())
    if p is not None:
        print("Encontrado!")
        nome = agenda[p][0]
        telefone = agenda[p][1]
        aniversario = agenda[p][2]
        email = agenda[p][3]
        mostra(nome, telefone, aniversario, email)
        nome = pedenome()
        telefone = pedetelefone()
        aniversario = pedeaniversario()
        email = pedeemail()
        m = "Certeza que quer alterar? (1 - Para confirmar / 0 - para sair): "
        valor = faixa(m, 0, 1)
        if valor == 1:
            agenda[p] = [nome, telefone, aniversario, email]
            gravou = False
        else:
            print("Não alterado!")
    else:
        print("Não encontrado")


def lista():
    print("\nAgenda\n")
    print("-"*6)
    for n, d in enumerate(agenda):
        nome, telefone, aniversario, email = d
        print(n+1, end=' ')
        mostra(nome, telefone, aniversario, email)
    print("-"*6)


def grava():
    global gravou
    if gravou is False:
        nomearquivo = pedearquivo()
        arquivo = open(nomearquivo, "w")
        for nome, telefone, aniversario, email in agenda:
            arquivo.write(f"{nome}#{telefone}#{aniversario}#{email}\n")
        arquivo.close()
        gravou = True
        grava_ultima_agenda(nomearquivo)
    else:
        print("Conteudo ja gravado")


def leia_arquivo(nomearquivo):
    global agenda
    agenda = []
    nomearquivo = nomearquivo
    arquivo = open(nomearquivo, "r")
    for linha in arquivo.readlines():
        nome, telefone, aniversario, email = linha.strip().split("#")
        agenda.append([nome, telefone, aniversario, email])
    arquivo.close()


def le():
    global agenda, gravou
    if gravou is False:
        print("Grave a agenda primeiro (Opção 5)")
    else:
        agenda = []
        nomearquivo = pedearquivo()
        leia_arquivo(nomearquivo)
        grava_ultima_agenda(nomearquivo)


def ultima_agenda():
    try:
        file = open("ultimaagenda.txt", "r")
        ultima = file.readline().strip()
        file.close()
        return ultima
    except:
        return None


def grava_ultima_agenda(nome):
    file = open("ultimaagenda.txt", "w")
    file.write(nome)
    file.close()


def le_ultima_agenda():
    ultima = ultima_agenda()
    if ultima is not None:
        leia_arquivo(ultima)


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


le_ultima_agenda()

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
