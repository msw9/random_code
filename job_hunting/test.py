import time
import msvcrt
from bs4 import BeautifulSoup
import requests

def get_html(url):
    r = requests.get(url)
    return r.text
  
with open ("MEMO.txt",encoding='utf-8') as f:
    MEMO = f.read()
    
print(MEMO)

url= "http://w3.erss.univ-tlse2.fr/membre/tanguy/offres.html"

soup = BeautifulSoup(get_html(url),'html.parser')

table = soup.find('table')
premiere_ligne = table.find_all('tr')

if str(premiere_ligne[1]) != MEMO :
    with open("MEMO.txt",mode="w",encoding='utf-8') as f:
        f.write(str(premiere_ligne[1]))
    print("Nouvelle offre d'emploi sur http://w3.erss.univ-tlse2.fr/membre/tanguy/offres.html")
    print("Toucher n'importe quelle touche pour arrêter le code")
    while True:
    	if msvcrt.kbhit():
    		break
