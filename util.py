# -*- coding: utf-8 -*-

from sympy import Lambda, symbols
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor


def str_to_func(func, vars):
    transformations = (standard_transformations + (implicit_multiplication_application, convert_xor))
    if type(vars) == str:
        vars = symbols(vars)
    return Lambda(vars, parse_expr(func, transformations=transformations))

def str_to_eq(func):
    transformations = (standard_transformations + (implicit_multiplication_application, convert_xor))
    return parse_expr(func, transformations=transformations)
