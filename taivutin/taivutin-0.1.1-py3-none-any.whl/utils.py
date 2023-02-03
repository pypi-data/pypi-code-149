# Sekalaisia pikkufunktioita, joille ei löydy selvempää paikkaa

def muuta_vokaalisointu(sana, sointu):
    if sointu == "ETU":
        return sana.translate("".maketrans("aouAOU", "äöyÄÖY"))
    elif sointu == "TAKA":
        return sana.translate("".maketrans("äöyÄÖY", "aouAOU"))
    else:
        raise ValueError(f"Tuntematon sointutyyppi '{sointu}'.")

def lisää_pääte_vartaloon(vartalo, pääte, sointu):
    
    # Selvitetään sanan viimeinen vokaali
    
    viimeinen_vokaali = "a"
    for m in vartalo[::-1].lower():
        if m in "aeiouäeiöyåüúùûéèëêáàâóòôíìïî":
            viimeinen_vokaali = m
            break
    
    # Toteutetaan $-sääntö (tuhoaa vartalon lopusta merkin)
    
    if "$" in pääte:
        vartalo = vartalo[:-1]
        pääte = "".join(pääte.split("$")) # Poistetaan $-merkit päätteestä

    # Sovelletaan ensin vokaalisointusääntöjä

    vokaalisoinnutettu_pääte = muuta_vokaalisointu(pääte, sointu)
        
    lopullinen_pääte = viimeinen_vokaali.join(vokaalisoinnutettu_pääte.split("+"))
        
    return vartalo + lopullinen_pääte
