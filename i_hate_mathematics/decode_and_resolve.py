import requests
import hashlib
from gazpacho import Soup


# Acessar a página usando cookies de uma página já logada
url = "https://ringzer0ctf.com/challenges/32"
cookies = {"PHPSESSID": "61qotuplj1u6innn61ffhoqdt6"}
html = requests.get(url, cookies=cookies).text
soup = Soup(html)

# Fazer um scrapzinho basico pra pegar o texto que precisa ser hasheado
div = soup.find('div', {'class': 'challenge-wrapper'})
message = div.find('div', {'class': 'message'})
stripped_message = message.strip()

# Remover os marcadores de "begin message" e "end message"
equation = stripped_message.replace("----- BEGIN MESSAGE -----", "")
equation = equation.replace(" ----- END MESSAGE -----", "")
equation = equation.strip()

# Extrair os valores da equação
value_a = equation.split(" + ")[0]
value_b = equation.split(" + ")[1].split(" - ")[0]
value_c = equation.split(" - ")[1].split(" = ")[0]

# A equação sempre segue a regra: <valor_a> + <valor_b> - <valor_c>
# Calcular o resultado, convertendo os valores todos para decimal
result = int(value_a) + int(value_b, 16) - int(value_c, 2)

# Enviar de volta e printar o html resultante
response_url = url + "/" + str(result)
response = requests.get(response_url, cookies=cookies)
print(response.text)

# Utilize algum renderizador html pra facilitar a visualização e achar a flag
# https://htmledit.squarefree.com/
