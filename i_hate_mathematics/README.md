# Hash me reloaded

> https://ringzer0ctf.com/challenges/32

O desafio consiste em, em menos de 2 segundos, pegar uma string com uma equação, onde existem valores decimais, hexadecimais, e binarios, resolver a equação, e enviar o resultado de volta.

![print](https://github.com/renanstd/ringzer0ctf-challenges/blob/main/i_hate_mathematics/images/challenge.png)

Resolvi utilizando as libs:
- **requests**: para pegar o html da página usando cookies de uma sessão logada
- **gazpacho**: para fazer o scrap deste html e coletar a string a ser codificada
- `int(value, 16)` para converter um numero hexadecimal para decimal
- `int(value, 2)` para converter um numero binário para decimal
