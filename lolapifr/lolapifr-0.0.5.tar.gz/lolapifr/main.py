import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

class fonction:
    "Toutes les fonctions"
    def get_rotation_champion(serveur:str = "euw1") -> dict:
        """
        `entrée str`: serveur (requis) |

        `sortie dict`: requete |

        `pré-condition`: "serveur" doit être le nom d'une région qui appartient à LoL (ex: euw1, eun1...) |

        `post-condition`:

                Renvoie en format dictionnaire les informations sur la rotation des champions gratuit.
                
                Si le paramètre n'est pas respecté alors un message est envoyé avec le message d'erreur.
        """
        serveur = serveur.lower()
        try:
            requete = requests.get("https://"+serveur+".api.riotgames.com/lol/platform/v3/champion-rotations?api_key=" + API_KEY)
            if requete.status_code != 200:
                print("Erreur "+str(requete.status_code)+" ("+requete.reason+")")
            return requete.json()
        except:
            print("Erreur: votre serveur '"+serveur+"' n'est pas valide !")

    def get_derniere_version() -> str:
        """
        `sortie str` |

        `post-condition`: Renvoie la version actuelle de LoL en str.

        Cela peut permettre d'afficher la bonne version des items (en image) pour avoir un bon résultat.
        """
        requete = requests.get("https://ddragon.leagueoflegends.com/api/versions.json")
        try:
            return requete.json()[0]
        except:
            print("Erreur "+str(requete.status_code)+" ("+requete.reason+")")

class summoner:
    "Correspond aux infos d'un joueur"
    def __init__(self, ):
        pass