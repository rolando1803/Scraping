import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text

patron = r"/entry/[\w-]*"
maquinas_repetidas=re.findall(patron,str(content))

sin_duplicados = list(set(maquinas_repetidas))

maquinas_final = []

for i in sin_duplicados:
    nombre_maquinas = i.replace("/entry/","")
    maquinas_final.append(nombre_maquinas)
    print(nombre_maquinas)

#################################################

maquina_noob = "maquinaxyz" 
existe_noob = False

for a in maquinas_final:
    if a  == maquina_noob:
        existe_noob=True
        break

color_verde = Fore.GREEN
colo_amarillo=Fore.YELLOW

if existe_noob == True:
    print(color_verde + "no hay maquina nueva")
else:
    print(colo_amarillo + "maquina nueva!!!")


