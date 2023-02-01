from bs4 import BeautifulSoup as BS
import requests, json, re, random


class Macros:
    def transformArchive(archive: str | dict) -> dict:
        if isinstance(archive, str):
            try:
                with open(archive) as afile:
                    archive: dict = json.load(afile)
            except FileNotFoundError:
                raise FileNotFoundError("Archive file not found") from None
            else:
                return archive
        else:
            return archive

    def checkIfInArchive(archive: dict, num: str) -> dict:
        minidict = {}
        try:
            minidict["name"] = archive[num]["name"]
            minidict["date"] = archive[num]["date"]
        except KeyError:
            raise KeyError("Comic not found in archive, try reloading it") from None
        else:
            return minidict


def parseArchive() -> dict:
    """Parses https://xkcd.com/archive/ for comics.
    Returns a dict with "entries" being the list of entries.
    Each entry is an object with attributes href, date and name.
    Entries are sorted by latest-first, so comic /1/ ends up at the end of the list.
    * href: link to comic (e.g. '/1137/')
    * date: YYYY-MM-DD formatted date of publication
    * name: name of the comic"""
    archive: dict = {}
    archiveDoc = requests.get("https://xkcd.com/archive/").text
    soup = BS(archiveDoc, "html.parser")
    comicContainer = soup.find(id="middleContainer")
    for comicTag in comicContainer.children:
        if comicTag.name == "a":
            archive[comicTag["href"]] = {
                "date": comicTag["title"],
                "name": comicTag.string,
            }
    return archive


def dumpToFile(
    archiveDict: dict, fp: str = "xkcd.json", indent: int | None = None
) -> None:
    """Dump an archive dict as JSON in fp.
    * archiveDict: dict of an archive. Actually, works with any dict, it's a general save function.
    * fp: A filepath to the file. By default saves in the current folder as xkcd.json
    * indent: Amount of spaces to indent the file with, 2 by default. Set to None to remove pretty-printing (saves file space)."""
    try:
        with open(fp, "x") as file:
            json.dump(archiveDict, file, indent=indent)
    except FileExistsError:
        with open(fp, "w") as file:
            json.dump(archiveDict, file, indent=indent)
    return None


def getComicInfo(
    archive: dict | str, comic: int | str = "https://xkcd.com"
) -> dict:
    """Returns an object with info about the comic.
    If not specified - returns last comic's info.
    If comic link isn't correct - returns None.
    * archive: dict or a filepath to an archive dump.
    * comic: Either an int of the comic number, a link, or a /num/ string.
    """

    # Transform archive into a dict
    archive = Macros.transformArchive(archive)

    # Construct link from comic input
    if isinstance(comic, str):
        m = re.match(r"((https?:\/\/)?(xkcd\.com)(\/\d+\/?)?)|(\/\d+\/)|(\d+)", comic)
        if m == None:
            raise ValueError("Comic doesn't match proper formatting")
        m = m[0]
        if m.startswith("http"):
            link = comic
        elif m.startswith("xkcd.com"):
            link = f"https://{m}"
        elif m.startswith("/"):
            link = f"https://xkcd.com{m}"
        elif m[0].isdigit():
            link = f"https://xkcd.com/{m}"
        else:
            raise RuntimeError("How did you get here?")
    elif isinstance(comic, int):
        link = f"https://xkcd.com/{comic}/"

    # Get information from comic's page
    comicInfo = {}
    bob = []
    comicDoc = requests.get(link).text
    soup = BS(comicDoc, "html.parser")
    cc = soup.find(id="middleContainer")
    ntag = cc.find("a", {"href": re.compile(r"https://xkcd.com/")})
    num = "/" + re.search(r"(\d+)", ntag.string)[0] + "/"
    nd = Macros.checkIfInArchive(archive, num)  # nd = namedate

    # Build the comicInfo dict
    comicInfo["num"] = num.strip("/")
    comicInfo["link"] = ntag.string
    comicInfo["name"] = nd["name"]
    comicInfo["date"] = nd["date"]
    comicInfo["image"] = "https:" + cc.find("img")["src"]
    comicInfo["title"] = cc.find("img")["title"]
    return comicInfo


def getRandomComic(
    archive: dict | str, fromArchive: bool = False
) -> dict:
    """Returns a random comic.
    * archive: dict or a filepath to an archive dump.
    * fromArchive: Get a random entry from the archive or from the website. False by default.
    """

    # Transform archive into a dict
    archive = Macros.transformArchive(archive)

    # Get the comic info using getComicInfo()
    if fromArchive:
        c = random.choice(list(archive.keys()))
    else:
        c = requests.get("https://c.xkcd.com/random/comic/").url
    comic = getComicInfo(archive, c)
    return comic
