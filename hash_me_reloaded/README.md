# Hash me reloaded

> https://ringzer0ctf.com/challenges/14

O desafio consiste em, em menos de 2 segundos, pegar uma string de código binário, converter, hashear ela usando um algoritmo sha512, e enviar o resultado de volta.

![print](https://github.com/renanstd/ringzer0ctf-challenges/blob/main/hash_me_reloaded/images/challenge.png)

Resolvi utilizando as libs:
- **requests**: para pegar o html da página usando cookies de uma sessão logada
- **gazpacho**: para fazer o scrap deste html e coletar a string a ser codificada
- `chr(int(bin_value, 2))`, para converter um binário de 8 bits em seu respectivo caractere ASCII
