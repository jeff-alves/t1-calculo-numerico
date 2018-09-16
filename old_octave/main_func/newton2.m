function [d, k, ea] = newton2(f, fd, ajuste, tolerancia, inicio, max_it)

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

  fd_i = vpa(fd(inicio, ajuste));
  old = inicio;
  while (k <= max_it)

    f_x0 =  vpa(f (old, ajuste));
    #fd_x0 = vpa(fd(old, ajuste));

    x1 = old - ( f_x0 / fd_i );
    
    f_x1 =  vpa(f (x1, ajuste));

    #if (abs(f_x1) < tolerancia) || (abs(x1 - old) <= tolerancia)
    ea = abs(x1 - old);
    if (ea <= tolerancia)
      d = simplify(x1);
      return
    endif

    old = x1;
    k+=1;
  endwhile
  k-=1;
  d = 'Limite de iterações atingido, sem resultados.';

endfunction