# Tutorial para registrarse en earthdata para descargar imagenes desde python 
from netrc import netrc
from subprocess import Popen
from getpass import getpass
import os

urs = 'urs.earthdata.nasa.gov'    # Sitio para autentificar
prompts = ['Temaukel','Colocar clave'] #Nombre y contraseña de nuestra cuenta 

# Determina si el archivo netrc existe https://git.earthdata.nasa.gov/projects/LPDUR/repos/daac_data_download_python/browse desde aca se descarga la carpeta donde 
#esta el archivo netrc
try:
    netrcDir = os.path.expanduser("C:/Users/Monta/Downloads/daac_data_download_python-main@9679208f496/.netrc") #Se usa la dirección de la carpeta descargada en el link anterior 
    netrc(netrcDir).authenticators(urs)[0]

# Sino se crea se usa este codigo donde se crea esa el archivo netrc 
except FileNotFoundError:
    homeDir = os.path.expanduser("~")
    Popen('touch {0}.netrc | chmod og-rw {0}.netrc | echo machine {1} >> {0}.netrc'.format(homeDir + os.sep, urs), shell=True)
    Popen('echo login {} >> {}.netrc'.format(getpass(prompt=prompts[0]), homeDir + os.sep), shell=True)
    Popen('echo password {} >> {}.netrc'.format(getpass(prompt=prompts[1]), homeDir + os.sep), shell=True)

# Edita el archivo netrc con el nombre y contraseña 
except TypeError:
    homeDir = os.path.expanduser("~")
    Popen('echo machine {1} >> {0}.netrc'.format(homeDir + os.sep, urs), shell=True)
    Popen('echo login {} >> {}.netrc'.format(getpass(prompt=prompts[0]), homeDir + os.sep), shell=True)
