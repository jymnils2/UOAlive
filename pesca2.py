# version 1.0
# requisitos : una caña de pesca que debe estar en la mano del personaje
#              haber usado una vez el scrip pesca1 y tener exito en la pesca (animacion de pesca)
#              colocar el serial de la caña de pesca en el scrip  *** mejorar esto
#              ver "cosas que debes saber hacer"
#              archivo color.py para que los mensajes se vean a colores
# descripcion : realiza la actividad de pesca 10 veces en el mismo lugar 
#               donde se realizo la pesca en el scrip pesca1
#               el scrip se corta con un mensaje "Ya no hay peces" si es que
#               hay que cambiar de posicion de pesca, caso contrario
#               se puede ejecutar el scrips muchas veces seguidas
#               sin necesidad de cambiar de posicion de pesca.
# configuracion este escrip debe estar configurado para ejecutarse con la tecla F2
#               y el scrip pesca1 en la tecla F1 para mayor comodidad
# consejos      ya que los peces y trofeos pesan mucho, es bueno andar con una pet de carga
#               una llama o mejor aun una cucaracha para poder meter dentro lo que pesquemos
#               la pesca desde los puertos o la tierra firme no crea moustruos que te ataquen
#               a menos que se realice la pesca a mas de 10 espacios de distancia
#               para subir la habilidad mas que 65 es mejor salir de las ciudades
##############################################################################

from colors import colors
canadepesca = 0x41414DA6    #codigo de la caña de pesca que debemos tener en la mano
cantidad = 0  
pescas = 9                  # cambiar esto para mas intentos de pesca pero cuidado con la policia antimacro
Player.HeadMessage( colors[ 'yellow' ], 'iniciando pesca')
#lugar = Target.PromptGroundTarget('donde pescamos')
while cantidad <= pescas:
    Journal.Clear()
    Items.UseItem(canadepesca)
    Target.WaitForTarget(10000, False)
    Target.Last()
    #Target.TargetExecute(3492, 2601 ,-5 ,6044)
    #Target.TargetExecute(lugar.X, lugar.Y, lugar.Z,6044)
    cantidad = cantidad + 1
    Player.HeadMessage( colors[ 'green' ], 'pesca '+str(cantidad)+' tarda 11 segundos, paciencia')    
    Misc.Pause(11000)           #la pesca tarda 11 segundos, no desesperarse
    if Journal.Search('biting here'):
       Player.HeadMessage( colors[ 'red' ], 'Ya no peces' )
       Misc.SendMessage("ya no hay peces - terminando script")
       break    
Player.HeadMessage( colors[ 'red' ], 'pesca terminada')
