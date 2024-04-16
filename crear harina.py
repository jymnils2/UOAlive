# version 1.0
# requisitos : tener al menos 1 item del elemento "wheat sheaf" en la bolsa
#              archivo color.py para que los mensajes se vean a colores
#              Serial de una moledora de trigo "flour mill"    
#              la moledora debe estar alado de el personaje que la usara
#              ver "cosas que debes saber hacer"
# descripcion : usa todos los elementos trigo "wheath sheaf" en una moledora "flour mill"
#               el script informara de la cantidad de items bolsa de harina "sack of flour" que seran creados 
# configuracion este scrip necesita el serial de la moledora de trigo
#               debe estar configurado para ejecutarse con la tecla F1
# consejos      consiga muchos wheath sheaf de los campos de cultivo de britania, visite la libreria de UOAlive para ir directamente
#               al mismo tiempo tambien puede cosechar algodon para hacer rollos de tela y calabazas para cocinar
#               si el script esta asignado a una tecla como F1, esta tecla sirve para iniciarlo y detenerlo
##############################################################################

from colors import colors   # lindos colores para los mensajes
moledora = 0x406D587E       # este es el codigo de la maquina de moler grano
IDmontondetrigo = 0x1EBD    # este es el codigo del monton de trigo
contador = 0
cantidadtrigos = 0
cantidadbolsas = 0
trigosporbolsa = 2
montondetrigo = Items.FindByID(IDmontondetrigo, -1, Player.Backpack.Serial)  # buscando el item monton de trigo que tiene el ID 0x1EBD
if montondetrigo != None:
    cantidadtrigos = montondetrigo.Amount             # encontramos el item y averiguamos su cantidad de trigos
    cantidadbolsas = cantidadtrigos//trigosporbolsa   # calculamos cuantas bolsas podemos crear
    contador = cantidadbolsas*trigosporbolsa          # calculamos cuantos montones de trigo necesitamos usar
    Player.HeadMessage( colors[ 'green' ], 'encontrados '+str(cantidadtrigos)+' trigos')
    Player.HeadMessage( colors[ 'green' ], 'solo '+str(contador)+' seran usados')
    Player.HeadMessage( colors[ 'green' ], 'para crear '+str(cantidadbolsas)+' bolsas')
else:
    Player.HeadMessage( colors[ 'red' ], 'no se encontraron trigos '+str(cantidadbolsas))
    #break

#   si no tenemos trigos suficientes abortamos
if cantidadtrigos < trigosporbolsa:
    Player.HeadMessage( colors[ 'red' ], 'no hay trigos suficientes para hacer 1 bolsa')
    #break
    
#   ahora que tenemos todo listo recien molemos
molidos = 1
while molidos <= cantidadbolsas:
    Player.HeadMessage( colors[ 'yellow' ], 'cargando '+str(molidos))
    Items.UseItem(montondetrigo.Serial)             # usando el item que encontramos
    Target.WaitForTarget(10000, False)
    Target.TargetExecute(moledora)
    Misc.Pause(1000)                                # pausa para la cargar el trigo 1 segundos
    Items.UseItem(moledora)
    Player.HeadMessage( colors[ 'yellow' ], 'moliendo '+str(molidos))
    Misc.Pause(7000)                                # pausa para la animacion de molido 7 segundos
    molidos = molidos+1

#   todo termino existosamente
Player.HeadMessage( colors[ 'yellow' ], 'Terminado! se crearon '+str(cantidadbolsas)+' bolsas')
