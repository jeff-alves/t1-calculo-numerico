function [d, k, ea] = newton(f, fd, ajuste, tolerancia, inicio, max_it)

  tolerancia = vpa(tolerancia);
  ajuste = vpa(ajuste);
  inicio = vpa(inicio);

  k = 1;
  f_i = vpa(f(inicio, ajuste));
  if abs(f_i) < tolerancia
    d = inicio;
    ea = abs(f_i);
    return
  endif

  x0 = inicio;
  while (k <= max_it)

    f_x0 =  vpa(f (x0, ajuste));
    fd_x0 = vpa(fd(x0, ajuste));

    x1 = x0 - ( f_x0 / fd_x0 );
    
    f_x1 =  vpa(f (x1, ajuste));

    #if (abs(f_x1) < tolerancia) || (abs(x1 - x0) <= tolerancia)
    ea = abs(x1 - x0);
    if (ea <= tolerancia)
      d = simplify(x1);
      return
    endif

    x0 = x1;
    k+=1;
  endwhile
  k-=1;
  d = 'Limite de iterações atingido, sem resultados.';

endfunction