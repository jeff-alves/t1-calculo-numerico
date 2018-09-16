addpath ("main_func")
pkg load symbolic

param = parse_args(argv, nargin); #converte os parametros em variaveis nomeadas

syms x a
f(x,a) = cell2sym({param.f})
tolerancia = param.t;
intervalo = param.i;
max_it = param.max;

for ajuste = param.a
    printf("#############################\n");
    ajuste
    [d, k, ea] = falsa_posicao(f, ajuste, tolerancia, intervalo, max_it)
endfor
printf("#############################\n");
