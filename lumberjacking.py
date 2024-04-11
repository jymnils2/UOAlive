# version 1.0
# requisitos : tener al menos 1 del elemento "axe" en la bolsa, puede ser de una dos manos
#              archivo color.py para que los mensajes se vean a colores
#              Serial de un Escarabajo
#              el escarabajo debe estar en modo seguir 
#              ver "cosas que debes saber hacer"
# descripcion : te pide que escojas un elemento hacha de tu bolsa
#               usa el axe que escojiste (se equipa con el) para talar un recurso de madera cercano (alado de tu personaje)
#               en caso de estar pesado transforma los troncos en tablas
#               en caso de que todavia estemos muy pesados mueve las tablas un escarabajo (cuca)
#               cuyo serial debe estar definido dentro del script
# configuracion este scrip necesita el serial de escarabajo
#               debe estar configurado para ejecutarse con la tecla F1
# consejos      configurar el cliente para que no muestre el follaje y veas mejor los troncos
#               ver "cosas que debes saber hacer"
#               siempre tener armas disponibles para defenderse de NPCs agresivos
#               usar joyeria y ropa que suba la fuerza (STR) para tener mas capacidad de carga
#               se puede talar practicamente en todos lados, asi que escoge un lugar tranquilo
#               si el script esta asignado a una tecla como F1, esta tecla sirve para iniciarlo y detenerlo
##############################################################################

from colors import colors
# variables que se usaran

WOOD_LOGS = 0x1BDD          #ID de las tablas
                            # este serial del hacha ya no es necesaria porque le pedimos al usuario
AXE_SERIAL = 0x4084B539     # serial de el hacha que tenemos, podriamos mejorar pidiendo el hacha al principio
escarabajo = 0x0011B6BC     # serial del escarabajo
woodID = 0x1BD7             # ID de la madera en tablas    la diferencia entre serial y id es que el
                            # serial es unico por items pero el ID es igual para items con el
                            # mismo grafico pero diferente color
prev_wood = 0  
max_tries = 10

# creando los pesos para hacer maderas y pasar al escarabajo
max_weight = Player.MaxWeight
start_chopping_logs_weight = max_weight - 30
stop_chopping_trees_weight = max_weight - 2
# pidiendo que el usuario nos muestre el hacha a usar
axe_serial = Target.PromptTarget( 'Que hacha usaremos?' )
# autoequiparse el hacha si no esta equipada
axe_serial = Player.GetItemOnLayer('LeftHand')
if not axe_serial:
    Misc.SendMessage('No tenemos el hacha equipada!')
    # axe_serial = AXE_SERIAL #esto ya no es necesario
    Player.EquipItem(axe_serial)
    Misc.Pause(600)
# tala arboles hasta estar pesados para cortar o traspasar a escarabajo
Player.HeadMessage( colors[ 'green' ], 'empezando a cortar troncos')
while True:
    Journal.Clear()
    Target.TargetResource(axe_serial,"wood")
    Misc.Pause(1000)
    # si estamos pesados creamos tablas de los troncos.
    if Player.Weight >= start_chopping_logs_weight:
        Misc.SendMessage("Heavy, chop logs....")
        log = Items.FindByID(WOOD_LOGS, -1, Player.Backpack.Serial) 
        # convertimos TODOS los troncos a tablas
        while log != None:
            Player.HeadMessage( colors[ 'cyan' ], 'haciendo tablas')
            Items.UseItem(axe_serial)
            Target.WaitForTarget(5000, False)
            Target.TargetExecute(log)
            Misc.Pause(1000)
            log = Items.FindByID(WOOD_LOGS, -1, Player.Backpack.Serial)
    # Stop chopping trees when we cant carry more.
    if Player.Weight >= stop_chopping_trees_weight:
        Misc.SendMessage("Too heavy....  Stop")
        # aca hay que transferir a el escarabajo
        wood = Items.FindByID(woodID, -1, Player.Backpack.Serial)
        while wood != None:
            prev_wood = wood.Serial                             # linea sobrante
            Items.Move(wood.Serial, escarabajo, 0)
            Misc.Pause(1000)
            test = Items.FindBySerial(wood.Serial)              # linea sobrante
            # Misc.SendMessage("Moviendo MADERA", 6)
            Player.HeadMessage( colors[ 'yellow' ], 'moviendo tablas')
            wood = Items.FindByID(woodID, -1, Player.Backpack.Serial)
            max_tries = max_tries - 1
            if max_tries <= 0:
                break
        # break no hacemos break porque tenemos escarabajo
    # si vemos el mensaje de no hay mas madera, nos detenemos.    
    # theres not enought wood here to harvest 
    if Journal.Search('here to harvest'):
       Player.HeadMessage( colors[ 'red' ], 'Ya no hay troncos aca' )
       Misc.SendMessage("ya no hay troncos aca - terminando script")
       break    
    else:
        Misc.SendMessage("no encontramos nada")