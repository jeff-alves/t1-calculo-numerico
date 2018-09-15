# -*- coding: utf-8 -*-

from sympy import Lambda, symbols

from calc import newtwon, newtwon_mod, falsa_posicao
from util import str_to_func


x, a = symbols('x a')
f = str_to_func('ax - x log(x)', (x, a))
precisao = 100
inicio = 2
ajustes = [-50, -1, 0, 0.69315218, 0.693147, 1, 1.9065, 2, 3, 4, 5]
tol = 10**-10

for ajuste in ajustes:
    ftemp = Lambda(x, f(x, a).subs(a, ajuste))
    r = falsa_posicao(ftemp, intervalo=[1,3])
    print(r)
    r = newtwon(ftemp, intervalo=[1,3])
    print(r)
    r = newtwon_mod(ftemp, intervalo=[1,3])
    print(r)
    print('###################')