# -*- coding: utf-8 -*-

from sympy import Lambda, simplify, diff, symbols, solve
from sympy.parsing.sympy_parser import parse_expr, convert_xor
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application


def newtwon(f, erro=10**-6, chute=None, intervalo=None, max=50, precisao=5):
    if type(f) == str:
        transformations = (standard_transformations + (implicit_multiplication_application, convert_xor))
        f = Lambda(x, parse_expr(f, transformations=transformations))
    fd = Lambda(x, simplify(diff(f(x), x)))

    if chute:
        x0 = chute
    else:
        if intervalo:
            x0 = (intervalo[0]+intervalo[1]) / 2
        else:
            x0 = (solve(fd(x), x)[0]).evalf(precisao)

    print(f(x))
    print(fd(x))
    print(x0)

    # if abs(f(chute)) < erro:
    #     return {
    #         'y': chute,
    #         'it': 0
    #     }
    x1 = None
    ea = None
    for i in range(1, max+1):
        f_x0 =  f(x0).evalf(precisao)
        fd_x0 = fd(x0).evalf(precisao)

        if fd_x0 == 0:
            print('Derivada de "{}" para "x = {}" resulta em zero. Não é possivel continuar operação.'.format(fd(x), x0))
            return

        x1 = (x0 - (f_x0 / fd_x0)).evalf(precisao)

        ea = abs(x1 - x0).evalf(precisao)
        if ea <= erro:
            return {
                'y': x1, #?
                'it': i,
                'ea': ea
            }

        x0 = x1

    return {
        'y': 'Limite de iterações atingido.',
        'it': max,
        'ea': ea
    }


x, a = symbols('x a')

#test = newtwon('2*x - sin(x) - 4', erro=10**-3, intervalo=[2,3])
test = newtwon('x^3 - 9*x + 5', erro=10**-2, intervalo=[0.5,1])
print(test)
exit(0)

transformations = (standard_transformations + (implicit_multiplication_application, convert_xor))
f = Lambda((x,a), parse_expr("a*x - x*log(x)", transformations=transformations))

precisao = 100

inicio = 2

ajustes = [-50, -1, 0, 0.69315218, 0.693147, 1, 1.9065, 2, 3, 4, 5]
ajustes = [0]

tol = 10**-10

for ajuste in ajustes:
    ftemp = Lambda(x, f(x, a).subs(a, ajuste))
    newtwon(ftemp, intervalo=[1,3])
    # print('#####################')
    # found = False
    # inicio = solve(fd(x, a).subs(a, 1), x)[0]
    # print('ajuste:       ', ajuste)
    # print('chute inicial:', inicio)
    #
    # if abs(f(inicio, ajuste)) < tol:
    #     print('d', inicio)
    #     print('k',0)
    #     continue
    #
    # x0 = inicio
    # for i in range(50):
    #     f_x0 =  f(x0, ajuste).evalf(precisao)
    #     fd_x0 = fd(x0, ajuste).evalf(precisao)
    #     if fd_x0 == 0:
    #         print('Divisão por zero.')
    #         break
    #
    #     x1 = (x0 - ( f_x0 / fd_x0 )).evalf(precisao)
    #
    #     f_x1 =  f(x1, ajuste).evalf(precisao)
    #
    #     if (abs(x1 - x0) <= tol):
    #       print('d', x1)
    #       print('k',i+1)
    #       found = True
    #       break
    #     x0 = x1
    #
    # if found:
    #     continue
    #
    # print('limite atingido sem resultado!')
    #
