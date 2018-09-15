# -*- coding: utf-8 -*-

from sympy import Lambda, diff, symbols, solve, sign

from util import str_to_func

MAX = 50
PREC = 5


def falsa_posicao(f, erro=10**-6, intervalo=None, max=MAX, precisao=PREC):
    x = symbols('x')
    if type(f) == str:
        f = str_to_func(f, x)

    a = intervalo[0]
    b = intervalo[1]

    ea = abs(f(a)).evalf(precisao)
    if ea <= erro:
        return {
            'y': a,
            'it': 1,
            'ea': ea
        }

    ea = abs(f(b)).evalf(precisao)
    if ea <= erro:
        return {
            'y': b,
            'it': 1,
            'ea': ea
        }

    for i in range(1, max+1):
        ea = abs(b - a)
        if ea <= erro:
            return {
                'y': [a, b],
                'it': i,
                'ea': ea
            }

        f_a = f(a).evalf(precisao)
        f_b = f(b).evalf(precisao)
        x = ((a * f_b - b * f_a) / (f_b - f_a)).evalf(precisao)
        f_x = f(x).evalf(precisao)

        ea = abs(f_x)
        if ea <= erro:
            return {
                'y': x,
                'it': i,
                'ea': ea
            }

        if not f_x.is_comparable:
            return {
                'y': 'Não é possivel obter o sinal de um número imaginário em f(x).',
                'it': i,
                'ea': ea
            }
        if sign(f_x) > 0:
            a = x
        else:
            b = x


    return {
        'y': 'Limite de iterações atingido.',
        'it': max,
        'ea': ea
    }


def newtwon(f, erro=10**-6, chute=None, intervalo=None, max=MAX, precisao=PREC):
    x = symbols('x')
    if type(f) == str:
        f = str_to_func(f, x)
    fd = Lambda(x, diff(f(x), x))
    ea = None

    if chute:
        x0 = chute
    else:
        if intervalo:
            x0 = (intervalo[0]+intervalo[1]) / 2
        else:
            x0 = (solve(fd(x), x)[0]).evalf(precisao)
            if abs(x0) <= erro: x0 = 1


    for i in range(1, max+1):
        f_x0 =  f(x0).evalf(precisao)
        if abs(f_x0) <= erro:
            return {
                'y': x0,
                'it': i,
                'ea': ea
            }

        fd_x0 = fd(x0).evalf(precisao)
        if fd_x0 == 0:
            return {
                'y': 'Derivada de "{}" para "x = {}" resulta em zero. Não é possivel continuar operação.'.format(fd(x), x0),
                'it': i,
                'ea': ea
            }

        x1 = (x0 - (f_x0 / fd_x0)).evalf(precisao)

        ea = abs(x1 - x0).evalf(precisao)
        if ea <= erro:
            return {
                'y': x1,
                'it': i,
                'ea': ea
            }

        x0 = x1

    return {
        'y': 'Limite de iterações atingido.',
        'it': max,
        'ea': ea
    }


def newtwon_mod(f, erro=10**-6, chute=None, intervalo=None, max=MAX, precisao=PREC):
    x = symbols('x')
    if type(f) == str:
        f = str_to_func(f, x)
    fd = Lambda(x, diff(f(x), x))
    ea = None

    if chute:
        x0 = chute
    else:
        if intervalo:
            x0 = (intervalo[0]+intervalo[1]) / 2
        else:
            x0 = (solve(fd(x), x)[0]).evalf(precisao)
            if abs(x0) <= erro: x0 = 1

    fd_x0 = fd(x0).evalf(precisao)
    if fd_x0 == 0:
        return {
            'y': 'Derivada de "{}" para "x = {}" resulta em zero. Não é possivel continuar operação.'.format(fd(x), x0),
            'it': 1,
            'ea': ea
        }

    for i in range(1, max+1):
        f_x0 =  f(x0).evalf(precisao)
        if abs(f_x0) <= erro:
            return {
                'y': x0,
                'it': i,
                'ea': ea
            }

        x1 = (x0 - (f_x0 / fd_x0)).evalf(precisao)

        ea = abs(x1 - x0).evalf(precisao)
        if ea <= erro:
            return {
                'y': x1,
                'it': i,
                'ea': ea
            }

        x0 = x1

    return {
        'y': 'Limite de iterações atingido.',
        'it': max,
        'ea': ea
    }