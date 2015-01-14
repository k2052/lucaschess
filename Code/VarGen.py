import sys
import os

isLinux = sys.platform == "linux2"
if isLinux:
    isWine = os.path.isfile("/usr/bin/wine")
    startfile = os.system
else:
    startfile = os.startfile
isWindows = not isLinux

dgt = None
dgtDispatch = None

configuracion = None  # Actualizado en Configuracion tras lee()

todasPiezas = None

tbook = "Openings/GM_1990-2012.bin"
tbookPTZ = "Openings/fics15.bin"

xtutor = None

