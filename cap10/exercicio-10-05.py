class Televisao:
    """
    Modelagem de uma TV
    """
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = 2
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
        
tv_min = Televisao(min=3)
tv_max = Televisao(max=10)
print(f"tv_min = {tv_min.cmin}")
print(f"tv_max = {tv_max.cmax}")