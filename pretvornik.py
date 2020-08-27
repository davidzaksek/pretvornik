import requests 
  
class Pretvornik:
    rates = {}  
    def __init__(self, url): 
        podatki = requests.get(url).json() 
        self.rates = podatki["rates"]  

    def pretvori(self, iz_valute, v_valuto, količina): 
        začetna_količina = količina 
        količina = količina / self.rates[iz_valute] 
        količina = int(količina * self.rates[v_valuto] * 100) / 100
        return('{} {} = {} {}'.format(začetna_količina, iz_valute, količina, v_valuto)) 
        