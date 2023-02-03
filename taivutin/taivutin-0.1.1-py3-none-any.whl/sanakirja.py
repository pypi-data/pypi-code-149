import xml.etree.ElementTree as ET
import csv

# Lukee Kotus-sanalistan ja poimii sieltä hyödylliset tiedot

def lue_sanakirja(polku):
    tree = ET.parse(polku)
    root = tree.getroot()

    sanat = {}

    for word in root:
        assert word.tag == "st"
        word_dict = {}
        exclude = False
        for child in word:
            if child.tag == "s":
                if child.text in ("ismi", "niitti", "nisti", "riitti", "letti", "tiili"): # -geeni -päätteisistä hyväksytään molemmat
                    exclude = True
                    break
                word_dict["s"] = child.text
            if child.tag == "t":
                for t_info in child:
                    if t_info.tag == "tn":
                        word_dict["tn"] = t_info.text
                    if t_info.tag == "av":
                        word_dict["av"] = t_info.text
        if exclude:
            continue
        assert "s" in word_dict.keys()
        sanat[word_dict["s"]] = {}
        if "tn" in word_dict.keys():
            sanat[word_dict["s"]]["tn"] = word_dict["tn"]
        if "av" in word_dict.keys():
            sanat[word_dict["s"]]["av"] = word_dict["av"]
        elif "tn" in word_dict.keys():
            sanat[word_dict["s"]]["av"] = "-"
    return sanat

# rivejä muotoa: sana taivutusnumero astevaihteluluokka

def lue_yksinkertainen_sanakirja(polku):
    sanakirja = {}
    with open(polku, "r") as f:
        for line in f:
            l = line.split("#")[0].strip("\n").strip(" ")
            if len(l) == 0:
                continue
            sana, taivutusnumero, astevaihteluluokka = l.split(" ")
            sanakirja[sana] = {"tn": taivutusnumero, "av": astevaihteluluokka}
    return sanakirja

# CSV-rivejä muotoa: nominatiivi, taivutusluokka, aste, sointu

def lue_csvsanakirja(polku):
    sanakirja = {}
    with open(polku) as tiedosto:
        lukija = csv.reader(tiedosto)
        for nominatiivi, taivutusluokka, aste, sointu in lukija:
            sanakirja[nominatiivi] = {"tn": taivutusluokka, "av": aste, "sointu": sointu}
    return sanakirja

# rivejä, joista löytyy ensin kaikki yksinkön taivutusmuodot välein erotettuina, putki ja sitten kaikki monikon taivutusmuodot välein erotettuina


def lue_poikkeussanakirja(polku, MUOTOJEN_NIMET=None):

    # MUOTOJEN_NIMET ladataan mutkan kautta
    # Tämä kikkailu liittyy vakioiden leivontaan

    if MUOTOJEN_NIMET == None:
        from .muodot import MUOTOJEN_NIMET
    
    # Tiedoston luku
    
    with open(polku, "r") as f:
        tulos = {}
        for rivi in f:
            
            # Kommenttien käsittely
            
            r = rivi.split("#")[0].strip(" \t\n")
            if len(r) == 0:
                continue
            muodot = []
            for a, b in zip(r.split("|")[0].strip().split(" "), r.split("|")[1].strip().split(" ")):
                muodot.extend([a, b])
            tulos[r.split(" ")[0]] = dict(zip(MUOTOJEN_NIMET, muodot))
    
        return tulos
