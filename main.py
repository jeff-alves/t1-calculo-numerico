# -*- coding: utf-8 -*-
from argparse import ArgumentParser, RawTextHelpFormatter

from sympy import Lambda, symbols

from calc import newtwon, newtwon_mod, falsa_posicao
from util import str_to_func, str_to_eq


if __name__ == '__main__':
    parser = ArgumentParser(description="Trabalho de Cálculo Numérico", epilog="Exemplo de uso: python -m main -f 'ax - x ln(x)' -a '[-50, -1, 0, 0.69315218, 0.693147, 1, 1.9065, 2, 3, 4, 5]' -i '[1,3]'", formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--funcao', metavar='', required=True, type=str, help='Função  f(x,a) a ser usada. EX: "ax - x ln(x)"')
    parser.add_argument('-a', '--ajustes', metavar='', required=True, type=str, help='Lista com os ajustes "a" para a função. EX: "[1, 2, 3, 4]"')
    parser.add_argument('-i', '--intervalo', metavar='', required=True, default='None', type=str, help='Intervalo que contem a raizes. EX: "[1, 3]"')
    parser.add_argument('-c', '--chute', metavar='', default=None, type=float, help='Chute inicial para x0. Usado apenas para o metodo de Newton.')
    parser.add_argument('-e', '--erro', metavar='', default='10^-4', type=str, help='Erro máximo permitido. EX: "10^-4"')
    parser.add_argument('-p', '--precisao', metavar='', default=6, type=int, help='Precisão a ser usada nos calculos.')
    parser.add_argument('-m', '--max', metavar='', default=50, type=int, help='Limite de iterações permitidas para cada metodo.')

    args = parser.parse_args()

    try:
        x, a = symbols('x a')
        f = str_to_func(args.funcao, (x, a))
        precisao = args.precisao
        chute = args.chute
        ajustes = eval(args.ajustes)
        erro = str_to_eq(args.erro)
        max = args.max
        intervalo = eval(args.intervalo)

        for ajuste in ajustes:
            ftemp = Lambda(x, f(x, a).subs(a, ajuste))
            print('\n' + ('#' * 80) + '\n')
            print('Para a = {}, a função será: {}\n'.format(ajuste, ftemp(x)))

            try:
                print('\tFalsa Posição:')
                r = falsa_posicao(ftemp, erro=erro, intervalo=intervalo, max=max, precisao=precisao)
                for key, value in sorted(r.items()):
                    print('\t\t{}\t=\t{}'.format(key, value))
            except Exception as exc:
                print(exc)
            try:
                print('\tNewton:')
                r = newtwon(ftemp, erro=erro, chute=chute, intervalo=intervalo, max=max, precisao=precisao)
                for key, value in sorted(r.items()):
                    print('\t\t{}\t=\t{}'.format(key, value))
            except Exception as exc:
                print(exc)
            try:
                print('\tNewton MOD:')
                r = newtwon_mod(ftemp, erro=erro, chute=chute, intervalo=intervalo, max=max, precisao=precisao)
                for key, value in sorted(r.items()):
                    print('\t\t{}\t=\t{}'.format(key, value))
            except Exception as exc:
                print(exc)

        print('\n' + ('#' * 80) + '\n')

    except KeyboardInterrupt:
        print('Ctrl+C')
        exit(1)
