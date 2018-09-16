function [d, k, ea] = falsa_posicao(f, ajuste, tolerancia, intervalo, max_it)
  
  tolerancia = abs(sym(tolerancia, 'f'));
  ajuste = sym(ajuste, 'f');
  a = sym(intervalo(1), 'f');
  b = sym(intervalo(2), 'f');
  k = 1;
  ea = sym(0,'f');

  if abs(b-a) <= tolerancia
    d = [a, b];
    ea = abs(b-a);
    return
  elseif abs(f(a, ajuste)) < tolerancia
    d = [a];
    ea = abs(f(a, ajuste))
    return
  elseif abs(f(b, ajuste)) < tolerancia
    d = [b];
    ea = abs(f(b, ajuste))
    return
  endif

  while (k <= max_it)
    f_a = vpa(f(a, ajuste));
    f_b = vpa(f(b, ajuste));
    x = vpa((a*f_b - b*f_a) / (f_b-f_a));
    f_x = vpa(f(x, ajuste));


    if abs(f_x) < tolerancia
      d = [x];
      ea = abs(f_x)
      return
    endif

    if imag(f_x)
      d = 'Não é possivel obter o sinal de um número imaginário em f(x).';
      return
    endif
    #if sign(f_a * f_x) > 0
    if sign(f_x) > 0
      a = x;
    else
      b = x;
    endif

    if abs(b-a) <= tolerancia
      d = [a, b];
      ea = abs(b-a)
      return
    endif
    
    k+=1;
  endwhile
  k-=1;
  d = 'Limite de iterações atingido, sem resultados.';

endfunction