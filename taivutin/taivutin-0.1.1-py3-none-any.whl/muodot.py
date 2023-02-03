TIEDOSTOSTA_LÖYTYVÄT_MUODOT = ("nom", "gen", "part", "ill", "mon nom", "mon gen", "mon part", "mon ill", "ess", "mon iness")
MUOTOJEN_NIMET = []

for muoto in ("nom", "gen", "part", "ess", "iness", "elat", "ill", "ade", "abl", "all", "trans", "ins", "abe", "kom"):
    MUOTOJEN_NIMET.append(muoto)
    MUOTOJEN_NIMET.append("mon " + muoto)

MUOTOJEN_NIMET = tuple(MUOTOJEN_NIMET)

YLEISET_PÄÄTTEET = {
    "iness": "ssa",
    "elat": "sta",
    "ade": "lla",
    "abl": "lta",
    "all": "lle",
    "ess": "na",
    "trans": "ksi",
    "ins": "in", # Onko yksiköllistä?
    "abe": "tta",
    "kom": "ineen", # Onko yksiköllistä?
    "mon elat": "sta",
    "mon ade": "lla",
    "mon abl": "lta",
    "mon all": "lle",
    "mon ess": "na",
    "mon trans": "ksi",
    "mon ins": "n",
    "mon abe": "tta",
    "mon kom": "neen"
}
