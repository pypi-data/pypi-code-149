# Arvain nominin taivutusluokkaa varten

from .trie import Trie

class Arvain():
    def __init__(self, syöte_sanat, syöte_nimet={}):
        self.sanat = {}
        self.nimet = syöte_nimet
        self.trie = Trie()
        self.astetrie = Trie()
        
        # Sanaston syönti
        
        for sana in syöte_sanat.keys():
            if sana.endswith("-"):
                continue
            if "tn" in syöte_sanat[sana].keys() and syöte_sanat[sana]["tn"].isnumeric() and int(syöte_sanat[sana]["tn"]) > 51:
                continue
            self.sanat[sana] = syöte_sanat[sana]
            if "tn" in syöte_sanat[sana].keys():
                self.trie.add(sana, syöte_sanat[sana]["tn"])
            if "av" in syöte_sanat[sana].keys():
                self.astetrie.add(sana, syöte_sanat[sana]["av"])
        
        self.sanat["inen"] = {"tn":"38"}
        self.sanat["isuus"] = {"tn":"40"}
        self.trie.add("inen", "38")
        self.trie.add("isuus", "40")
        self.trie.compute_value_distributions()
        self.astetrie.compute_value_distributions()

    def normalisoi_konsonanttiloppuiset(self, sana, taivutus):
        # 5 ei lopu vokaaliin, silloin 5b
        if taivutus == "5" and sana[-1] in "qwrpsdfghjklzxcvbnm":
           return "5b"
        elif taivutus == "5" and sana[-1] == "t" and sana[-2] in "qwrtpsdfghjklzxcvbnm":
           return "5b"
        return taivutus
   
    def arvaa(self, sana, **kwargs):

        kwargs = {"tilastollisesti": True} | kwargs

        # Jos ei erikseen kielletty nimeä, katsotaan nimiosumat

        if not "nimi" in kwargs.keys() or kwargs["nimi"]:
            loppuosa = sana.split("-")[-1].split(" ")[-1]
            if loppuosa in self.nimet.keys():
                return self.normalisoi_konsonanttiloppuiset(loppuosa, self.nimet[loppuosa]["tn"])

        taivutus = None
        if sana in self.sanat.keys() and "tn" in self.sanat[sana].keys():
            taivutus = self.sanat[sana]["tn"]
        else:
            ehdokas = self.trie.lookup_by_longest_common_suffix(sana)
            if ehdokas == None and not kwargs["tilastollisesti"]:
                ehdokas = self.trie.lookup_by_longest_common_suffix(sana, False)
            if ehdokas != None:
                taivutus = self.sanat[ehdokas]["tn"]
            else:
                jakauma = self.trie.value_distribution_for_longest_common_suffix(sana)
                paras = 0
                paras_luokka = None
                for key in jakauma.keys():
                    if jakauma[key] > paras:
                        paras_luokka = key
                        paras = jakauma[key]
                        
                taivutus = paras_luokka
    
        return self.normalisoi_konsonanttiloppuiset(sana, taivutus)
    
    def sointuluokka_yksinkertaiselle(self, sana):
        last_front = -1
        last_back = -1
        last_middle = -1 # Unused at this time
        lowered = sana.lower()
        for i in range(len(sana))[::-1]:
            if last_front == -1 and lowered[i] in "äöy":
                last_front = i
            elif last_back == -1 and lowered[i] in "aouå":
                last_back = i
            elif last_middle == -1 and lowered[i] in "ie":
                last_middle = i
        if last_back > last_front:
            return "TAKA"
        else:
            return "ETU"
    
    def arvaa_sointuluokka(self, sana, **kwargs):

        kwargs = {"hiljaa": True} | kwargs

        # Jos ei erikseen kielletty nimeä, katsotaan nimiosumat

        if not "nimi" in kwargs.keys() or kwargs["nimi"]:
            loppuosa = sana.split("-")[-1].split(" ")[-1]
            if loppuosa in self.nimet.keys():
                return self.nimet[loppuosa]["sointu"]

        ehdokas = self.trie.lookup_by_longest_common_suffix(sana[1:], True)
        if ehdokas != None:
            if not kwargs["hiljaa"]:
                print(f"Sanan suffiksisana '{ehdokas}' löytyy sanakirjasta")
            return self.sointuluokka_yksinkertaiselle(ehdokas)
        else:
            if not kwargs["hiljaa"]:
                print(f"Sanaan liittyvää tietoa ei löydy sanakirjasta")
            return self.sointuluokka_yksinkertaiselle(sana)
    
    def arvaa_astevaihteluluokka(self, sana, **kwargs):

        kwargs = {"tilastollisesti": True, "hiljaa": True} | kwargs

        # Jos ei erikseen kielletty nimeä, katsotaan nimiosumat

        if not "nimi" in kwargs.keys() or kwargs["nimi"]:
            loppuosa = sana.split("-")[-1].split(" ")[-1]
            if loppuosa in self.nimet.keys():
                return self.nimet[loppuosa]["av"]

        taivutus = None
        if sana in self.sanat.keys() and "av" in self.sanat[sana].keys():
            if not kwargs["hiljaa"]:
                print(f"{sana}: sukkana")
            taivutus = self.sanat[sana]["av"]
        else:
            ehdokas = self.astetrie.lookup_by_longest_common_suffix(sana)
            if ehdokas == None and not kwargs["tilastollisesti"]:
                if not kwargs["hiljaa"]:
                    print(f"{sana}: yritetään suffiksisanalla")
                ehdokas = self.astetrie.lookup_by_longest_common_suffix(sana, False)
            if ehdokas != None:
                if not kwargs["hiljaa"]:
                    print(f"{sana}: yritetään ei-tilastollisella suffiksilla")
                taivutus = self.sanat[ehdokas]["av"]
            else:
                if not kwargs["hiljaa"]:
                    print(f"{sana}: yritetään tilastollisella suffiksilla")
                jakauma = self.astetrie.value_distribution_for_longest_common_suffix(sana)
                paras = 0
                paras_luokka = None
                for key in jakauma.keys():
                    if jakauma[key] > paras:
                        paras_luokka = key
                        paras = jakauma[key]
                        
                taivutus = paras_luokka
        return taivutus
    
    def arvaa_viimeinen_komponentti(self, sana):
        ehdokas = self.astetrie.lookup_by_longest_common_suffix(sana[1:], True)
        if ehdokas == None:
            return sana
        else:
            return ehdokas
