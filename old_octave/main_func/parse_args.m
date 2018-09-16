function params = parse_args (args, nargs)

  for i = 1:nargs
    a = strsplit(args{i}, '=');
    params.(a{1}) = eval(a{2}, 'a{2}');
  endfor

endfunction