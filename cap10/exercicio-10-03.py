class Televisao:
    """
    Modelagem de uma TV
    """
    def __init__(self, min, max, canal):
        self.ligada = False
        self.canal = canal
        self.cmin = min
        self.cmax = max
    def muda_canal_para_cima(self):
        if (self.canal+1 <= self.cmax):
            self.canal += 1
        else:
            self.canal = self.cmin
    def muda_canal_para_baixo(self):
        if (self.canal-1 >= self.cmin):
            self.canal -= 1
        else:
            self.canal = self.cmax