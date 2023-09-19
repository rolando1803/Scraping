import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text

patron = r"/entry/[\w-]*"
maquinas_repetidas=re.findall(patron,str(content))
print(maquinas_repetidas)

