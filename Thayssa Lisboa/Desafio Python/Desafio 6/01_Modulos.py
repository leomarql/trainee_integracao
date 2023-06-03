import sys
import platform
import os
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html
# Printar o Sistema Operacional que voce esta usando:
print('sistema operacional:', sys.platform)

# Printar a versão de Python que voce esta usando:
print('python version:', platform.python_version())
print('python version extend:', sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html
# Printar a process Id atual
print('process ID:', os.getpid())

# Printar o atual diretório:
print('current directory:', os.getcwd())

# Printar o nome da maquina
print('hostname:', platform.node()) 