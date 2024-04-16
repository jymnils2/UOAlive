# version 1.0
# requisitos : tener al menos 1 item del elemento "Balls of Yarn" en la bolsa
#              archivo color.py para que los mensajes se vean a colores
#              Serial de una tejedora de tela "loom"    
#              la tejedora debe estar alado de el personaje que la usara
#              ver "cosas que debes saber hacer"
# descripcion : usa todos los elementos bola de hilo "Balls of Yarn" en una tejedora "loom"
#               el script informara de la cantidad de items rollo de tela " Bolt of Cloth" que seran creados 
# configuracion este scrip necesita el serial de la tejedora
#               debe estar configurado para ejecutarse con la tecla F1
# consejos      consiga muchos "Balls of Yarn" despues de ejecutar el script de "crear bolas de lana"
#               se consigue mucha lana de los campos de cultivo de britania, visite la libreria de UOAlive para ir directamente
#               al mismo tiempo tambien puede cosechar trigo para hacer harina y calabazas para cocinar
#               si el script esta asignado a una tecla como F1, esta tecla sirve para iniciarlo y detenerlo
##############################################################################

from colors import colors   # lindos colores para los mensajes
tejedora = 0x403C303C       # este es el codigo de la maquina de tejer de la ciudad inicial, cambiar por el de su casa
IDboladehilos = 0x0FA0      # este es el codigo de la bola de hilos
contador = 0
cantidadhilos = 0
cantidadrollos = 0
hilosporrollo = 5
boladelana = Items.FindByID(IDboladehilos, -1, Player.Backpack.Serial)  # buscando el item spool of thread que tiene el ID 0x0FA0
if boladelana != None:
    cantidadhilos = boladelana.Amount               # encontramos el item y averiguamos su cantidad hilos
    cantidadrollos = cantidadhilos//hilosporrollo   # calculamos cuantos rollos podemos crear
    contador = cantidadrollos*hilosporrollo         # calculamos cuantas bolas de hilo necesitamos usar
    Player.HeadMessage( colors[ 'green' ], 'encontrados '+str(cantidadhilos)+' hilos')
    Player.HeadMessage( colors[ 'green' ], 'solo '+str(contador)+' seran usados')
    Player.HeadMessage( colors[ 'green' ], 'para crear '+str(cantidadrollos)+' rollos')
else:
    Player.HeadMessage( colors[ 'red' ], 'no se encontraron bolas de lana '+str(cantidadrollos))
    #break

#   si no tenemos hilos suficientes abortamos
if cantidadhilos < hilosporrollo:
    Player.HeadMessage( colors[ 'red' ], 'no hay hilos suficientes para hacer 1 rollo')
    #break
    
#   ahora que tenemos todo listo recien hilamos
hilados = 1
while hilados <= contador:
    Player.HeadMessage( colors[ 'yellow' ], 'hilando '+str(hilados))
    Items.UseItem(boladelana.Serial)           # usando el item que encontramos
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(tejedora)
    Misc.Pause(1000)                           # pausa para la animacion de 1 segundo
    hilados = hilados+1

#   todo termino existosamente
Player.HeadMessage( colors[ 'yellow' ], 'Terminado! se crearon '+str(cantidadrollos)+' rollos')
