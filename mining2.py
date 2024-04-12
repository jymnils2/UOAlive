# version 1.0
# requisitos : tener al menos 1 item del elemento "pickaxe" en la bolsa
#              archivo color.py para que los mensajes se vean a colores
#              Serial de un Escarabajo    
#              el escarabajo debe estar en modo seguir 
#              ver "cosas que debes saber hacer"
# descripcion : usa un pickaxe en la bolsa (autoequipa) para minar un recurso mineral cercano (alado de tu personaje)
#               en caso de estar pesado mueve los minerales (ores) a un escarabajo (cuca)
#               cuyo serial debe estar definido dentro del script
#               si tienes mas de un pickaxe en la bolsa el scrip los usara hasta quedarse sin ninguno
#               asi que es bueno llevar unos 3 al menos para llenarse con minerales tanto tu como la cucaracha
# configuracion este scrip necesita el serial de escarabajo
#               debe estar configurado para ejecutarse con la tecla F1
# consejos      usar los guantes de mining (premios BOD) o la picota de mining +10
#               que se consigue en los quest iniciales para fundir minerales
#               asi hay menos chance de fallar y perder la mitad de ellos.
#               un escarabajo nivel 1 (sin entrenar) puede cargar casi 1500 stones de peso
#               llevar al menos 3 picotas para reemplazar las que se usan
#               siempre tener armas disponibles para defenderse de NPCs agresivos o elementales de metal
#               usar joyeria y ropa que suba la fuerza (STR) para tener mas capacidad de carga
#               si ves mucho peligro, por ejemplo elementales de verite, sube a tu cuca y corre por tu vida
#               no uses el scrip si vas a usar picotas de gargola, el chance de que aparezcan elementales es muy alto
#               se puede minar practicamente en todos lados, no necesariamente una mina, en los bosques hay pequeños
#               monticulos que pueden ser minados sin ningun problema por el script
#               si el script esta asignado a una tecla como F1, esta tecla sirve para iniciarlo y detenerlo
##############################################################################

from colors import colors
# ids de los diferentes montones de mineral
# id 01   0x19B7
# id 02   0x19B8
# id 03   0x19B9
# id 04   0x19BA
# variables que se usaran
pickaxeID = 0x0E86          #ID de las picotas
pickaxeserial = 0
escarabajo = 0x00056F5E     # serial del escarabajo, pidamosle el serial al usuario
oreid01 = 0x19B7            # ID de los montones de mineral   la diferencia entre serial y id es que el
oreid02 = 0x19B8            # serial es unico por items pero el ID es igual para items con el
oreid03 = 0x19B9            # mismo grafico pero diferente color
oreid04 = 0x19BA
prev_wood = 0  
max_tries = 6
mano = 0
# creando los pesos para pasar los minerales al escarabajo
peso_maximo = Player.MaxWeight
pesomaximo = peso_maximo - 20
# preguntando cual es nuestro animal de carga
# escarabajo = Target.PromptTarget( 'cual es nuestro animal de carga?' )
# mina minerales hasta estar pesados para traspasarlos al escarabajo
Player.HeadMessage( colors[ 'green' ], 'empezando a minar')
while True:
    mano = Player.GetItemOnLayer('RightHand')
    if not mano:
        # ciclo de busqueda de picas
        pica = Items.FindByID(pickaxeID, -1, Player.Backpack.Serial)
        if pica != None:
            Player.HeadMessage( colors[ 'green' ], 'pica encontrada')
            Player.EquipItem(pica.Serial)
            pickaxeserial = pica.Serial
            Misc.Pause(600)
        else:
            Player.HeadMessage( colors[ 'red' ], 'no hay picas')
            break
        # fin ciclo de busqueda de picas
    else:
        pickaxeserial = mano.Serial

    Journal.Clear()
    # objetivos de targetresource  'ore', 'sand', 'wood', 'graves', 'red mushrooms'
    Target.TargetResource(pickaxeserial,"ore")
    Misc.Pause(1500)
    # minamos hasta que estemos muy pesados.
    # estamos muy pesados
    if Player.Weight >= pesomaximo:
        Player.HeadMessage( colors[ 'red' ], 'estamos muy pesados' )
        # break #no terminamos porque tenemos un escarabajo
        # bloque 01 para 1 monton de mineral, hay 4 montones diferentes
        ore = Items.FindByID(oreid01, -1, Player.Backpack.Serial)
        while ore != None:
            Items.Move(ore.Serial, escarabajo, 0)
            Misc.Pause(1000)
            Player.HeadMessage( colors[ 'yellow' ], 'moviendo minerales')
            ore = Items.FindByID(oreid01, -1, Player.Backpack.Serial)
            max_tries = max_tries - 1
            if max_tries <= 0:
                break
        max_tries = 6
        # bloque 02 para 1 monton de mineral, hay 4 montones diferentes
        ore = Items.FindByID(oreid02, -1, Player.Backpack.Serial)
        while ore != None:
            Items.Move(ore.Serial, escarabajo, 0)
            Misc.Pause(1000)
            # test = Items.FindBySerial(wood.Serial)
            # Misc.SendMessage("Moviendo Mineral", 6)
            Player.HeadMessage( colors[ 'yellow' ], 'moviendo minerales')
            ore = Items.FindByID(oreid02, -1, Player.Backpack.Serial)
            max_tries = max_tries - 1
            if max_tries <= 0:
                break
        max_tries = 6
        # bloque 03 para 1 monton de mineral, hay 4 montones diferentes        
        ore = Items.FindByID(oreid03, -1, Player.Backpack.Serial)
        while ore != None:
            Items.Move(ore.Serial, escarabajo, 0)
            Misc.Pause(1000)
            # test = Items.FindBySerial(wood.Serial)
            # Misc.SendMessage("Moviendo Mineral", 6)
            Player.HeadMessage( colors[ 'yellow' ], 'moviendo minerales')
            ore = Items.FindByID(oreid03, -1, Player.Backpack.Serial)
            max_tries = max_tries - 1
            if max_tries <= 0:
                break
        max_tries = 6
        # bloque 04 para 1 monton de mineral, hay 4 montones diferentes        
        ore = Items.FindByID(oreid04, -1, Player.Backpack.Serial)
        while ore != None:
            Items.Move(ore.Serial, escarabajo, 0)
            Misc.Pause(1000)
            # test = Items.FindBySerial(wood.Serial)
            # Misc.SendMessage("Moviendo Mineral", 6)
            Player.HeadMessage( colors[ 'yellow' ], 'moviendo minerales')
            ore = Items.FindByID(oreid04, -1, Player.Backpack.Serial)
            max_tries = max_tries - 1
            if max_tries <= 0:
                break
        max_tries = 6
    # si vemos el mensaje de no hay mas metal, nos detenemos.    
    # there is no metal here to mine
    if Journal.Search('no metal here to mine'):
       Player.HeadMessage( colors[ 'red' ], 'Ya no mineral' )
       break    
    else:
        Player.HeadMessage( colors[ 'cyan' ], 'Minando' )
        
