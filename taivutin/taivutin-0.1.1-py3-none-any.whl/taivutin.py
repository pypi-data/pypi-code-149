import os
from .asteet import arvaa_astesuunta, toteuta_astevaihtelu, astemuutos
from .arvain import Arvain
from .sanakirja import lue_sanakirja, lue_poikkeussanakirja, lue_yksinkertainen_sanakirja
from .utils import lisää_pääte_vartaloon
from .muodot import TIEDOSTOSTA_LÖYTYVÄT_MUODOT, MUOTOJEN_NIMET, YLEISET_PÄÄTTEET
from .vakiot import MUODOT

from .vakiot import POIKKEUKSET

# Nominispesifejä, mutta tilattomia

def lisää_sijapääte_vartaloon(sijat, vartalo, sija, kotus_tyyppi, sointu):

    if sija in ("kom", "ins"):
        sija = "mon " + sija
    
    if sija not in MUOTOJEN_NIMET:
        ValueError(f"Tuntematon sija {sija}. Mahdolliset vaihtoehdot: {MUOTOJEN_NIMET}")
    if not kotus_tyyppi in sijat.keys():
        ValueError(f"Tuntematon taivutusluokka {kotus_tyyppi}. Mahdolliset vaihtehdot: {sijat.keys()}")

    pääte = None
    
    if sija in TIEDOSTOSTA_LÖYTYVÄT_MUODOT:
        pääte = sijat[kotus_tyyppi][sija][0]
    else:
        if sija in ("iness", "elat", "ade", "abl", "all", "trans", "abe"):
            gen_pääte = sijat[kotus_tyyppi]["gen"][0]
            pääte = gen_pääte[:max(len(gen_pääte)-1, 0)] + YLEISET_PÄÄTTEET[sija]
        elif sija.split(" ")[-1] in ("elat", "ade", "abl", "all", "trans", "abe", "ins", "kom", "ess"):
            mon_iness_pääte = sijat[kotus_tyyppi]["mon iness"][0]
            pääte = mon_iness_pääte[:max(len(mon_iness_pääte)-3, 0)] + YLEISET_PÄÄTTEET[sija]
            if sijat[kotus_tyyppi]["mon iness"][0].startswith("$"):
                pääte = "$" + pääte
        else:
            pääte = YLEISET_PÄÄTTEET[sija]
    
    return lisää_pääte_vartaloon(vartalo, pääte, sointu)

def lisää_sijapääte_perusmuotoon(sijat, perusmuoto, sija, kotus_tyyppi, asteluokka, sointu):
    
    astesuunta = arvaa_astesuunta(perusmuoto, asteluokka, kotus_tyyppi)
    astemuunnos = astemuutos(sija, astesuunta, asteluokka)
    
    if sija == "nom":
        return perusmuoto # Ei turhaa töhöä
    nom_pituus = len(sijat[kotus_tyyppi]["nom"][0])
    vartalo = perusmuoto[:-nom_pituus]
    if sijat[kotus_tyyppi]["nom"][0] == "":
        vartalo = perusmuoto
    
    vartalo = toteuta_astevaihtelu(vartalo, astemuunnos, kotus_tyyppi)
    
    return lisää_sijapääte_vartaloon(sijat, vartalo, sija, kotus_tyyppi, sointu)

class Taivutin():
    def __init__(self, arvain=None):

        # Jos arvainta ei anneta, luetaan sisäänrakennettu sanakirja ja poikkeukset

        if arvain == None:
            from .vakiot import SANATRIE, NIMET
            arvain = Arvain(SANATRIE, NIMET)

        self.arvain = arvain
        
        self.mallit = {}

        for muoto in MUOTOJEN_NIMET:
            self.mallit[self.taivuta("talo", muoto)] = muoto

    def taivuta(self, sana, muoto, **kwargs):

        # Jos käyttäjä pyysi taivuttamaan mallin mukaan, päättele muoto

        if muoto in self.mallit.keys():
            muoto = self.mallit[muoto]

        if sana in POIKKEUKSET.keys():
            return POIKKEUKSET[sana][muoto]

        # Tietty joukko parametrejä eteenpäin arvaimelle

        jatkoparametrit = { avain: kwargs[avain] for avain in kwargs
                                                 if avain in ["nimi"] }

        if "taivutusluokka" not in kwargs.keys():
            kotus_type = self.arvain.arvaa(sana, **jatkoparametrit)
        else:
            kotus_type = self.arvain.normalisoi_konsonanttiloppuiset(sana, kwargs["taivutusluokka"])
        
        if kotus_type == "50": # Yhdysnomini, jonka jälkimmäinen osa taipuu
            ehdokas = self.arvain.arvaa_viimeinen_komponentti(sana)
            if ehdokas == sana: # Ei päästä puusta pitkälle
                kotus_type = self.arvain.arvaa(sana[-2:], **jatkoparametrit) # Arvataan kahden viimeisen merkin perusteella
            else:
                alku = sana[:-len(ehdokas)] # Erotetaan alkuosa
                loppu = self.taivuta(ehdokas, muoto) # Taivutetaan loppu (ja arvataan sille samalla uusi taivutustyyppi)
                return alku + loppu
        elif kotus_type == "51": # Yhdysnomini, jonka molemmat osat taipuvat
            ehdokas = self.arvain.arvaa_viimeinen_komponentti(sana)
            if ehdokas == sana: # Ei päästä puusta pitkälle
                kotus_type = self.arvain.arvaa(sana[-2:], **jatkoparametrit) # Arvataan kahden viimeisen merkin perusteella
            else:
                alku = self.taivuta(sana[:-len(ehdokas)], muoto) # Erotetaan alkuosa
                loppu = self.taivuta(ehdokas, muoto) # Taivutetaan loppu (ja arvataan sille samalla uusi taivutustyyppi)
                return alku + loppu

        if "sointu" not in kwargs.keys():
            harmony = self.arvain.arvaa_sointuluokka(sana, **jatkoparametrit)
        else:
            harmony = kwargs["sointu"]
        if "asteluokka" not in kwargs.keys():
            gradation_class = self.arvain.arvaa_astevaihteluluokka(sana, **jatkoparametrit)
        else:
            gradation_class = kwargs["asteluokka"]
        
        # Monikolliset sanat
        
        if sana.endswith(MUODOT[kotus_type]["mon nom"][0]):
            sana = sana[:-len(MUODOT[kotus_type]["mon nom"][0])]
            
            gradation_direction = arvaa_astesuunta(sana, gradation_class, kotus_type)
            gradation_transformation = astemuutos("mon nom", gradation_direction, gradation_class)
    
            sana = toteuta_astevaihtelu(sana, gradation_transformation, kotus_type)
            
            sana += MUODOT[kotus_type]["nom"][0]
            if muoto.split(" ")[0] != "mon":
                muoto = "mon " + muoto
        
        return lisää_sijapääte_perusmuotoon(MUODOT, sana, muoto, kotus_type, gradation_class, harmony)
