import re
from colorama import Fore
import requests

website = "https://www.vulnhub.com/"
resultado = requests.get(website)
content = resultado.text
print(content)