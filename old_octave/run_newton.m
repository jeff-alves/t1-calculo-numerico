addpath ("main_func")
pkg load symbolic

param = parse_args(argv, nargin); #converte os parametros em variaveis nomeadas

syms x a
f(x,a) = cell2sym({param.f})
fd = diff(f)

tolerancia = param.t;
inicio = param.i;
max_it = param.max;

for ajuste = param.a
    printf("#############################\n");
    [d, k, ea] = newton(f, fd, ajuste, tolerancia, inicio, max_it);
    printf("Ajuste:    %f\n",ajuste);
    printf("Distancia: %s\n",char(d));
    printf("EA:        %s\n",char(ea));
    printf("Iterações: %i\n",k);
endfor
printf("#############################\n");
