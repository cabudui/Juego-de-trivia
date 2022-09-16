#Librerias que usaremos
import time
import random
#colores
BLACK = '\033[30m'
RED = '\033[31m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
BLUE = '\033[34m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
#variables estilo
RESET_ALL = '\033[0m'
BRIGHT = '\033[1m'
DIM = '\033[2m'
NORMAL = '\033[22m'
#bienvenida
print(DIM+'Hola¡ Bienvenido a la trivia')
print('Espero te entretenga')
time.sleep(2)
#Pedimos informacion del usuario
nombre = input(BRIGHT+'\nIngresa tu nombre: '+RESET_ALL)

print(DIM+'\nHola',nombre, 'responde  escribiendo la letra de la alternativa y presiona "Enter" para enviar tu respuesta \n')
time.sleep(2)
#contador de oportunidad
oportunidades = 2
print('Tienes', oportunidades,'oportunidad de responder correctamente a cada pregunta.Por favor, pon tu respuesta:\n'+RESET_ALL)
time.sleep(2)

score = 0
#Creamos una variable de puntaje 
puntaje = random.randint(0, 8)

#pregunta
pregunta_1 = print(YELLOW+'1) ¿Como se llama el actor principal de  American Psycho?'+RESET)
print(DIM+'a) Jared leto.'
)
print('b) Crhistian Bale.'+RESET_ALL)

respuesta_1 = 'b'
#while
while respuesta_1 not in ('a', 'b', 'c', 'd'):
  respuesta_1 = input ('Debes responder a, b, c o d. Ingresa nuevamente tu respuesta porfavor: ')
  #for
for i in range(oportunidades):
    respuesta = input(BRIGHT+CYAN+'Añade tu respuesta, por favor: '+RESET_ALL)
    if (respuesta.lower() == respuesta_1):
        print(YELLOW+'Correcto¡¡.\n'+RESET)
        score = score + 1
        puntaje = puntaje + 5
      
        break
    else:
        print(RED+'Incorrecto u-u\n')
        puntaje = puntaje - 5
        time.sleep(1)
        print('La respuesta era', respuesta_1, '\n\n'+RESET)

time.sleep(2)
#pregunta
pregunta_2 = print(YELLOW+'2) ¿Cual es el verdadero nombre del abogado Saul Goodman en la serie Better Call saul?'+RESET)
print(DIM+'a) Kim Wexler')
print('b) Heisengber')
print('c) Aaron paul')
print('d) Jimmy Mc Gill'+RESET_ALL)

respuesta_2 = 'd'
#for
for i in range(oportunidades):
    respuesta = input(BRIGHT+CYAN+'Pon tu respuesta: '+RESET_ALL)
    if (respuesta.lower() == respuesta_2):
        print(YELLOW+'Correcto!!\n'+RESET)
        score = score + 1
        puntaje = puntaje + 5
        break
    else:
        print(RED+'Incorrecto!u-u\n')
        puntaje = puntaje - 5
        time.sleep(0.5)
        print('La respuesta correcta era', respuesta_2,'Es Jimmy Mc Gill''\n\n'+RESET)

time.sleep(2)

#pregunta
pregunta_3 = print(YELLOW+'3) ¿Cómo se llama el amigo de Bojack Horseman que vivia en su casa en la serie Bojack horseman'+RESET)
print(DIM+'a) Sara ')
print('b) Todd')
print('c) James')
print('d) Lester'+RESET_ALL)

respuesta_3 = 'b'

#for 
for i in range(oportunidades):
    respuesta = input(BRIGHT+CYAN+'Añade tu respuesta: '+RESET_ALL)
    if (respuesta.lower() == respuesta_3):
        print(YELLOW+'Correcto!!\n'+RESET)
        score = score + 1
        puntaje = puntaje + 5
        break
    else:
        print(RED+'Incorrecto!u-u\n')
        puntaje = puntaje - 5
        time.sleep(0.5)
        print('La respuesta correcta es', respuesta_3,'Todd.''\n\n'+RESET)

time.sleep(2)
#final
print(CYAN+'¡Gracias por jugar mi trivia¡'+RESET_ALL)