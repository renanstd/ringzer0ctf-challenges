import requests
import hashlib
from gazpacho import Soup


# Acessar a página usando cookies de uma página já logada
url = "https://ringzer0ctf.com/challenges/13"
cookies = {"PHPSESSID": "61qotuplj1u6innn61ffhoqdt6"}
html = requests.get(url, cookies=cookies).text
soup = Soup(html)

# Fazer um scrapzinho basico pra pegar o texto que precisa ser hasheado
div = soup.find('div', {'class': 'challenge-wrapper'})
message = div.find('div', {'class': 'message'})
stripped_message = message.strip()

# Remover os marcadores de "begin message" e "end message"
to_hash = stripped_message.replace("----- BEGIN MESSAGE -----", "")
to_hash = to_hash.replace(" ----- END MESSAGE -----", "")
to_hash = to_hash.strip()

# Hashear a mensagem
hashed_string = hashlib.sha512(to_hash.encode())
hashed_string = hashed_string.hexdigest()

# Enviar de volta e printar o html resultante
response_url = url + "/" + hashed_string
response = requests.get(response_url, cookies=cookies)
print(response.text)

# Utilize algum renderizador html pra facilitar a visualização e achar a flag
# https://htmledit.squarefree.com/
