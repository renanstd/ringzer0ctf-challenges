import requests
import hashlib
from gazpacho import Soup


# Acessar a página usando cookies de uma página já logada
url = "https://ringzer0ctf.com/challenges/14"
cookies = {"PHPSESSID": "61qotuplj1u6innn61ffhoqdt6"}
html = requests.get(url, cookies=cookies).text
soup = Soup(html)

# Fazer um scrapzinho basico pra pegar o texto que precisa ser hasheado
div = soup.find('div', {'class': 'challenge-wrapper'})
message = div.find('div', {'class': 'message'})
stripped_message = message.strip()

# Remover os marcadores de "begin message" e "end message"
bin_numbers = stripped_message.replace("----- BEGIN MESSAGE -----", "")
bin_numbers = bin_numbers.replace(" ----- END MESSAGE -----", "")
bin_numbers = bin_numbers.strip()

# Dividir em grupos de 8 bits
bin_groups = ','.join([bin_numbers[i:i+8] for i in range(0, len(bin_numbers), 8)])
bin_letters = bin_groups.split(',')

# Decodificar a mensagem
to_hash = ""
for bin_letter in bin_letters:
    converted_letter = chr(int(bin_letter, 2))
    to_hash += converted_letter

# Hashear a mensagem
hashed_string = hashlib.sha512(to_hash.encode())
hashed_string = hashed_string.hexdigest()

# Enviar de volta e printar o html resultante
response_url = url + "/" + hashed_string
response = requests.get(response_url, cookies=cookies)
print(response.text)

# Utilize algum renderizador html pra facilitar a visualização e achar a flag
# https://htmledit.squarefree.com/
