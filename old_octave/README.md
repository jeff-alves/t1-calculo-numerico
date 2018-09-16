# Cálculo Numérico - Trabalho 1

Desenvolva um sistema para calcular esse deslocamento x da extremidade de um foguete espacial.

## Equipe

- Antônio Victor Figueiredo Porto (líder)
- Iago Braga
- Jefferson Alves Costa
- Lucas da Silva Soares
- Renan Da Silveira Teles

## Como usar:

### Falsa Posição:

Rodar o arquivo com o nome do metodo escolhido, passando os parametros nescessários:

    - f = Função a ser usada f(x,a);
    - a = Lista contendo ajustes para a função (usar "a" para variavel de ajuste na função acima);
    - t = Tolerancia permitida de erro para considerar como raiz;
    - i = Intervalo para busca;
    - max = numero maximo de iterações;

**Exemplo:**

    octave run_falsa_posicao.m f='a*x - x*ln(x)' a='[-50, -1, 0, 0.69315218, 1, 1.9065, 2, 3, 4, 5]' t='10^-4' i='[2,3]' max='50'

### Newton Raphson:

Rodar o arquivo "run_newton.m", passando os parametros nescessários:

    - f = Função a ser usada f(x,a);
    - a = Lista contendo ajustes para a função (usar "a" para variavel de ajuste na função acima);
    - t = Tolerancia permitida de erro para considerar como raiz;
    - i = Chute inicial;
    - max = numero maximo de iterações;

**Exemplo:**

    octave run_newton.m f='a*x - x*ln(x)' a='[-50, -1, 0, 0.69315218, 1, 1.9065, 2, 3, 4, 5]' t='10^-4' i='2' max='50'

### Newton Raphson modificado:

Rodar o arquivo "run_newton2.m", passando os parametros nescessários:

    - f = Função a ser usada f(x,a);
    - a = Lista contendo ajustes para a função (usar "a" para variavel de ajuste na função acima);
    - t = Tolerancia permitida de erro para considerar como raiz;
    - i = Chute inicial;
    - max = numero maximo de iterações;

**Exemplo:**

    octave run_newton2.m f='a*x - x*ln(x)' a='[-50, -1, 0, 0.69315218, 1, 1.9065, 2, 3, 4, 5]' t='10^-4' i='2' max='50'