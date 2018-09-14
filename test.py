# -*- coding: utf-8 -*-


from sympy import *
from sympy.parsing.sympy_parser import parse_expr

x, a, y = symbols('x a y')


f = Lambda((x,a), parse_expr("a*x - x*log(x)"))
fd = Lambda((x,a), diff(f(x,a), x))
precisao = 50

print(f(x,a))
print(fd(x,a))


inicio = 2

ajustes = [-50, -1, 0, 0.69315218, 1, 1.9065, 2, 3, 4, 5]

tol = 10**-4

for ajuste in ajustes:
    print('#####################')
    found = False
    inicio = solve(fd(x, a).subs(a, 1), x)[0]
    print('ajuste:       ', ajuste)
    print('chute inicial:', inicio)

    if abs(f(inicio, ajuste)) < tol:
        print('d', inicio)
        print('k',0)
        continue
    
    x0 = inicio
    for i in range(50):
        f_x0 =  f(x0, ajuste).evalf(precisao)
        fd_x0 = fd(x0, ajuste).evalf(precisao)
        if fd_x0 == 0:
            print('Divisão por zero.')
            break
    
        x1 = (x0 - ( f_x0 / fd_x0 )).evalf(precisao)
        
        f_x1 =  f(x1, ajuste).evalf(precisao)

        if (abs(x1 - x0) <= tol):
          print('d', x1)
          print('k',i+1)
          found = True
          break
        x0 = x1
    
    if found:
        continue
    
    print('limite atingido sem resultado!')
    
