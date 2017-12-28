from subprocess import check_call

check_call(['dot', '-Tpng', 'arbol1.dot', '-o', 'arbolsalida.png'])
