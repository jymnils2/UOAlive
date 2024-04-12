# version 1.0
# requisitos : tener al menos 1 del elemento "axe" en la bolsa, puede ser de una dos manos
#              archivo color.py para que los mensajes se vean a colores
#              Serial del elemento Axe en el inventario
#              Serial de un Escarabajo
#              el escarabajo debe estar en modo seguir 
#              ver "cosas que debes saber hacer"
# descripcion : para iniciar el scrip debes ir alado de un tronco visible
#               el script usara el hacha que escojiste para talar un recurso de madera cercano (alado de tu personaje)
#               en caso de estar pesado transforma los troncos en tablas
#               en caso de que todavia estemos muy pesados mueve las tablas un escarabajo (cuca)
#               cuyo serial debe estar definido dentro del script
#               el script se detendra cada vez que haya teeminado de obtener la madera de un tronco
#               en ese momento habra que moverse a otro
# configuracion este script necesita el serial de escarabajo
#               este script necesita el serial del hacha a usar
#               debe estar configurado para ejecutarse con la tecla F1
# consejos      configurar el cliente para que no muestre el follaje y veas mejor los troncos
#               ver "cosas que debes saber hacer"
#               usar la mejor hacha que dispongas para poder matar enemigos si es necesario
#               llevar un poco de comida, las actividades fisicas hacen que al Player le de hambre
#               usar joyeria y ropa que suba la fuerza (STR) para tener mas capacidad de carga
#               se puede talar practicamente en todos lados, asi que escoge un lugar tranquilo
#               si el script esta asignado a una tecla como F1, esta tecla sirve para iniciarlo y detenerlo
##############################################################################

from colors import colors
# variables que se usaran

WOOD_LOGS = 0x1BDD          # ID de los troncos
axe_serial = 0x40DB04AA     # serial de el hacha que tenemos, podriamos mejorar pidiendo el hacha al principio
hacha_equipada = 0          # para buscar hacha
escarabajo = 0x00056F5E     # serial del escarabajo
woodID = 0x1BD7             # ID de la madera en tablas    la diferencia entre serial y id es que el
                            # serial es unico por items pero el ID es igual para items con el
                            # mismo grafico pero diferente color
#prev_wood = 0  


# creando los pesos para hacer maderas y pasar al escarabajo
peso_maximo = Player.MaxWeight
comenzar_a_hacer_tablas = peso_maximo - 30
dejar_de_talar = peso_maximo - 2
# pidiendo que el usuario nos muestre el hacha a usar, debemos mejorar a autoequipo
# axe_serial = Target.PromptTarget( 'Que hacha usaremos?' )
# autoequiparse el hacha si no esta equipada
hacha_equipada = Player.GetItemOnLayer('LeftHand')
if not hacha_equipada:
    Player.HeadMessage( colors[ 'yellow' ], 'no tenemos el hacha equipada!')
    Player.EquipItem(axe_serial)
    Misc.Pause(600)
# tala arboles hasta estar pesados para cortar o traspasar a escarabajo
Player.HeadMessage( colors[ 'green' ], 'empezando a cortar troncos')
while True:
    Journal.Clear()
    Target.TargetResource(axe_serial,"wood")
    Misc.Pause(1000)
    # si estamos pesados creamos tablas de los troncos.
    if Player.Weight >= comenzar_a_hacer_tablas:
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
    # detenernos si ya no podemos cargar mas!
    if Player.Weight >= dejar_de_talar:
        Player.HeadMessage( colors[ 'cyan' ], 'Muy Pesado ... Detenerse')
        # aca hay que transferir a el escarabajo
        max_tries = 10
        wood = Items.FindByID(woodID, -1, Player.Backpack.Serial)
        while wood != None:
            #prev_wood = wood.Serial                             # linea sobrante
            Items.Move(wood.Serial, escarabajo, 0)
            Misc.Pause(1000)
            #test = Items.FindBySerial(wood.Serial)              # linea sobrante
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
       break    