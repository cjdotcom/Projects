from bs4 import BeautifulSoup
import requests
import unidecode

def cidade(local):

    process = unidecode.unidecode(local)
    site = f"https://www.tempo.com/{process.lower().replace(' ', '-')}.htm"
    html = requests.get(site).content
    soup = BeautifulSoup(html, 'html.parser')
    cidade = soup.find("h1", class_="titulo")

    return f'{cidade.string}'

def temperatura(local):

    process = unidecode.unidecode(local)
    site = f"https://www.tempo.com/{process.lower().replace(' ', '-')}.htm"
    html = requests.get(site).content
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find("span", class_="dato-temperatura changeUnitT")

    return f'{temp.string}'