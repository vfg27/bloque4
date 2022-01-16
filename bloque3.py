#Marta Morán, Miguel Varas y Victor Fresno
import sys
import os
import json
import time
from subprocess import call
os.chdir("/root/bloque3.2/bookinfo/src/reviewsV1")
call(["pwd"])
#Ejecutamos el comando indicado
call(["docker run --rm -u root -v "+r'"'+"$(pwd)"+r'"'+":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"], shell=True)
os.chdir("/root/bloque3.2/bookinfo/src/reviewsV2")
call(["pwd"])
#Ejecutamos el comando indicado
call(["docker run --rm -u root -v "+r'"'+"$(pwd)"+r'"'+":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"], shell=True)
os.chdir("/root/bloque3.2/bookinfo/src/reviewsV3")
call(["pwd"])
#Ejecutamos el comando indicado
call(["docker run --rm -u root -v "+r'"'+"$(pwd)"+r'"'+":/home/gradle/project -w /home/gradle/project gradle:4.8.1 gradle clean build"], shell=True)
os.chdir("/root")
call(["pwd"])
os.chdir("/root/bloque3.2")
call(["pwd"])
#Arrancamos los contenedores
call(["docker-compose up"], shell=True)
