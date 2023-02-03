def lue_muototiedosto(tiedosto, TIEDOSTOSTA_LÖYTYVÄT_MUODOT=None):

    if TIEDOSTOSTA_LÖYTYVÄT_MUODOT == None:
        from .muodot import TIEDOSTOSTA_LÖYTYVÄT_MUODOT

    # Tiedoston käsittely
    
    with open(tiedosto) as f:
        
        # Jaetaan tiedosto rivistöiksi, jotka kuvaavat taivutusluokan
        
        rivistöt = {}
        rivistö = []
        tunniste = None

        for rivi in f:
            
            # Kommentit
            
            l = rivi.split("#")[0].strip(" \t\n")
            if len(l) == 0:
                continue
            
            # Rivistön käsittely
            
            if l[0].isnumeric():
                if tunniste != None:
                    if tunniste in rivistöt.keys():
                        raise ValueError(f"Tunniste {tunniste} määritelty kahdesti")
                    rivistöt[tunniste] = rivistö[:]
                    rivistö = []
                tunniste = l
            else:
                rivistö.append(l)
        
        # Siivousta
        
        if tunniste != None:
            if tunniste in rivistöt.keys():
                raise ValueError(f"Tunniste {tunniste} määritelty kahdesti")
            rivistöt[tunniste] = rivistö[:]
    
    # Rivistöjen sisältöjen käsittely
    
    tulos = {}
    for tunniste in rivistöt.keys():
        sijat = {}
        if len(rivistöt[tunniste]) != len(TIEDOSTOSTA_LÖYTYVÄT_MUODOT):
            raise ValueError(f"Väärä määrä sijoja määritelty tunnisteelle {tunniste}. \
                               Odotettiin {len(TIEDOSTOSTA_LÖYTYVÄT_MUODOT)}, saatiin {len(rivistöt[tunniste])}.")
        for (nimi, muoto) in zip(TIEDOSTOSTA_LÖYTYVÄT_MUODOT, rivistöt[tunniste]):
            sijat[nimi] = []
            for vaihtoehto in muoto.split(" "):
                if vaihtoehto == "-":
                    sijat[nimi].append("")
                else:
                    sijat[nimi].append(vaihtoehto)
        tulos[tunniste] = sijat
    return tulos
