ASTE_HEIKOSTA_VAHVAKSI = {
"nom":   "A", # haMMas
"gen":   "B", # haMPaan
"part":  "A", # haMMasta
"ess":   "B", # haMPaana
"iness": "B", # haMPaassa
"elat":  "B", # haMPaasta
"ill":   "B", # haMPaahan/seen
"ade":   "B", # haMPaalla
"abl":   "B", # haMPaallta
"all":   "B", # haMPaalle
"trans": "B", # haMPaaksi
"ins":   "B", # haMPain
"abe":   "B", # haMPaatta
"kom":   "B"  # haMPaineen

# Monikot aina B
    
}

ASTE_VAHVASTA_HEIKOKSI = {
"nom":   "A", # soMPa
"gen":   "B", # soMMan
"part":  "A", # soMPaa
"ess":   "A", # soMPana
"iness": "B", # soMMassa
"elat":  "B", # soMMasta
"ill":   "A", # soMPaan
"ade":   "B", # soMMalla
"abl":   "B", # soMMalta
"all":   "B", # soMMalle
"trans": "B", # soMMaksi
"ins":   "B", # soMMin
"abe":   "B", # soMMitta
"kom":   "A",  # soMPineen
    
"mon nom":   "B", # soMMat
"mon gen":   "A", # soMPien
"mon part":  "A", # soMPia
"mon ess":   "A", # soMPina
"mon iness": "B", # soMMissa
"mon elat":  "B", # soMMista
"mon ill":   "A", # soMPiin
"mon ade":   "B", # soMMilla
"mon abl":   "B", # soMMilta
"mon all":   "B", # soMMilla
"mon trans": "B", # soMMiksi
"mon ins":   "B", # soMMin
"mon abe":   "B", # soMMitta
"mon kom":   "A"  # soMPineen
}

ASTEET = {"-": ("", "")}

for i, pari in enumerate([("kk", "k"),
                          ("pp", "p"),
                          ("tt", "t"),
                          ("k", ""),
                          ("p", "v"),
                          ("t", "d"),
                          ("nk", "ng"),
                          ("mp", "mm"),
                          ("lt", "ll"),
                          ("nt", "nn"),
                          ("rt", "rr"),
                          ("k", "j"),
                          ("k", "v")]):
    ASTEET[chr(ord('A')+i)] = pari


def astetila(sija, suunta):
    if suunta == "H->V" and sija.startswith("mon"): # Kaikki säänöllisiä
        return "B"
    else:
        if suunta == "H->V":
            return ASTE_HEIKOSTA_VAHVAKSI[sija]
        else:
            return ASTE_VAHVASTA_HEIKOKSI[sija]

def astemuutos(sija, suunta, asteluokka):
    if asteluokka == "-": # Luokka ei taivu
        return None
    tila = astetila(sija, suunta)
    if tila == "A": # nominatiivi (=juuri) on samassa muodossa
        return None
    muutos = ASTEET[asteluokka]
    if suunta == "V->H":
        return muutos
    else:
        return (muutos[1], muutos[0])

def etsi_kuvio(vartalo, kuvio):
    # O(n^2) haku, mutta n on sairaan pieni (< 5)
    
    kuvion_alku = None
    for i in range(len(vartalo)-len(kuvio)+1)[::-1]:
        if vartalo[i:i+len(kuvio)] == kuvio:
            kuvion_alku = i
            break
    return kuvion_alku
    
def toteuta_astevaihtelu(vartalo, muutos, kotus_tyyppi):

    if kotus_tyyppi == "48" and muutos == ("", "k"):
        return vartalo[:-1] + "k" + vartalo[-1]

    if muutos == None:
        return vartalo
    
    if muutos[0] == "":
        return vartalo + muutos[1]
    
    kuvion_alku = etsi_kuvio(vartalo.lower(), muutos[0])
    
    if kuvion_alku == None: # Hudin tapauksessa fiksuinta on luovuttaa
        return vartalo
    
    tulos = vartalo[:kuvion_alku] + muutos[1]
    if len(vartalo) > kuvion_alku + len(muutos[0]):
        tulos += vartalo[kuvion_alku + len(muutos[0]):]
    
    return tulos

def arvaa_astesuunta(vartalo, asteluokka, kotus_tyyppi=None):
    if asteluokka == "-":
        return "H->V" # Triviaalinen
    if kotus_tyyppi == "48" and asteluokka == "D":
        return "H->V" # Luotettava
    kuviot = ASTEET[asteluokka]
    if kuviot[1] == "": # Kiusallinen tilanne
        kuvion_alku = etsi_kuvio(vartalo, kuviot[0])
        if kuvion_alku != None and len(vartalo) - kuvion_alku < 4:
            return "V->H"
        else:
            return "H->V" # Kiusallinen tilanne
    
    osuma_a = etsi_kuvio(vartalo, kuviot[0])
    osuma_b = etsi_kuvio(vartalo, kuviot[1])
    
    # Kaikki kuviot ovat muodossa kk, k -> oikea voi olla osa vasenta, muttei toisin päin
    # Tällöin mätsätään pidempi, jos lyhyempi mätsäsi sen lopun
    
    if kuviot[1] in kuviot[0] and osuma_a != None and osuma_a == osuma_b - (len(kuviot[0]) - len(kuviot[1])):
        return "V->H"
    
    # Muuten mätsätään vain sijainnin pohjalta
    
    if osuma_a == None:
        osuma_a = -1
    
    if osuma_b == None:
        osuma_b = -1
    
    if osuma_a < osuma_b:
        return "H->V"
    else:
        return "V->H"
