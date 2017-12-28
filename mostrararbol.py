from subprocess import check_call

check_call(['dot', '-Tpng', 'arbol.dot', '-o', 'arbolsalida.png'])
