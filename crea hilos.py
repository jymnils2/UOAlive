# version 1.0
# requisitos : tener al menos 1 item del elemento "Bale of Cotton" en la bolsa
#              archivo color.py para que los mensajes se vean a colores
#              Serial de una hiladora de algodon "Spining Wheel"    
#              la hiladora debe estar alado de el personaje que la usara
#              ver "cosas que debes saber hacer"
# descripcion : usa todos los elementos algodon "Bale of Cotton" en una hiladora "Spining Wheel"
#               el script informara de la cantidad de items rollo de tela " Bolt of Cloth" que seran creados 
# configuracion este scrip necesita el serial de la hiladora
#               debe estar configurado para ejecutarse con la tecla F1
# consejos      consiga mucho algodon lana "Bale of Cotton" de los campos de cultivo de britania
#               visite la libreria de UOAlive para ir directamente
#               al mismo tiempo tambien puede cosechar trigo para hacer harina y calabazas para cocinar
#               si el script esta asignado a una tecla como F1, esta tecla sirve para iniciarlo y detenerlo
##############################################################################

from colors import colors   # lindos colores para los mensajes
hiladora = 0x403B9669       # este es el codigo de la maquina hiladora de la ciudad inicial, cambiar por el de su casa
IDboladealgodon = 0x0DF9    # este es el codigo de la bola de algodon
contador = 0
cantidadhilos = 0
cantidadbolas = 0
hilosporbola = 1
boladealgodon = Items.FindByID(IDboladealgodon, -1, Player.Backpack.Serial)  # buscando el item "Bale of Cotton" que tiene el ID 0x0DF9
if boladealgodon != None:
    cantidadhilos = boladealgodon.Amount          # encontramos el item y averiguamos su cantidad
    cantidadbolas = cantidadhilos//hilosporbola   # calculamos cuantos rollos podemos crear
    contador = cantidadbolas*hilosporbola         # calculamos cuantas bolas de hilo necesitamos usar
    Player.HeadMessage( colors[ 'green' ], 'encontrados '+str(cantidadhilos)+' algodones')
    Player.HeadMessage( colors[ 'green' ], 'solo '+str(contador)+' seran usados')
    Player.HeadMessage( colors[ 'green' ], 'para crear '+str(cantidadbolas*6)+' hilos de algodon')
else:
    Player.HeadMessage( colors[ 'red' ], 'no se encontro algodon '+str(cantidadbolas))
    #break

#   si no tenemos hilos suficientes abortamos
if cantidadhilos < hilosporbola:
    Player.HeadMessage( colors[ 'red' ], 'no hay algodon suficientes para hacer 1 hilo')
    #break
    
#   ahora que tenemos todo listo recien hilamos
hilados = 1
while hilados <= contador:
    Player.HeadMessage( colors[ 'yellow' ], 'hilando '+str(hilados))
    Items.UseItem(boladealgodon.Serial)           # usando el item que encontramos
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(hiladora)
    Misc.Pause(7000)                           # pausa para la animacion de 1 segundo
    hilados = hilados+1

#   todo termino existosamente
Player.HeadMessage( colors[ 'yellow' ], 'Terminado! se crearon '+str(cantidadbolas*6)+' hilos de algodon')
