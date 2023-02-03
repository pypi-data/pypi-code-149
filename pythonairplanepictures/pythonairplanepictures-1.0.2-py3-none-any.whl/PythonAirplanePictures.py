import requests
import random
import re
import os

def getRandomPage(amountOfPages = 1, download = False, printOutput = True):
    allitems = []
    if printOutput:
        print(f"Getting amount of pages on site...")
    response = requests.get(url="https://www.airplane-pictures.net/top-photos.php/top-photos.php?pg=1&limit=all")
    lastPage = re.findall("<td>Page 1 of (.*)</td>", response.text)

    for turn in range(1, amountOfPages + 1):
        randPage = random.randrange(1, int(lastPage[0]))
        if printOutput:
            print(f"Scraping page {randPage}")
        response = requests.get(url=f"https://www.airplane-pictures.net/top-photos.php/top-photos.php?pg={randPage}&limit=all")
        items = re.findall("<img src='(.*)' alt=\".*\" title=\"(.*)\">", response.text)

        for item in items:
            allitems.append(item)

    if download:
        if not os.path.exists(os.path.join(os.getcwd(), "images")):
            os.mkdir(os.path.join(os.getcwd(), "images"))
        curimage = 1
        for item in allitems:
            if printOutput:
                print(f"Saving image {curimage} / {len(allitems)}")
            curimage += 1
            image = requests.get(url=item[0])
            imagename = "".join( x for x in item[1] if (x.isalnum() or x in "._- "))
            with open("./images/" + imagename + ".png", 'wb') as f:
                f.write(image.content)
        
    return allitems

def getTopPages(amountOfPages = 1, download = False, printOutput = True):
    allitems = []

    for page in range(1, amountOfPages + 1):
        if printOutput:
            print(f"Scraping page {page}...")
        response = requests.get(url=f"https://www.airplane-pictures.net/top-photos.php/top-photos.php?pg={page}&limit=all")
        
        items = re.findall("<img src='(.*)' alt=\".*\" title=\"(.*)\">", response.text)

        for item in items:
            allitems.append(item)

    

    if download:
        if not os.path.exists(os.path.join(os.getcwd(), "images")):
            os.mkdir(os.path.join(os.getcwd(), "images"))
        curimage = 1
        for item in allitems:
            if printOutput:
                print(f"Saving image {curimage} / {len(allitems)}")
            curimage += 1
            image = requests.get(url=item[0])
            imagename = "".join( x for x in item[1] if (x.isalnum() or x in "._- "))
            with open("./images/" + imagename + ".png", 'wb') as f:
                f.write(image.content)
    return allitems
