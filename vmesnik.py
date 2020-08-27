from pretvornik import *
import bottle

url = 'http://data.fixer.io/api/latest?access_key=3cadc2f7558a5e2aacc7e73054f1d38d'   
p = Pretvornik(url) 

@bottle.get("/")
def index():
    return bottle.template("index.html")

@bottle.post("/")
def formshandler():
    Valuta1 = bottle.request.forms.getunicode("dropdown1")
    Valuta2 = bottle.request.forms.getunicode("dropdown2")
    količina = bottle.request.forms.getunicode("fname")
    return bottle.template("index.html") + Pretvornik.pretvori(p, Valuta1, Valuta2, float(količina))



bottle.run(debug = True, reloader = True)




