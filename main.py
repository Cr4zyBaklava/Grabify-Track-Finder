import requests
import string
import random

def createID():
    ID = ""
    for i in range(6):
        if random.randint(1, 2) == 1:
            ID += random.choice(string.ascii_uppercase)
        else:
            ID += str(random.choice(string.digits))
    return ID
def trackID(ID):
    url = f"https://grabify.link/track/{ID}"
    r = requests.get(url)
    if "404" not in r.text:
        print(f"{url} -> FOUND !!!")
    else:
        print(url, r)

while True:
    trackID(createID())
