
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html


# Printar o Sistema Operacional que voce esta usando:
# YOUR CODE HERE
sistema_operacional = sys.platform
print(sistema_operacional)

# Printar a versão de Python que voce esta usando:
# YOUR CODE HERE
versao_python = sys.version

print(versao_python)


import os
# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Printar a process Id atual
# YOUR CODE HERE
id = os.getpid()
print(id)

# Printar o atual diretório:
# YOUR CODE HERE
diretorio = os.getcwd()

print(diretorio)

# Printar o nome da maquina
# YOUR CODE HERE
print(os.uname().nodename)