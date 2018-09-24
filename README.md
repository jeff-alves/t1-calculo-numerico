# Cálculo Numérico - Trabalho 1

Desenvolva um sistema para calcular esse deslocamento x da extremidade de um foguete espacial.

## Equipe

- Antônio Victor Figueiredo Porto (líder)
- Iago Braga
- Jefferson Alves Costa
- Lucas da Silva Soares
- Renan Da Silveira Teles

## Como usar:

**Requer biblioteca Sympy:**

    sudo pip install sympy

**Rodar o arquivo main com a opção -h para ver a ajuda:**

    python main.py -h
    usage: main.py [-h] -f  -a  -i  [-c] [-e] [-p] [-m]

    Trabalho de Cálculo Numérico

    optional arguments:
      -h, --help         show this help message and exit
      -f , --funcao      Função  f(x,a) a ser usada. EX: "ax - x ln(x)"
      -a , --ajustes     Lista com os ajustes "a" para a função. EX: "[1, 2, 3, 4]"
      -i , --intervalo   Intervalo que contem a raizes. EX: "[1, 3]"
      -c , --chute       Chute inicial para x0. Usado apenas para o metodo de Newton.
      -e , --erro        Erro máximo permitido. Default: 10^-4. EX: "10^-6"
      -p , --precisao    Precisão a ser usada nos calculos. Default: 6
      -m , --max         Limite de iterações permitidas para cada metodo. Default: 50


**Exemplo de uso:**

    python main.py -f 'ax - x ln(x)' -a '[-50, -1, 0, 0.6931471805, 1, 1.9065, 2, 3]' -i '[0.01,25]' -e '10^-10' -p 12