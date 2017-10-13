class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 4
        self.marca = "Panasonic"
        self.tamanho = 32

tv_sala = Televisao()
tv_sala.marca = "Sony"
tv_sala.tamanho = 59
print(tv_sala.marca)
print(tv_sala.tamanho)

tv_quarto = Televisao()
tv_quarto.marca = "Samsung"
tv_quarto.tamanho = 47
print(tv_quarto.marca)
print(tv_quarto.tamanho)